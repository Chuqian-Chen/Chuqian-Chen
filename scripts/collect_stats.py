"""Collect the numbers on the profile from the source repositories.

Run by .github/workflows/refresh-stats.yml, which clones the repos below
into ./src/<name> using a read-only token. Anything it cannot find keeps
the value already in stats.json, so a missing checkout never zeroes a stat.
"""
import glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = os.path.join(ROOT, "scripts", "stats.json")
st = json.load(open(SP))
src = lambda *p: os.path.join(ROOT, "src", *p)

def count(pattern, paths):
    n = 0
    for path in paths:
        for f in glob.glob(path, recursive=True):
            try: n += len(re.findall(pattern, open(f, encoding="utf-8", errors="ignore").read(), re.M))
            except OSError: pass
    return n

def put(key, value, label):
    if value: st[key]["value"], st[key]["label"] = value, label; print(f"{key}: {label}")
    else: print(f"{key}: not found, keeping {st[key]['label']}")

rnd = lambda n, step: f"{(n // step) * step:,}+"
put("ukb_agent_tests", count(r"^\s*def test_", [src("ukb", "tests", "**", "*.py")]), rnd(count(r"^\s*def test_", [src("ukb", "tests", "**", "*.py")]), 100))
put("ukb_agent_e2e", count(r"^\s*test\(", [src("ukb", "e2e", "**", "*.js"), src("ukb", "e2e", "**", "*.ts"), src("ukb", "tests", "e2e", "**", "*.py")]), rnd(count(r"^\s*test\(", [src("ukb", "e2e", "**", "*.js"), src("ukb", "e2e", "**", "*.ts")]), 10))
ci = count(r"\bCI-\d+\b", [src("ontology", "schema", "dictionary", "verify_docs.py")]); put("ontology_ci", len(set(re.findall(r"CI-\d+", open(src("ontology","schema","dictionary","verify_docs.py")).read()))) if os.path.exists(src("ontology","schema","dictionary","verify_docs.py")) else 0, None if not ci else str(ci))
put("hsct_suites", len(glob.glob(src("hsct", "tests", "test_*.py"))), f"{len(glob.glob(src('hsct','tests','test_*.py')))} suites")
put("women_tests", count(r"^\s*def test_", [src("women", "backend", "tests", "**", "*.py")]), str(count(r"^\s*def test_", [src("women", "backend", "tests", "**", "*.py")])))

am = src("ontology", "schema", "dictionary", "axis_measurements.json")
if os.path.exists(am):
    data = json.load(open(am))
    axes = data.get("axes", data) if isinstance(data, dict) else data
    rows = []
    for k, v in (axes.items() if isinstance(axes, dict) else ((a.get("name") or a.get("id"), a) for a in axes)):
        w = v.get("weight") if isinstance(v, dict) else None
        if isinstance(w, (int, float)): rows.append([k, round(float(w), 2)])
    rows.sort(key=lambda r: -r[1])
    if rows: st["axis_weights"]["value"] = rows[:10]; st["axis_weights"]["source"] = "auto: axis_measurements.json"; print("axis_weights:", rows[:10])
else: print("axis_measurements.json not found, keeping current weights")
json.dump(st, open(SP, "w"), indent=2, ensure_ascii=False)
