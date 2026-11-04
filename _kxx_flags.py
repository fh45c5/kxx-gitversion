# -*- coding: utf-8 -*-
import io, re, collections

REFS = "refs_check.tsv"
OUT = "interface/KXX_game_rules_flags.gfx"

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

def fmt(b):
    return "    SpriteType = {\n" + "\n".join(reindent(b["inner"])) + "\n    }"

# collect flag blocks; on duplicate sprite name the file that loads later wins
best = {}
for f, names in kept.items():
    for b in parse_blocks(f):
        if b["name"] in names and b["tex"].replace("\\", "/").lower().startswith("gfx/flags/"):
            cur = best.get(b["name"])
            if cur is None or b["file"] > cur["file"]:
                best[b["name"]] = b

blocks = [best[k] for k in sorted(best)]
write = "spriteTypes = {\n" + "\n".join(fmt(b) for b in blocks) + "\n}\n"
io.open(OUT, "w", encoding="utf-8", newline="\n").write(write)
print("wrote", OUT, "sprites:", len(blocks))
for b in blocks:
    print("  ", b["name"], "->", b["tex"])
