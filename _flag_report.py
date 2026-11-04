# -*- coding: utf-8 -*-
import io, re, os, collections

REFS = "refs_check.tsv"
kept = collections.defaultdict(set)
for line in io.open(REFS, encoding="utf-8").read().splitlines()[1:]:
    p = line.split("\t")
    if p and p[0] == "block":
        kept[p[1]].add(p[2])

def read(p):
    raw = open(p, "rb").read()
    return raw.decode("utf-8-sig" if raw.startswith(b"\xef\xbb\xbf") else "utf-8").replace("\r\n", "\n")

def parse_blocks(path):
    lines = read(path).split("\n")
    res = []
    i = 0
    while i < len(lines):
        if re.match(r"\s*spriteType\s*=\s*\{", lines[i], re.I):
            d = 0
            j = i
            while j < len(lines):
                d += lines[j].count("{") - lines[j].count("}")
                if d <= 0:
                    break
                j += 1
            blk = "\n".join(lines[i:j + 1])
            nm = re.search(r'name\s*=\s*"([^"]+)"', blk)
            tex = re.search(r'(?i)texturefile\s*=\s*"([^"]+)"', blk)
            res.append((nm.group(1) if nm else "", tex.group(1) if tex else "", path))
            i = j + 1
        else:
            i += 1
    return res

flags = []
for f, names in kept.items():
    for n, t, pf in parse_blocks(f):
        if n in names and t.replace("\\", "/").lower().startswith("gfx/flags/"):
            flags.append((n, t, pf))

files = []
for r, ds, fs in os.walk("."):
    if ".git" in ds:
        ds.remove(".git")
    for fn in fs:
        if fn.endswith((".txt", ".gfx", ".gui", ".yml", ".lua", ".mod")):
            files.append(os.path.join(r, fn).replace("\\", "/")[2:])

out = []
out.append("flags=%d" % len(flags))
for n, t, pf in flags:
    out.append("\n## %s -> %s" % (n, t))
    out.append("定义: %s" % pf)
    hits = []
    for f in files:
        if f == pf:
            continue
        txt = io.open(f, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"\b" + re.escape(n) + r"\b", txt):
            ln = txt.count("\n", 0, m.start()) + 1
            hits.append("%s:%d: %s" % (f, ln, txt.splitlines()[ln - 1].strip()[:150]))
    out.append("引用数: %d" % len(hits))
    for h in hits:
        out.append("  " + h)

io.open("_flags_report.txt", "w", encoding="utf-8").write("\n".join(out))
print("done", len(flags))
