# -*- coding: utf-8 -*-
import io, re

MIN = "interface/KXX_ministers.gfx"
IDEAS = "interface/KXX_ideas.gfx"
MOVE = ["GFX_idea_PHI_Lius_Taruc_eco_rso", "GFX_idea_PHI_Vincente_Soto_eco_sde"]

def read(p):
    raw = open(p, "rb").read()
    return raw.decode("utf-8-sig" if raw.startswith(b"\xef\xbb\xbf") else "utf-8").replace("\r\n", "\n")

def parse(path):
    txt = read(path)
    lines = txt.split("\n")
    blocks = []
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
            blocks.append((nm.group(1) if nm else "", lines[i:j + 1]))
            i = j + 1
        else:
            i += 1
    return txt, blocks

def fmt(lines):
    out = []
    depth = 0
    for ln in lines[1:-1]:
        s = ln.strip()
        if not s:
            continue
        if s.startswith("}"):
            depth = max(0, depth - 1)
            out.append("\t" * (2 + depth) + s)
        else:
            out.append("\t" * (2 + depth) + s)
            depth += s.count("{") - s.count("}")
    return "    SpriteType = {\n" + "\n".join(out) + "\n    }"

ideas_txt, ideas_blocks = parse(IDEAS)
moved = [b for b in ideas_blocks if b[0] in MOVE]
rest = [b for b in ideas_blocks if b[0] not in MOVE]
assert len(moved) == 2, len(moved)
io.open(IDEAS, "w", encoding="utf-8", newline="\n").write(
    "spriteTypes = {\n" + "\n".join(fmt(l) for _, l in rest) + "\n}\n")

min_txt, min_blocks = parse(MIN)
body = "\n".join(fmt(l) for _, l in min_blocks)
io.open(MIN, "w", encoding="utf-8", newline="\n").write(
    "spriteTypes = {\n" + "\n".join(fmt(l) for _, l in moved) + "\n" + body + "\n}\n")

for p in (MIN, IDEAS):
    t = read(p)
    n = re.findall(r'name\s*=\s*"([^"]+)"', t)
    print(p, "sprites", t.count("SpriteType"), "uniq", len(set(n)), "braces", t.count("{"), t.count("}"))
print("first two:", [b[0] for b in min_blocks][:2])
