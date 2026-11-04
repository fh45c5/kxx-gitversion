# -*- coding: utf-8 -*-
import subprocess, re, io
from collections import Counter, defaultdict

def sh(a):
    return subprocess.run(a, capture_output=True).stdout

files = [p.decode("utf-8") for p in sh(["git", "ls-files", "-z"]).split(b"\x00") if p]
tokre = re.compile(r"[^a-z0-9]+")
EXTRA = {"jpn","nippon","nihon","tokyo","yamato","shogun","sakura","meiji","hirohito",
         "tojo","ijn","ija","kyoto","okinawa","ryukyu","hokkaido","shinto","bushido",
         "samurai","mikado","tenno"}

def toks(s):
    return [t for t in tokre.split(s.lower()) if t]

def m_jp(s):
    ts = toks(s)
    return any("jap" in t for t in ts) or bool(set(ts) & EXTRA)

def m_tw(s):
    ts = toks(s)
    return any(t.startswith("tai") and not t.startswith("taiping") for t in ts) or "formosa" in ts or "twn" in ts

def m_kr(s):
    ts = toks(s)
    return any(t in {"kor","korea","korean","koreans","korjuche","prk","choson","joseon"}
               or t.startswith(("korea","korju","choson","joseon")) for t in ts)

def m_xb(s):
    ts = toks(s)
    return any(t in {"tib","tibet","tibetan"} or t.startswith(("tibet","tib")) for t in ts)

MATCH = {"日本": m_jp, "台湾": m_tw, "朝鲜": m_kr, "西藏": m_xb}

def region_tags(path, mode):
    # mode "base": basename only; "path": any path component
    target = path.split("/")[-1] if mode == "base" else path
    return [r for r in MATCH if MATCH[r](target)]

def dir_prefixed(p):
    return any(x.upper().startswith(("KXX_", "SCB_")) for x in p.split("/")[:-1])

def jp_excl(p):
    b = p.split("/")[-1]
    if b.upper().startswith(("KXX_", "SCB_")):
        return "A 文件名 KXX_/SCB_ 前缀"
    if dir_prefixed(p):
        return "B 位于 KXX_/SCB_ 目录"
    if "socialist" in b.lower():
        return "C 含 Socialist"
    if p == "history/countries/JAP - Japan.txt":
        return "D JAP - Japan.txt"
    return None

pref = [p for p in files if p.split("/")[-1].startswith(("RD_", "focus-"))]

def pref_group(p):
    tags = region_tags(p, "base")
    return tags[0] if tags else "其他"

pgroups = defaultdict(list)
for p in pref:
    pgroups[pref_group(p)].append(p)

regions = ["日本", "台湾", "朝鲜", "西藏"]
rpaths = {}
for r in regions:
    paths = [p for p in files if region_tags(p, "path") and (r in region_tags(p, "path"))]
    if r == "日本":
        paths = [p for p in paths if not jp_excl(p)]
    rpaths[r] = sorted(paths)

excl = defaultdict(list)
for p in files:
    if m_jp(p):
        why = jp_excl(p)
        if why:
            excl[why[0]].append(p)

union = set(pref)
for r in regions:
    union.update(rpaths[r])
for k in excl:
    union.update(excl[k])

rows = []
rows.append("# RD_/focus- 文件与四地区相关文件清单")
rows.append("")
rows.append("范围：`E:\\Games\\kxx-gitversion`（git 跟踪文件）。路径均相对仓库根。")
rows.append("")
rows.append("## 规则说明")
rows.append("")
rows.append("- **A 类（RD_/focus-）**：文件名以 `RD_` 或 `focus-` 开头的文件，共 %d 个，按文件名里的地区词分成 日本/台湾/朝鲜/西藏/其他。" % len(pref))
rows.append("- **B 类（四地区相关）**：**任意路径段（目录名或文件名）**命中地区词的文件，不限前缀：日本=包含 jap* / jpn / nippon / nihon / tokyo / yamato / shogun / sakura / meiji / hirohito / tojo / ijn / ija / kyoto / okinawa / ryukyu / hokkaido / shinto / bushido / samurai / mikado / tenno；台湾=tai*（Taipei/Taiwan/…，排除 Taiping）、formosa、twn；朝鲜=kor/korea/korean/korjuche/prk/choson/joseon；西藏=tib/tibet/tibetan。")
rows.append("- 日本 B 类按你的要求排除：①文件名 KXX_/SCB_ 前缀；②位于 KXX_/SCB_ 目录；③含 Socialist 字样；④`history/countries/JAP - Japan.txt`。这些被排除的文件在 §C 单独列出。")
rows.append("")
rows.append("## 汇总")
rows.append("")
rows.append("| 项目 | 数量 |")
rows.append("|---|---|")
rows.append("| A：RD_/focus- 文件 | %d |" % len(pref))
for r in regions:
    rows.append("| A·%s | %d |" % (r, len(pgroups.get(r, []))))
rows.append("| A·其他 | %d |" % len(pgroups.get("其他", [])))
rows.append("| B：日本相关（已排除 §C） | %d |" % len(rpaths["日本"]))
rows.append("| B：台湾相关 | %d |" % len(rpaths["台湾"]))
rows.append("| B：朝鲜相关 | %d |" % len(rpaths["朝鲜"]))
rows.append("| B：西藏相关 | %d |" % len(rpaths["西藏"]))
rows.append("| C：日本排除项合计 | %d |" % sum(len(v) for v in excl.values()))
for k in sorted(excl):
    rows.append("| C·%s | %d |" % (k, len(excl[k])))
rows.append("| A∪B∪C 去重合计 | %d |" % len(union))
rows.append("")

rows.append("## §A 全部 RD_/focus- 文件（%d）" % len(pref))
rows.append("")
for r in regions + ["其他"]:
    ps = sorted(pgroups.get(r, []))
    rows.append("### A·%s（%d）" % (r, len(ps)))
    rows.append("")
    if not ps:
        rows.append("（无）")
        rows.append("")
        continue
    rows.append("```")
    rows.extend(ps)
    rows.append("```")
    rows.append("")

rows.append("## §B 四地区相关文件（不限前缀，%d 个）" % sum(len(rpaths[r]) for r in regions))
rows.append("")
rows.append("同一文件可能同时属于多个地区组；组内数字为组内条数。")
rows.append("")
for r in regions:
    ps = rpaths[r]
    rows.append("### B·%s（%d）" % (r, len(ps)))
    rows.append("")
    rows.append("```")
    rows.extend(ps)
    rows.append("```")
    rows.append("")

rows.append("## §C 日本被排除项（%d，单独列出）" % sum(len(v) for v in excl.values()))
rows.append("")
for k in sorted(excl):
    ps = sorted(excl[k])
    rows.append("### C·%s（%d）" % (k, len(ps)))
    rows.append("")
    rows.append("```")
    rows.extend(ps)
    rows.append("```")
    rows.append("")

rows.append("## 重叠与备注")
rows.append("")
overlap = 0
for r in regions:
    overlap += len(set(rpaths[r]) & set(pref))
rows.append("- §A 的 %d 个文件里，有 %d 个同时出现在 §B（四地区相关）。" % (len(pref), overlap))
multi = [p for p in set().union(*[set(rpaths[r]) for r in regions]) if sum(1 for r in regions if p in rpaths[r]) > 1]
rows.append("- §B 内部跨地区重复文件：%d 个（如同时含 Japan 与 Taiwan 词）。" % len(multi))
for p in sorted(multi)[:50]:
    rows.append("  - `%s`" % p)
rows.append("")

io.open("rd_focus_region_report.md", "w", encoding="utf-8", newline="\n").write("\n".join(rows))

with io.open("rd_focus_region_report.tsv", "w", encoding="utf-8", newline="\n") as f:
    f.write("section\tgroup\tpath\n")
    for r in regions + ["其他"]:
        for p in sorted(pgroups.get(r, [])):
            f.write("A\t%s\t%s\n" % (r, p))
    for r in regions:
        for p in rpaths[r]:
            f.write("B\t%s\t%s\n" % (r, p))
    for k in sorted(excl):
        for p in sorted(excl[k]):
            f.write("C\t%s\t%s\n" % (k, p))

print("pref", len(pref), {r: len(pgroups.get(r, [])) for r in regions + ["其他"]})
print("B", {r: len(rpaths[r]) for r in regions})
print("C", {k: len(v) for k, v in sorted(excl.items())}, "sum", sum(len(v) for v in excl.values()))
print("union", len(union), "md lines", len(rows))
