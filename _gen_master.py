# -*- coding: utf-8 -*-
import io, collections

rows = io.open("rd_focus_region_report.tsv", encoding="utf-8").read().splitlines()[1:]
byfile = collections.defaultdict(lambda: {"sec": set(), "grp": set()})
for r in rows:
    s, g, p = r.split("\t")
    byfile[p]["sec"].add(s)
    byfile[p]["grp"].add(g)

files = sorted(byfile)
secs = collections.Counter()
for p, v in byfile.items():
    for s in v["sec"]:
        secs[s] += 1

A = {p for p, v in byfile.items() if "A" in v["sec"]}
B = {p for p, v in byfile.items() if "B" in v["sec"]}
C = {p for p, v in byfile.items() if "C" in v["sec"]}

def base(p): return p.split("/")[-1]
def dirs(p): return p.split("/")[:-1]
def reason(p):
    b = base(p)
    rs = []
    if b.upper().startswith(("KXX_", "SCB_")):
        rs.append("文件名 KXX_/SCB_ 前缀")
    if any(d.upper().startswith(("KXX_", "SCB_")) for d in dirs(p)):
        rs.append("目录 KXX_/SCB_")
    if "socialist" in b.lower():
        rs.append("含 Socialist 字样")
    if p == "history/countries/JAP - Japan.txt":
        rs.append("JAP - Japan.txt")
    return "、".join(rs) if rs else ""

# group names (regions) per file
regions = collections.Counter()
for p, v in byfile.items():
    for g in v["grp"]:
        if g not in ("A", "B", "C", "D", "其他"):
            regions[g] += 1

def ext(p):
    b = base(p)
    return ("." + b.rsplit(".", 1)[-1].lower()) if "." in b else "(无扩展名)"

def dir2(p):
    parts = p.split("/")
    return "/".join(parts[:2]) if len(parts) > 1 else "(根)"

# icons
irows = io.open("rd_focus_gfx_icons.tsv", encoding="utf-8").read().splitlines()[1:]
gfx_icons = collections.Counter()
for r in irows:
    gfx_icons[r.split("\t")[0]] += 1
gfx_total = sum(gfx_icons.values())

out = []
out.append("# 文件总汇总（含被排除项）")
out.append("")
out.append("范围：`E:\\Games\\kxx-gitversion`。合并上一步报告的三个来源：")
out.append("")
out.append("- **§A**：文件名以 `RD_` / `focus-` 开头的全部文件")
out.append("- **§B**：与日本 / 台湾 / 朝鲜 / 西藏相关的文件（路径任一段命中，不限前缀）")
out.append("- **§C**：日本部分里被排除的项（KXX_/SCB_ 前缀、KXX_/SCB_ 目录、含 Socialist、`history/countries/JAP - Japan.txt`）")
out.append("")
out.append("## 总览")
out.append("")
out.append("| 项目 | 数量 |")
out.append("|---|---|")
out.append("| 去重后文件总数 | **%d** |" % len(files))
out.append("| §A | %d |" % len(A))
out.append("| §B | %d |" % len(B))
out.append("| §C（被排除项） | %d |" % len(C))
out.append("| §A ∩ §B | %d |" % len(A & B))
out.append("| §A ∩ §C | %d |" % len(A & C))
out.append("| §B ∩ §C | %d |" % len(B & C))
out.append("")
out.append("三个来源相加为 %d 条记录，去重后 %d 个文件（重复计入见上表交集）。" % (len(A) + len(B) + len(C), len(files)))
out.append("")
out.append("地区分组（§B）：" + "、".join("%s %d" % (k, v) for k, v in regions.most_common()))
out.append("")
out.append("（同一文件可同时命中多个地区，地区计数之和为 %d，§B 去重后为 %d。）" % (sum(regions.values()), len(B)))
if B & C:
    out.append("")
    out.append("§B ∩ §C 的文件：" + "、".join("`%s`" % p for p in sorted(B & C)))
out.append("")
out.append("## §C 被排除项的构成")
out.append("")
rc = collections.Counter()
for p in C:
    rc[reason(p)] += 1
out.append("| 排除原因 | 文件数 |")
out.append("|---|---|")
for k, v in rc.most_common():
    out.append("| %s | %d |" % (k, v))
out.append("")
out.append("## 按扩展名")
out.append("")
out.append("| 扩展名 | 合计（去重文件） |")
out.append("|---|---|")
ec = collections.Counter(ext(p) for p in files)
for k, v in ec.most_common():
    out.append("| %s | %d |" % (k, v))
out.append("")
out.append("## 按目录（前 20）")
out.append("")
out.append("| 目录 | 文件数 |")
out.append("|---|---|")
dc = collections.Counter(dir2(p) for p in files)
for k, v in dc.most_common(20):
    out.append("| `%s` | %d |" % (k, v))
out.append("")
out.append("## .gfx 与图标")
out.append("")
out.append("- 去重 .gfx：**%d 个**（§A 113 / 仅 §B 10 / §C 3），共注册 **%d 条** sprite。" % (len(gfx_icons), gfx_total))
out.append("- 图标明细见 `rd_focus_gfx_icons.md` / `.tsv`。")
out.append("")
out.append("## 完整合并清单（%d）" % len(files))
out.append("")
out.append("每条格式：`[来源] 路径`；来源为 A/B/C 的组合，C 的条目后缀排除原因。")
out.append("")
out.append("```")
for p in files:
    v = byfile[p]
    tag = "+".join(sorted(v["sec"]))
    if "C" in v["sec"]:
        tag += " | " + reason(p)
    out.append("[%s] %s" % (tag, p))
out.append("```")
out.append("")

io.open("files_master_summary.md", "w", encoding="utf-8", newline="\n").write("\n".join(out))

with io.open("files_master_summary.tsv", "w", encoding="utf-8", newline="\n") as f:
    f.write("path\tsections\tgroups\tc_reason\n")
    for p in files:
        v = byfile[p]
        f.write("%s\t%s\t%s\t%s\n" % (p, "+".join(sorted(v["sec"])), "+".join(sorted(v["grp"])), reason(p) if "C" in v["sec"] else ""))

print("unique:", len(files), "A:", len(A), "B:", len(B), "C:", len(C))
print("A&B:", len(A & B), "A&C:", len(A & C), "B&C:", len(B & C))
print("regions:", dict(regions))
print("md lines:", len(out))
print("gfx:", len(gfx_icons), gfx_total)
