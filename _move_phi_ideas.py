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
    blocks, keep = [], []
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
    return txt, blocks, lines

def fmt(lines):
    out = []
    depth = 0
    body = lines[1:-1]
    for ln in body:
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

txt, blocks, lines = parse(MIN)
moved = [b for b in blocks if b[0] in MOVE]
rest = [b for b in blocks if b[0] not in MOVE]
assert len(moved) == 2, len(moved)
body = "\n".join(fmt(l) for _, l in rest)
io.open(MIN, "w", encoding="utf-8", newline="\n").write("spriteTypes = {\n" + body + "\n}\n")

ideas = read(IDEAS)
idx = ideas.rstrip().rfind("}")
head = ideas[:idx].rstrip("\n")
add = "\n".join(fmt(l) for _, l in moved)
io.open(IDEAS, "w", encoding="utf-8", newline="\n").write(head + "\n" + add + "\n}\n")

for p in (MIN, IDEAS):
    t = read(p)
    n = re.findall(r'name\s*=\s*"([^"]+)"', t)
    print(p, "sprites", t.count("SpriteType"), "uniq", len(set(n)), "braces", t.count("{"), t.count("}"))
