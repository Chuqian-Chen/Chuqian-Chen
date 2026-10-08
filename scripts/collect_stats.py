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

oy = src("ontology", "schema", "ontology.yaml"); lo = src("ontology", "schema", "dictionary", "loo_stability.json"); rv = src("ontology", "schema", "dictionary", "retrieval_eval.json")
NAME = {"clinical_lab":"ClinicalLab","anthropometry":"Anthropometry","nmr_metabolomics":"NMR metab.","blood_pressure":"Blood pressure","diet":"Diet","hand_grip_strength":"Hand grip","sleep":"Sleep","icd10_burden":"ICD-10","sun_exposure":"Sun exposure","opcs4_burden":"OPCS-4"}
if os.path.exists(oy) and os.path.exists(lo):
    y = open(oy, encoding="utf-8").read(); blk = y[y.index("axis_weight_policy:"):]; blk = blk[:blk.index("note:")]
    w = {k: float(v) for k, v in re.findall(r"^\s{4}([a-z0-9_]+):\s+([0-9.]+)\s*$", blk, re.M)}
    loo = {k: v for k, v in json.load(open(lo)).items() if not k.startswith("_")}
    rows = [[NAME.get(k, k), round(v, 4), round(1 - loo[k]["after"], 3) if k in loo else 0] for k, v in sorted(w.items(), key=lambda kv: -kv[1])]
    if rows: st["axis_weights"]["value"] = rows; print("axis_weights:", rows)
else: print("ontology.yaml / loo_stability.json not found, keeping current weights")
if os.path.exists(rv):
    ev = json.load(open(rv)); st["retrieval_eval"]["value"] = {k: {"prevalence": ev[k]["prevalence"], "point": ev[k]["bootstrap"]["point_on_paired_subset"], "ci95": ev[k]["bootstrap"]["ci95"], "lift": ev[k]["concordance_separation"]["lift_vs_prevalence"]} for k in ("t2dm", "circulatory") if k in ev}; print("retrieval_eval refreshed")
json.dump(st, open(SP, "w"), indent=2, ensure_ascii=False)
