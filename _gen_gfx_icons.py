# -*- coding: utf-8 -*-
import io, re, collections

rows = io.open("rd_focus_region_report.tsv", encoding="utf-8").read().splitlines()[1:]
by_sec = collections.defaultdict(set)
group_of = {}
for line in rows:
    s, g, p = line.split("\t")
    by_sec[s].add(p)
    group_of.setdefault(p, set()).add(s + "·" + g)

gfx_secs = collections.defaultdict(set)
for s, ps in by_sec.items():
    for p in ps:
        if p.lower().endswith(".gfx"):
            gfx_secs[p].add(s)

def primary(p):
    s = gfx_secs[p]
    for k in ("A", "B", "C"):
        if k in s:
            return k
    return "?"

blocks = []
for p in sorted(gfx_secs):
    txt = io.open(p, encoding="utf-8-sig", errors="replace").read().replace("\r\n", "\n")
    for m in re.finditer(r"(?im)^[ \t]*spriteType\s*=\s*\{", txt):
        i = m.end() - 1
        depth = 0
        j = i
        while j < len(txt):
            if txt[j] == "{":
                depth += 1
            elif txt[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        blk = txt[m.start():j + 1]
        nm = re.search(r'name\s*=\s*"([^"]+)"', blk)
        paths = re.findall(r'(?:texturefile|animationmaskfile|animationtexturefile)\s*=\s*"([^"]+)"', blk, re.I)
        # 去重保序
        seen = []
        for x in paths:
            if x not in seen:
                seen.append(x)
        blocks.append((p, nm.group(1) if nm else "(no name)", seen))

by_file = collections.defaultdict(list)
for p, n, ps in blocks:
    by_file[p].append((n, ps))

sec_files = collections.defaultdict(list)
for p in by_file:
    sec_files[primary(p)].append(p)
for k in sec_files:
    sec_files[k].sort()

allnames = [n for _, n, _ in blocks]
uniq_names = len(set(allnames))

out = []
out.append("# 这些 .gfx 中注册的图标清单")
out.append("")
out.append("范围：`E:\\Games\\kxx-gitversion`。来源为上一步清单（§A RD_/focus- 全量、§B 四地区相关、§C 日本排除项）里出现的全部 .gfx 文件。")
out.append("")
out.append("每条格式：`图标(sprite 名)  →  贴图路径`；同一 sprite 若带 shine 动画，会列出 texturefile 与 animationmaskfile（分号分隔）。")
out.append("")
out.append("## 汇总")
out.append("")
out.append("| 来源 | .gfx 数 | sprite 条数 |")
out.append("|---|---|---|")
for k in ("A", "B", "C"):
    fs = sec_files.get(k, [])
    n = sum(len(by_file[f]) for f in fs)
    out.append("| %s | %d | %d |" % (k, len(fs), n))
out.append("| 合计（去重 .gfx） | %d | %d |" % (len(by_file), len(blocks)))
out.append("")
out.append("唯一 sprite 名：%d（%d 条注册，存在重名）。" % (uniq_names, len(blocks)))
out.append("")
out.append("## 文件一览")
out.append("")
out.append("| .gfx | 来源 | sprite 数 |")
out.append("|---|---|---|")
for p in sorted(by_file, key=lambda x: (primary(x), -len(by_file[x]), x)):
    out.append("| `%s` | %s | %d |" % (p, "+".join(sorted(gfx_secs[p])), len(by_file[p])))
out.append("")

for k in ("A", "B", "C"):
    fs = sec_files.get(k, [])
    out.append("## §%s（%d 个 .gfx，%d 条 sprite）" % (k, len(fs), sum(len(by_file[f]) for f in fs)))
    out.append("")
    for p in fs:
        items = by_file[p]
        out.append("### `%s`（%d）" % (p, len(items)))
        out.append("")
        out.append("```")
        for n, ps in items:
            out.append("%s  ->  %s" % (n, " ; ".join(ps) if ps else "(无贴图)"))
        out.append("```")
        out.append("")

io.open("rd_focus_gfx_icons.md", "w", encoding="utf-8", newline="\n").write("\n".join(out))

with io.open("rd_focus_gfx_icons.tsv", "w", encoding="utf-8", newline="\n") as f:
    f.write("gfx\tsection\tsprite\ttextures\n")
    for p in sorted(by_file, key=lambda x: (primary(x), x)):
        for n, ps in by_file[p]:
            f.write("%s\t%s\t%s\t%s\n" % (p, "+".join(sorted(gfx_secs[p])), n, ";".join(ps)))

print("gfx files:", len(by_file), "blocks:", len(blocks), "unique names:", uniq_names)
for k in ("A", "B", "C"):
    print(k, len(sec_files.get(k, [])), sum(len(by_file[f]) for f in sec_files.get(k, [])))
print("md lines:", len(out))
print("top:", [(f, len(v)) for f, v in sorted(by_file.items(), key=lambda x: -len(x[1]))[:8]])
