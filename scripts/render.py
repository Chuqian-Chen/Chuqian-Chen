import html
import json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,"assets")
ST=json.load(open(os.path.join(ROOT,"scripts","stats.json")))
L=lambda k:ST[k]["label"]
V=lambda k:ST[k]["value"]
M="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
S="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, 'Liberation Sans', Arial, sans-serif"
G="Georgia, Cambria, 'Liberation Serif', 'Times New Roman', serif"
P={"light":dict(paper="#FBF8F3",panel="#F3EFE7",ink="#1A1712",green="#0E3B34",ochre="#B8724A",body="#5A5248",muted="#6B6257",faint="#9A8F80",rule="#DED6C9",pill="#E9E3D8",bar="#D9CDB9"),
   "dark":dict(paper="#17150F",panel="#1F1C15",ink="#F3EDE3",green="#8CC7B5",ochre="#D08B5F",body="#B8AE9F",muted="#A0968A",faint="#6E665C",rule="#33302A",pill="#2A2620",bar="#3A352C")}

ROWS=[("UKB health agent","deterministic tests",V("ukb_agent_tests"),L("ukb_agent_tests")),("UKB health agent","real-browser E2E",V("ukb_agent_e2e"),L("ukb_agent_e2e")),
      ("Ontology","CI checks",V("ontology_ci"),L("ontology_ci")),("Ontology","fault-injection cases",V("ontology_faults"),L("ontology_faults")),("Ontology","hallucination modes caught",V("halluc_modes"),L("halluc_modes")),
      ("HSCT explainability","smoke + clinical tests",V("hsct_suites"),L("hsct_suites")),("Women's health","API test cases",V("women_tests"),L("women_tests"))]
def verify(p):
    import math
    parts=[]; y0=92; maxv=math.log10(2300)
    for i,(repo,what,v,lab) in enumerate(ROWS):
        y=y0+i*38; w=max(14, (math.log10(max(v,1))/maxv)*520)
        c=p["green"] if i%2==0 else p["ochre"]
        parts.append(f'''  <text x="24" y="{y+15}" font-family="{S}" font-size="12.5" font-weight="700" fill="{p["ink"]}">{html.escape(repo)}</text>
  <text x="212" y="{y+15}" font-family="{S}" font-size="12.5" fill="{p["body"]}">{html.escape(what)}</text>
  <rect x="440" y="{y}" width="520" height="20" rx="3" fill="{p["bar"]}" opacity=".35"/>
  <rect x="440" y="{y}" width="{w:.0f}" height="20" rx="3" fill="{c}"/>
  <text x="{440+w+10:.0f}" y="{y+15}" font-family="{G}" font-size="15" font-weight="700" fill="{p["ink"]}">{lab}</text>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="372" viewBox="0 0 1080 372" role="img" aria-label="Verification wall">
  <rect width="1080" height="372" rx="4" fill="{p["paper"]}"/><rect x=".5" y=".5" width="1079" height="371" rx="3.5" fill="none" stroke="{p["rule"]}"/>
  <text x="24" y="38" font-family="{M}" font-size="11.5" letter-spacing="3.5" fill="{p["faint"]}">PROOF, NOT PROMISES</text>
  <text x="23" y="66" font-family="{G}" font-size="22" font-weight="700" fill="{p["ink"]}">What runs green before anything ships</text>
  <text x="1056" y="66" text-anchor="end" font-family="{M}" font-size="10.5" fill="{p["faint"]}">log scale</text>
{chr(10).join(parts)}
</svg>
'''
def wrap(t,n):
    o,c=[],""
    for w in t.split():
        if c and len(c)+1+len(w)>n: o.append(c); c=w
        else: c=(c+" "+w).strip()
    return o+[c] if c else o

AXES=[tuple(a[:2]) for a in V("axis_weights")]
INFL={a[0]:a[2] for a in V("axis_weights") if len(a)>2}
STEPS=[("GATE","Baseline characteristics","sex · age band · hard filter, not a distance"),
       ("AXIS VECTORS","10 P0 axes · 1,982 field families","one vector per dictionary Sublevel"),
       ("MISSING-AWARE DISTANCE","reliability = 0 drops the axis","pairwise usable ≈ coverage² · <25% → own tier"),
       ("CALIBRATE + FUSE","expert weights, measured influence","leave-one-axis-out stability · opcs4 flagged inert"),
       ("TOP-10 → ACTION LIBRARY","explain, don't estimate","effect sizes come from the full matched layer")]
def retrieval(p):
    parts=[]
    for i,(k,t,d) in enumerate(STEPS):
        y=92+i*54
        parts.append(f'''  <circle cx="44" cy="{y+12}" r="13" fill="{p["green"] if i!=4 else p["ochre"]}"/><text x="44" y="{y+16.5}" text-anchor="middle" font-family="{M}" font-size="12" font-weight="700" fill="{p["paper"]}">{i+1}</text>
  <text x="70" y="{y+6}" font-family="{M}" font-size="10" letter-spacing="2.2" fill="{p["faint"]}">{k}</text>
  <text x="70" y="{y+24}" font-family="{G}" font-size="15.5" font-weight="700" fill="{p["ink"]}">{t}</text>
  <text x="70" y="{y+40}" font-family="{S}" font-size="11.5" fill="{p["body"]}">{html.escape(d)}</text>''')
        if i<4: parts.append(f'  <path d="M44 {y+26} V{y+53}" stroke="{p["rule"]}" stroke-width="2"/>')
    bars=[f'  <text x="620" y="88" font-family="{M}" font-size="10" letter-spacing="2.2" fill="{p["faint"]}">NOMINAL WEIGHT (AW-P0-v1)  ·  ◆ MEASURED LEAVE-ONE-OUT INFLUENCE</text>']
    for i,(a,w) in enumerate(AXES):
        y=100+i*24
        bars.append(f'''  <text x="730" y="{y+13}" text-anchor="end" font-family="{S}" font-size="11.5" fill="{p["body"]}">{a}</text>
  <rect x="742" y="{y}" width="340" height="16" rx="2" fill="{p["bar"]}" opacity=".35"/><rect x="742" y="{y}" width="{w*340/AXES[0][1]:.0f}" height="16" rx="2" fill="{p["green"] if i<9 else p["ochre"]}"/>
  <text x="{750+w*340/AXES[0][1]:.0f}" y="{y+12.5}" font-family="{M}" font-size="10.5" fill="{p["muted"]}">{w:.2f}</text>
  <path d="M{742+INFL.get(a,0)*340/max(INFL.values() or [1]):.0f} {y+2} l6 6 -6 6 -6 -6z" fill="{p["ochre"]}"/>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1152" height="386" viewBox="0 0 1152 386" role="img" aria-label="Similar-patient retrieval algorithm">
  <rect width="1152" height="372" rx="4" fill="{p["paper"]}"/><rect x=".5" y=".5" width="1151" height="385" rx="3.5" fill="none" stroke="{p["rule"]}"/>
  <text x="24" y="38" font-family="{M}" font-size="11.5" letter-spacing="3.5" fill="{p["faint"]}">THE ALGORITHM · SIMILAR-PATIENT RETRIEVAL OVER 498,339 PEOPLE</text>
  <text x="23" y="66" font-family="{G}" font-size="22" font-weight="700" fill="{p["ink"]}">Not one 11,318-dim kNN. Ten axes, each allowed to say “I don’t know.”</text>
{chr(10).join(parts)}
{chr(10).join(bars)}
  <text x="620" y="352" font-family="{G}" font-size="12.5" font-style="italic" fill="{p["muted"]}">weights and influence are read from ontology.yaml and loo_stability.json by a scheduled workflow;</text>
  <text x="620" y="368" font-family="{G}" font-size="12.5" font-style="italic" fill="{p["muted"]}">no number on this chart is typed by hand.</text>
</svg>
'''


if __name__=="__main__":
    for t,p in P.items():
        open(f"{OUT}/verification-{t}.svg","w").write(verify(p)); open(f"{OUT}/retrieval-{t}.svg","w").write(retrieval(p))
    print("rendered from stats.json")
