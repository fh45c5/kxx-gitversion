# -*- coding: utf-8 -*-
import io, re, os, collections, subprocess

ROOT = "."
REFS = "refs_check.tsv"
TARGETS = {
    "ideologies": "interface/KXX_ideologies.gfx",
    "decisions": "interface/KXX_decisions.gfx",
    "ministers": "interface/KXX_ministers.gfx",
}

kept = collections.defaultdict(set)
for line in io.open(REFS, encoding="utf-8").read().splitlines()[1:]:
    parts = line.split("\t")
    if parts and parts[0] == "block":
        kept[parts[1]].add(parts[2])

def read(p):
    raw = open(p, "rb").read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    txt = raw.decode("utf-8-sig" if bom else "utf-8")
    crlf = "\r\n" in txt
    return txt.replace("\r\n", "\n"), bom, crlf

def write(p, txt):
    open(p, "wb").write(txt.encode("utf-8"))

def parse_blocks(path):
    txt, _, _ = read(path)
    lines = txt.split("\n")
    res = []
    i = 0
    while i < len(lines):
        if re.match(r"\s*spriteType\s*=\s*\{", lines[i], re.I):
            depth = 0
            j = i
            while j < len(lines):
                depth += lines[j].count("{") - lines[j].count("}")
                if depth <= 0:
                    break
                j += 1
            blk = "\n".join(lines[i:j + 1])
            nm = re.search(r'name\s*=\s*"([^"]+)"', blk)
            tex = re.search(r'(?i)texturefile\s*=\s*"([^"]+)"', blk)
            res.append({"name": nm.group(1) if nm else "", "tex": tex.group(1) if tex else "",
                        "inner": lines[i + 1:j], "file": path})
            i = j + 1
        else:
            i += 1
    return res

def reindent(inner):
    out = []
    depth = 0
    for ln in inner:
        s = ln.strip()
        if not s:
            continue
        if s.startswith("}"):
            depth = max(0, depth - 1)
            out.append("\t" * (2 + depth) + s)
        else:
            out.append("\t" * (2 + depth) + s)
            depth += s.count("{") - s.count("}")
    return out

def fmt(block):
    return "    SpriteType = {\n" + "\n".join(reindent(block["inner"])) + "\n    }"

def build_file(path, blocks):
    body = "\n".join(fmt(b) for b in blocks)
    write(path, "spriteTypes = {\n" + body + "\n}\n")

groups = collections.defaultdict(list)
flags = []
allblocks = {}
for f, names in kept.items():
    for b in parse_blocks(f):
        allblocks[(f, b["name"])] = b

for f, names in sorted(kept.items()):
    for name in sorted(names):
        b = allblocks.get((f, name))
        if not b:
            continue
        t = b["tex"].replace("\\", "/").lower()
        if t.startswith("gfx/interface/goals/") or t.startswith("gfx/interface/ideas/") or t.startswith("gfx/event_pictures/"):
            continue
        if t.startswith("gfx/interface/ideologies/"):
            groups["ideologies"].append(b)
        elif t.startswith("gfx/interface/decisions/"):
            groups["decisions"].append(b)
        elif t.startswith("gfx/flags/"):
            flags.append(b)
        else:
            groups["ministers"].append(b)

for k, path in TARGETS.items():
    build_file(path, groups[k])
    print("%s: %d blocks -> %s" % (k, len(groups[k]), path))

print("ministers textures:")
for b in groups["ministers"]:
    print("   ", b["name"], "->", b["tex"])

print("\nFLAGS (%d):" % len(flags))
exts = (".txt", ".gfx", ".gui", ".yml", ".lua", ".mod")
files = []
for r, ds, fs in os.walk(ROOT):
    if ".git" in ds:
        ds.remove(".git")
    for fn in fs:
        if fn.endswith(exts):
            files.append(os.path.join(r, fn).replace("\\", "/")[2:])
for b in flags:
    name = b["name"]
    hits = []
    for f in files:
        if f == b["file"] or not os.path.exists(f):
            continue
        try:
            t = io.open(f, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        for m in re.finditer(r"\b" + re.escape(name) + r"\b", t):
            ln = t.count("\n", 0, m.start()) + 1
            line = t.splitlines()[ln - 1].strip()
            hits.append("%s:%d: %s" % (f, ln, line[:160]))
    print("\n%s -> %s  (定义于 %s)" % (name, b["tex"], b["file"]))
    if not hits:
        print("   未被其他文件引用")
    for h in hits:
        print("   ", h)
