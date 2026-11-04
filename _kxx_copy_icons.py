# -*- coding: utf-8 -*-
import io, re, os, collections

ROOT = "."
REFS = "refs_check.tsv"
GOALS = "interface/KXX_goals.gfx"
GOALS_SHINE = "interface/KXX_goals_shine.gfx"
IDEAS = "interface/KXX_ideas.gfx"
EVENTS = "interface/KXX_event_pictures.gfx"

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

def write(p, txt, bom=False, crlf=False):
    if crlf:
        txt = txt.replace("\n", "\r\n")
    data = txt.encode("utf-8")
    if bom:
        data = b"\xef\xbb\xbf" + data
    open(p, "wb").write(data)

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
            inner = lines[i + 1:j]
            blk = "\n".join(lines[i:j + 1])
            nm = re.search(r'name\s*=\s*"([^"]+)"', blk)
            tex = re.search(r'(?i)texturefile\s*=\s*"([^"]+)"', blk)
            res.append({"name": nm.group(1) if nm else "", "tex": tex.group(1) if tex else "",
                        "inner": inner, "code": blk, "file": path})
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

def make_shine(block):
    name = block["name"] + "_shine"
    tex = block["tex"]
    inner = [
        'name = "%s"' % name,
        'texturefile = "%s"' % tex,
        'effectFile = "gfx/FX/buttonstate.lua"',
        'animation = {',
        'animationmaskfile = "%s"' % tex,
        'animationtexturefile = "gfx/interface/goals/shine_overlay.dds"',
        'animationrotation = -90.0',
        'animationlooping = no',
        'animationtime = 0.75',
        'animationdelay = 0',
        'animationblendmode = "add"',
        'animationtype = "scrolling"',
        'animationrotationoffset = { x = 0.0 y = 0.0 }',
        'animationtexturescale = { x = 1.0 y = 1.0 }',
        '}',
        'animation = {',
        'animationmaskfile = "%s"' % tex,
        'animationtexturefile = "gfx/interface/goals/shine_overlay.dds"',
        'animationrotation = 90.0',
        'animationlooping = no',
        'animationtime = 0.75',
        'animationdelay = 0',
        'animationblendmode = "add"',
        'animationtype = "scrolling"',
        'animationrotationoffset = { x = 0.0 y = 0.0 }',
        'animationtexturescale = { x = 1.0 y = 1.0 }',
        '}',
        'legacy_lazy_load = no',
    ]
    return {"name": name, "tex": tex, "inner": inner, "code": "", "file": ""}

def existing_names(path):
    if not os.path.exists(path):
        return set()
    txt, _, _ = read(path)
    return set(re.findall(r'name\s*=\s*"([^"]+)"', txt))

def append_to(path, blocks):
    txt, bom, crlf = read(path) if os.path.exists(path) else ("", False, False)
    if txt.strip() == "":
        txt = "spriteTypes = {\n}\n"
        bom, crlf = False, False
    idx = txt.rstrip().rfind("}")
    head = txt[:idx].rstrip("\n")
    tail = txt[idx:]
    body = "\n".join(fmt(b) for b in blocks)
    new = head + "\n" + body + "\n" + tail
    write(path, new, bom, crlf)

allblocks = {}
by_name = collections.defaultdict(list)
for f, names in kept.items():
    for b in parse_blocks(f):
        allblocks[(f, b["name"])] = b
        by_name[b["name"]].append(b)

goals_base, goals_shine, ideas, events, other = [], [], [], [], []
missing, gen = [], 0
for f, names in sorted(kept.items()):
    for name in sorted(names):
        b = allblocks.get((f, name))
        if not b:
            missing.append((f, name))
            continue
        tex = b["tex"].replace("\\", "/").lower()
        if tex.startswith("gfx/interface/goals/"):
            goals_base.append(b)
            twin = allblocks.get((f, name + "_shine"))
            if not twin:
                for cand in by_name.get(name + "_shine", []):
                    if cand["tex"].replace("\\", "/").lower() == tex:
                        twin = cand
                        break
            if twin:
                goals_shine.append(twin)
            else:
                goals_shine.append(make_shine(b))
                gen += 1
        elif tex.startswith("gfx/interface/ideas/"):
            ideas.append(b)
        elif tex.startswith("gfx/event_pictures/"):
            events.append(b)
        else:
            other.append(b)

def dedupe(blocks, target):
    have = existing_names(target)
    out, dup = [], 0
    for b in blocks:
        if b["name"] in have:
            dup += 1
            continue
        have.add(b["name"])
        out.append(b)
    return out, dup

g_new, g_dup = dedupe(goals_base, GOALS)
s_new, s_dup = dedupe(goals_shine, GOALS_SHINE)
i_new, i_dup = dedupe(ideas, IDEAS)
e_new, e_dup = dedupe(events, EVENTS)

append_to(GOALS, g_new)
append_to(GOALS_SHINE, s_new)
append_to(IDEAS, i_new)
append_to(EVENTS, e_new)

print("kept blocks:", sum(len(v) for v in kept.values()))
print("missing parsed:", len(missing), missing[:5])
print("categories: goals %d, ideas %d, event_pictures %d, other %d" % (len(goals_base), len(ideas), len(events), len(other)))
print("goals added %d (dup %d), shine added %d (dup %d, generated %d)" % (len(g_new), g_dup, len(s_new), s_dup, gen))
print("ideas added %d (dup %d), events added %d (dup %d)" % (len(i_new), i_dup, len(e_new), e_dup))
oc = collections.Counter()
for b in other:
    t = b["tex"].replace("\\", "/").lower()
    if t.startswith("gfx/interface/ideologies/"): oc["ideologies"] += 1
    elif t.startswith("gfx/leaders/"): oc["leaders"] += 1
    elif t.startswith("gfx/interface/decisions/"): oc["decisions"] += 1
    elif t.startswith("gfx/flags/"): oc["flags"] += 1
    else: oc["interface_other"] += 1
print("other:", dict(oc))
