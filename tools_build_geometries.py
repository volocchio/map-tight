import json
import math
import re
import urllib.request
from pathlib import Path

URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
TARGETS = {
    "Africa": lambda p: p.get("CONTINENT") == "Africa",
    "Asia": lambda p: p.get("CONTINENT") == "Asia" and p.get("ADMIN") not in {"Turkey","Cyprus","Northern Cyprus","Armenia","Azerbaijan","Georgia","Iran","Iraq","Israel","Jordan","Kuwait","Lebanon","Oman","Palestine","Qatar","Saudi Arabia","Syria","United Arab Emirates","Yemen"},
    "Europe": lambda p: p.get("CONTINENT") == "Europe" and p.get("ADMIN") != "Russia",
    "North America": lambda p: p.get("CONTINENT") == "North America" and p.get("ADMIN") != "Greenland",
    "South America": lambda p: p.get("CONTINENT") == "South America",
    "Oceania": lambda p: p.get("CONTINENT") == "Oceania",
    "Antarctica": lambda p: p.get("CONTINENT") == "Antarctica",
    "Eurasia": lambda p: p.get("CONTINENT") in {"Europe", "Asia"},
    "European Union": lambda p: p.get("ISO_A2_EH") in {
        "AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","GR","HU","IE","IT","LV","LT","LU","MT","NL","PL","PT","RO","SK","SI","ES","SE"
    },
    # Rough cultural/geographic regions — deliberately broad for visual comparison.
    "Middle East": lambda p: p.get("ADMIN") in {
        "Turkey","Syria","Lebanon","Israel","Palestine","Jordan","Iraq","Iran","Saudi Arabia","Yemen","Oman","United Arab Emirates","Qatar","Bahrain","Kuwait","Egypt"
    },
    "Caribbean": lambda p: p.get("SUBREGION") == "Caribbean",
}

# geographic bboxes for natural regions from land/country pieces, rough but non-cartoon
BBOX_TARGETS = {
    "Sahara Desert": (-18, 15, 35, 34),
    "Amazon Basin": (-80, -21, -44, 8),
    "Arctic": (-180, 60, 180, 90),
}

def rings_from_feature(feat):
    geom = feat["geometry"]
    coords = geom["coordinates"]
    if geom["type"] == "Polygon":
        return [coords[0]]
    if geom["type"] == "MultiPolygon":
        return [poly[0] for poly in coords]
    return []

def ring_bbox(ring):
    xs = [p[0] for p in ring]
    ys = [p[1] for p in ring]
    return min(xs), min(ys), max(xs), max(ys)

def ring_center(ring):
    xs = [p[0] for p in ring]
    ys = [p[1] for p in ring]
    return sum(xs) / len(xs), sum(ys) / len(ys)

def planar_area(points):
    return abs(sum(points[i][0]*points[(i+1)%len(points)][1] - points[(i+1)%len(points)][0]*points[i][1] for i in range(len(points))) / 2)

def simplify_ring(ring, max_points=80):
    # Keep enough points for recognizable outlines but avoid giant inline JS.
    if len(ring) <= max_points:
        return ring
    step = math.ceil(len(ring) / max_points)
    out = ring[::step]
    if out[-1] != ring[-1]:
        out.append(ring[-1])
    return out

def to_path(rings):
    if not rings:
        return "M10,10L90,10L90,90L10,90Z", 6400
    # Drop tiny rings relative to target bbox to prevent remote crumbs dominating.
    raw_areas = [planar_area(r) for r in rings]
    max_raw = max(raw_areas) if raw_areas else 1
    keep = [r for r,a in zip(rings, raw_areas) if a >= max_raw * 0.001]
    if not keep:
        keep = [rings[raw_areas.index(max_raw)]]
    allx = [x for r in keep for x,y in r]
    ally = [y for r in keep for x,y in r]
    minx,maxx,miny,maxy = min(allx),max(allx),min(ally),max(ally)
    pad = 6
    scale = min((100-2*pad)/(maxx-minx or 1), (100-2*pad)/(maxy-miny or 1))
    w=(maxx-minx)*scale
    h=(maxy-miny)*scale
    ox=(100-w)/2
    oy=(100-h)/2
    paths=[]
    area=0
    for ring in keep:
        pts=[]
        for lon,lat in simplify_ring(ring):
            x=ox+(lon-minx)*scale
            y=oy+(maxy-lat)*scale
            pts.append((x,y))
        area += planar_area(pts)
        cmd=[]
        for i,(x,y) in enumerate(pts):
            cmd.append(("M" if i==0 else "L") + f"{x:.1f},{y:.1f}")
        paths.append("".join(cmd)+"Z")
    return "".join(paths), round(area, 2)

def main():
    data = json.load(urllib.request.urlopen(URL, timeout=30))
    features = data["features"]
    out = {}
    for name, pred in TARGETS.items():
        rings=[]
        for feat in features:
            props = feat["properties"]
            if pred(props):
                rings.extend(rings_from_feature(feat))
        out[name] = to_path(rings)
    for name, (minlon, minlat, maxlon, maxlat) in BBOX_TARGETS.items():
        rings=[]
        for feat in features:
            for ring in rings_from_feature(feat):
                cx,cy=ring_center(ring)
                if minlon <= cx <= maxlon and minlat <= cy <= maxlat:
                    rings.append(ring)
        out[name] = to_path(rings)
    Path("generated_geometries.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    for k,(path,area) in out.items():
        print(k, area, path[:80])

if __name__ == "__main__":
    main()
