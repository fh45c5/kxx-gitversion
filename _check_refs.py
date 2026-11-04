# -*- coding: utf-8 -*-
import subprocess, re, io, os, collections, bisect

def sh(a):
    return subprocess.run(a, capture_output=True).stdout

tracked = [p.decode("utf-8", "replace") for p in sh(["git", "ls-files", "-z"]).split(b"\x00") if p]
rows = io.open("files_master_summary.tsv", encoding="utf-8").read().splitlines()[1:]
sec = {}
for r in rows:
    p, s, g, c = r.split("\t")
    sec[p] = set(s.split("+"))
D = {p for p, s in sec.items() if ("A" in s or "B" in s) and "C" not in s}
S = [p for p in tracked if p not in D and os.path.exists(p)]

IMAGE = {".png", ".dds", ".tga", ".jpg", ".jpeg", ".bmp", ".gif", ".psd", ".tif", ".tiff", ".webp"}
TEXT = {".txt", ".gui", ".yml", ".lua", ".gfx", ".csv", ".mod", ".asset"}

def ext(p):
    b = p.rsplit("/", 1)[-1]
    return ("." + b.rsplit(".", 1)[-1].lower()) if "." in b else ""

def norm(p):
    return p.replace("\\", "/").replace("//", "/").strip().lower()

def parse_gfx(path):
    lines = io.open(path, encoding="utf-8-sig", errors="replace").read().replace("\r\n", "\n").split("\n")
    out = []
    i = 0
    while i < len(lines):
        if re.match(r"\s*spriteType\s*=\s*\{", lines[i], re.I):
            start = i
            depth = 0
            j = i
            while j < len(lines):
                depth += lines[j].count("{") - lines[j].count("}")
                if depth <= 0:
                    break
                j += 1
            blk = "\n".join(lines[start:j + 1])
            nm = re.search(r'name\s*=\s*"([^"]+)"', blk)
            paths = re.findall(r'(?:texturefile|animationmaskfile|animationtexturefile)\s*=\s*"([^"]+)"', blk, re.I)
            out.append({"name": nm.group(1) if nm else "", "tex": paths, "start": start + 1, "end": j + 1, "code": blk})
            i = j + 1
        else:
            i += 1
    return out

Dgfx = sorted(p for p in D if p.lower().endswith(".gfx") and os.path.exists(p))
Sgfx = sorted(p for p in S if p.lower().endswith(".gfx"))
Dblocks = []
for f in Dgfx:
    for b in parse_gfx(f):
        b["file"] = f
        Dblocks.append(b)
Snames = set()
for f in Sgfx:
    for b in parse_gfx(f):
        if b["name"]:
            Snames.add(b["name"])

names = {b["name"] for b in Dblocks if b["name"]}
tex = set()
for b in Dblocks:
    for t in b["tex"]:
        tex.add(norm(t))
Dimg = {p for p in D if ext(p) in IMAGE}
Dimg_norm = {norm(p) for p in Dimg}

NAME_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_\-]{2,}")
QRE = re.compile(r'"([^"\n]{1,300})"')

name_refs = collections.defaultdict(list)
tex_refs = collections.defaultdict(list)

for p in S:
    if ext(p) not in TEXT:
        continue
    try:
        t = io.open(p, encoding="utf-8-sig", errors="replace").read()
    except Exception:
        continue
    if not t:
        continue
    offs = [0]
    for m in re.finditer("\n", t):
        offs.append(m.end())
    def line(m):
        return bisect.bisect_right(offs, m.start())
    for m in NAME_RE.finditer(t):
        w = m.group(0).rstrip("-")
        if w in names:
            name_refs[w].append((p, line(m)))
    for m in QRE.finditer(t):
        v = norm(m.group(1))
        if v in Dimg_norm:
            tex_refs[v].append((p, line(m)))

STUB = {n for n in names if len(n) <= 5}
cannot_names = {n: v for n, v in name_refs.items() if n not in Snames and n not in STUB}
stub_names = {n: v for n, v in name_refs.items() if n not in Snames and n in STUB}
cannot_blocks = [b for b in Dblocks if b["name"] in cannot_names]
stub_blocks = [b for b in Dblocks if b["name"] in stub_names]
cannot_imgs = {p for p in tex_refs if p in Dimg_norm}
for b in cannot_blocks:
    for t in b["tex"]:
        n = norm(t)
        if n in Dimg_norm:
            cannot_imgs.add(n)

# .gfx with/without needed blocks
gfx_needed = collections.Counter()
for b in cannot_blocks:
    gfx_needed[b["file"]] += 1

files_with_refs = set()
for n, v in cannot_names.items():
    for f, ln in v:
        files_with_refs.add(f)
for p, v in tex_refs.items():
    for f, ln in v:
        files_with_refs.add(f)

out = []
out.append("# 删除前的引用检查")
out.append("")
out.append("检查对象：删除集 = §A ∪ §B 去掉 §C（被排除项），共 **%d** 个文件；存活集 = 本 mod 其余全部文件（%d 个）。" % (len(D), len(S)))
out.append("")
out.append("## 概览")
out.append("")
out.append("| 项目 | 数量 |")
out.append("|---|---|")
out.append("| 删除集文件 | %d |" % len(D))
out.append("| 删除集里的 .gfx | %d |" % len(Dgfx))
out.append("| 删除集里的图片 | %d |" % len(Dimg))
out.append("| 删除集 .gfx 注册的 sprite 条数 | %d |" % len(Dblocks))
out.append("| **被存活文件引用、不能删的 sprite** | **%d** |" % len(cannot_names))
out.append("| 这些 sprite 落在的 .gfx 文件数 | %d |" % len(gfx_needed))
out.append("| **被存活文件引用、不能删的图片** | **%d** |" % len(cannot_imgs))
out.append("| 引用它们的存活文件数 | %d |" % len(files_with_refs))
out.append("| 坏注册块（name 被截断，如 `GFX_`） | %d |" % len(stub_blocks))
out.append("")
out.append("说明：sprite 若在存活 .gfx 里也有同名定义，则不算冲突（已排除）；图片按路径字符串匹配（含存活 .gfx 的 texturefile/mask 行）。name 长度 ≤5 的块（例如整段被截断成 `GFX_`）单独列在下面，不计入上面的“不能删”统计。")
out.append("")

out.append("## 不能删的注册块（按 .gfx 分组）")
out.append("")
for f in sorted(gfx_needed, key=lambda x: (-gfx_needed[x], x)):
    blocks = [b for b in cannot_blocks if b["file"] == f]
    out.append("### `%s` — 需保留 %d 块 / 共 %d 块" % (f, len(blocks), sum(1 for b in Dblocks if b["file"] == f)))
    out.append("")
    for b in sorted(blocks, key=lambda x: x["start"]):
        refs = cannot_names.get(b["name"], [])[:8]
        out.append("- 行 %d–%d，`%s`" % (b["start"], b["end"], b["name"]))
        out.append("")
        out.append("```")
        out.append(b["code"])
        out.append("```")
        out.append("")
        if refs:
            out.append("  被引用：" + "、".join("`%s:%d`" % (p, ln) for p, ln in refs) + ("" if len(cannot_names[b["name"]]) <= 8 else " …共 %d 处" % len(cannot_names[b["name"]])))
            out.append("")
out.append("")

out.append("## 坏注册块（name 被截断，未计入“不能删”）")
out.append("")
out.append("这些 spriteType 的 name 只剩很短的前缀（如 `GFX_`），贴图与引用都不可靠；保留它们只会引入无效注册。")
out.append("")
stub_by_file = collections.defaultdict(list)
for b in stub_blocks:
    stub_by_file[b["file"]].append(b)
for f in sorted(stub_by_file):
    bs = sorted(stub_by_file[f], key=lambda x: x["start"])
    out.append("### `%s`（%d 块）" % (f, len(bs)))
    out.append("")
    out.append("```")
    for b in bs:
        out.append("行 %d–%d  name=%s  tex=%s" % (b["start"], b["end"], b["name"], ";".join(b["tex"])))
    out.append("```")
    out.append("")
out.append("")

out.append("## 不能删的图片")
out.append("")
out.append("| 图片 | 引用处（最多 5 个） |")
out.append("|---|---|")
for p in sorted(cannot_imgs):
    refs = tex_refs.get(p, [])
    s = "、".join("`%s:%d`" % (f, ln) for f, ln in refs[:5])
    if len(refs) > 5:
        s += " …共 %d 处" % len(refs)
    out.append("| `%s` | %s |" % (p, s))
out.append("")

out.append("## 可整体删除的 .gfx（无被引用的块）")
out.append("")
out.append("```")
for f in Dgfx:
    if f not in gfx_needed:
        out.append(f)
out.append("```")
out.append("")

out.append("## 需保留/编辑的 .gfx")
out.append("")
out.append("```")
for f in sorted(gfx_needed):
    out.append("%s  (%d 块需保留)" % (f, gfx_needed[f]))
out.append("```")
out.append("")

io.open("refs_check_report.md", "w", encoding="utf-8", newline="\n").write("\n".join(out))
with io.open("refs_check.tsv", "w", encoding="utf-8", newline="\n") as fh:
    fh.write("type\tfile\titem\trefs\n")
    for b in cannot_blocks:
        refs = ";".join("%s:%d" % x for x in cannot_names.get(b["name"], []))
        fh.write("block\t%s\t%s\t%s\n" % (b["file"], b["name"], refs))
    for p in sorted(cannot_imgs):
        refs = ";".join("%s:%d" % x for x in tex_refs.get(p, []))
        fh.write("image\t%s\t%s\t%s\n" % (p, p, refs))
    for b in stub_blocks:
        fh.write("stub\t%s\t%s\t-\n" % (b["file"], b["name"]))

print("D:", len(D), "S:", len(S))
print("Dgfx:", len(Dgfx), "Dimg:", len(Dimg))
print("blocks:", len(Dblocks), "Snames:", len(Snames))
print("cannot names:", len(cannot_names), "blocks:", len(cannot_blocks), "gfx:", len(gfx_needed))
print("stub blocks:", len(stub_blocks), "stub names:", len(stub_names))
print("cannot imgs:", len(cannot_imgs), "ref files:", len(files_with_refs))
print("md lines:", len(out))
print("top gfx:", [(f, c) for f, c in gfx_needed.most_common(8)])
