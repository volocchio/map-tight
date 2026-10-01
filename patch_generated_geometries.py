import json
import re
from pathlib import Path

p = Path('index.html')
s = p.read_text()
g = json.loads(Path('generated_geometries.json').read_text())

for name, (path, area) in g.items():
    # Replace path if existing in shapePaths override block or original shapePaths.
    pattern = r'"' + re.escape(name) + r'":"[^"]+"'
    repl = '"' + name + '":"' + path + '"'
    matches = list(re.finditer(pattern, s))
    if matches:
        # Prefer last occurrence because override block wins.
        m = matches[-1]
        s = s[:m.start()] + repl + s[m.end():]
    else:
        # Add into Object.assign(shapePaths,{...}) override block.
        marker = 'Object.assign(shapePaths,{'
        pos = s.find(marker)
        if pos < 0:
            raise SystemExit('shapePaths override block not found')
        insert_pos = pos + len(marker)
        s = s[:insert_pos] + repl + ',' + s[insert_pos:]

    # Replace/add shapeAreas value in override Object.assign(shapeAreas,{...}) block first.
    area_pat = r'"' + re.escape(name) + r'":([0-9.]+)'
    area_repl = '"' + name + '":' + str(area)
    matches = list(re.finditer(area_pat, s))
    if matches:
        # Replace last, override if present; if only original, still okay.
        m = matches[-1]
        s = s[:m.start()] + area_repl + s[m.end():]
    else:
        marker = 'Object.assign(shapeAreas,{'
        pos = s.find(marker)
        if pos < 0:
            raise SystemExit('shapeAreas override block not found')
        insert_pos = pos + len(marker)
        s = s[:insert_pos] + area_repl + ',' + s[insert_pos:]

s = s.replace('v2026-09-19n · Natural Earth France geometry', 'v2026-09-19o · Real continent geometries')
p.write_text(s)
print('patched', len(g), 'geometries')
