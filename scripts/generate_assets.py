#!/usr/bin/env python3
"""Generates the self-hosted SVG assets for the profile README.

Run from anywhere: `python3 scripts/generate_assets.py`. Output goes to images/.
Edit the data (terminal script, impact numbers, PROJECTS, STACK) and re-run.
"""
import html
import math
import os
import random
import re

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Helvetica Neue',Inter,Arial,sans-serif"
MONO = "'SF Mono','JetBrains Mono','Fira Code',Menlo,Consolas,'DejaVu Sans Mono','Liberation Mono',monospace"

BASE_CSS = """
.sans{font-family:SANS}
.mono{font-family:MONO}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@keyframes pulse{from{opacity:.5}to{opacity:1}}
@keyframes blink{50%{opacity:.2}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
""".replace("SANS", SANS).replace("MONO", MONO)


def esc(s):
    return html.escape(s, quote=True)


# Dark palette -> GitHub light palette. Every asset except the buttons also gets a
# "-light.svg" twin; the README picks one per viewer via <picture> + prefers-color-scheme.
LIGHT = {
    # surfaces and borders
    "#0B0E14": "#FFFFFF", "#0D1117": "#FFFFFF", "#161B22": "#F6F8FA", "#21262D": "#EAEEF2",
    "#30363D": "#D0D7DE", "#484F58": "#8C959F",
    # text
    "#E6EDF3": "#1F2328", "#C9D1D9": "#424A53", "#8B949E": "#59636E", "#6E7681": "#6E7781",
    # accents, darkened for contrast on white
    "#A78BFA": "#7C3AED", "#C4B5FD": "#6D28D9", "#E9D5FF": "#8B5CF6", "#60A5FA": "#2563EB",
    "#22D3EE": "#0891B2", "#79C0FF": "#0969DA", "#A5D6FF": "#0A3069", "#D2A8FF": "#8250DF",
    "#FF7B72": "#CF222E", "#3FB950": "#1A7F37",
    # badge and chip fills
    "#0F2A1A": "#DAFBE1", "#1E1433": "#F3E8FF", "#0C1D33": "#DDF4FF",
}


def to_light(body):
    body = re.sub(r"#[0-9A-Fa-f]{6}\b", lambda m: LIGHT.get(m.group().upper(), m.group()), body)
    return body.replace('flood-opacity=".55"', 'flood-opacity=".12"')


def write(rel, body):
    variants = [(rel, body)]
    if not rel.startswith("buttons/"):
        variants.append((rel.replace(".svg", "-light.svg"), to_light(body)))
    for name, content in variants:
        path = os.path.join(OUT, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"wrote {name} ({len(content.encode()) / 1024:.1f} KB)")


def svg_open(w, h, label, css=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'fill="none" role="img" aria-label="{esc(label)}">\n'
        f"<title>{esc(label)}</title>\n<style>{BASE_CSS}{css}</style>\n"
    )


# --------------------------------------------------------------------------- hero
def hero():
    W, H = 1200, 420
    css = """
.glow{animation:pulse 7s ease-in-out infinite alternate}
.glow.g2{animation-delay:-3.5s}
.bar{transform-box:fill-box;transform-origin:center;animation:eq 1.1s ease-in-out infinite alternate}
@keyframes eq{from{transform:scaleY(.18)}to{transform:scaleY(1)}}
.r{animation:rise .9s cubic-bezier(.2,.7,.2,1) both}
.live{animation:blink 1.6s ease-in-out infinite}
.p{fill:#A78BFA}.c{fill:#E6EDF3}.o{fill:#8B949E}.h{fill:#C4B5FD}.ok{fill:#3FB950}.dim{fill:#484F58}.bl{fill:#79C0FF}
"""
    s = [svg_open(W, H, "Pavan Kumar — AI Engineer building AI agents, real-time voice AI and automation", css)]
    s.append("""<defs>
  <clipPath id="card"><rect width="1200" height="420" rx="24"/></clipPath>
  <linearGradient id="border" x1="0" y1="0" x2="1200" y2="420" gradientUnits="userSpaceOnUse">
    <stop stop-color="#7C3AED"/><stop offset=".5" stop-color="#30363D"/><stop offset="1" stop-color="#22D3EE"/>
  </linearGradient>
  <linearGradient id="name" x1="60" y1="0" x2="560" y2="0" gradientUnits="userSpaceOnUse" spreadMethod="reflect">
    <stop stop-color="#C4B5FD"/><stop offset=".35" stop-color="#A78BFA"/><stop offset=".7" stop-color="#60A5FA"/><stop offset="1" stop-color="#22D3EE"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="1000 0" dur="9s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="wave" x1="64" y1="0" x2="370" y2="0" gradientUnits="userSpaceOnUse">
    <stop stop-color="#A78BFA"/><stop offset="1" stop-color="#22D3EE"/>
  </linearGradient>
  <radialGradient id="gv"><stop stop-color="#7C3AED" stop-opacity=".55"/><stop offset="1" stop-color="#7C3AED" stop-opacity="0"/></radialGradient>
  <radialGradient id="gc"><stop stop-color="#0EA5E9" stop-opacity=".35"/><stop offset="1" stop-color="#0EA5E9" stop-opacity="0"/></radialGradient>
  <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#30363D"/></pattern>
  <radialGradient id="fade" cx=".35" cy=".4" r=".8"><stop stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
  <mask id="gridmask"><rect width="1200" height="420" fill="url(#fade)"/></mask>
  <clipPath id="term"><rect x="660" y="52" width="480" height="316" rx="14"/></clipPath>
  <filter id="shadow" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#000" flood-opacity=".55"/></filter>
</defs>
""")
    # background
    s.append('<g clip-path="url(#card)">\n<rect width="1200" height="420" fill="#0B0E14"/>\n')
    s.append('<rect width="1200" height="420" fill="url(#dots)" mask="url(#gridmask)"/>\n')
    s.append('<circle class="glow" cx="140" cy="40" r="420" fill="url(#gv)"/>\n')
    s.append('<circle class="glow g2" cx="1120" cy="430" r="400" fill="url(#gc)"/>\n</g>\n')
    s.append('<rect x=".75" y=".75" width="1198.5" height="418.5" rx="23.25" stroke="url(#border)" stroke-width="1.5"/>\n')

    # left column
    s.append(f'<text class="mono r" x="64" y="110" font-size="15" fill="#6E7681" letter-spacing="1">// hello world, i\'m</text>\n')
    s.append('<text class="sans r" x="60" y="186" font-size="72" font-weight="800" letter-spacing="-1.5" '
             'fill="url(#name)" style="animation-delay:.1s">Pavan Kumar</text>\n')
    s.append('<text class="sans r" x="64" y="236" font-size="21" fill="#8B949E" style="animation-delay:.2s">'
             'I build <tspan fill="#E6EDF3" font-weight="600">AI agents</tspan>, '
             '<tspan fill="#E6EDF3" font-weight="600">real-time voice AI</tspan> and</text>\n')
    s.append('<text class="sans r" x="64" y="266" font-size="21" fill="#8B949E" style="animation-delay:.25s">'
             '<tspan fill="#E6EDF3" font-weight="600">automation</tspan> that runs real operations.</text>\n')

    # chips
    x = 64
    s.append('<g class="r" style="animation-delay:.35s">\n')
    for i, label in enumerate(["AI agents", "voice AI", "RAG", "FastAPI", "automation"]):
        w = len(label) * 7.8 + 26
        stroke = "#7C3AED" if i == 0 else "#30363D"
        fill = "#1E1433" if i == 0 else "#161B22"
        color = "#C4B5FD" if i == 0 else "#C9D1D9"
        s.append(f'<rect x="{x:.1f}" y="296" width="{w:.1f}" height="30" rx="15" fill="{fill}" stroke="{stroke}"/>'
                 f'<text class="mono" x="{x + w / 2:.1f}" y="316" font-size="13" fill="{color}" text-anchor="middle">{label}</text>\n')
        x += w + 10
    s.append("</g>\n")

    # voice waveform
    random.seed(11)
    n, cy = 34, 374
    s.append('<g class="r" style="animation-delay:.45s">\n')
    for i in range(n):
        env = 0.3 + 0.7 * math.sin(math.pi * (i + 0.5) / n) ** 1.3
        h = max(6.0, 32 * env * random.uniform(0.5, 1.0))
        dur = random.uniform(0.55, 1.35)
        delay = -random.uniform(0, 1.3)
        s.append(f'<rect class="bar" x="{64 + i * 9}" y="{cy - h / 2:.1f}" width="4" height="{h:.1f}" rx="2" '
                 f'fill="url(#wave)" style="animation-duration:{dur:.2f}s;animation-delay:{delay:.2f}s"/>\n')
    s.append('<circle class="live" cx="392" cy="370" r="4" fill="#3FB950"/>')
    s.append('<text class="mono" x="404" y="374" font-size="13" fill="#6E7681">stt → llm → tts</text>\n</g>\n')

    # terminal window
    tx, ty, tw, th = 660, 52, 480, 316
    s.append(f'<g class="r" style="animation-delay:.15s">\n<g filter="url(#shadow)"><rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="14" fill="#0D1117"/></g>\n')
    s.append(f'<g clip-path="url(#term)"><rect x="{tx}" y="{ty}" width="{tw}" height="38" fill="#161B22"/>'
             f'<rect x="{tx}" y="{ty + 38}" width="{tw}" height="1" fill="#21262D"/></g>\n')
    s.append(f'<rect x="{tx + .5}" y="{ty + .5}" width="{tw - 1}" height="{th - 1}" rx="13.5" stroke="#30363D"/>\n')
    for k, c in enumerate(["#FF5F56", "#FFBD2E", "#27C93F"]):
        s.append(f'<circle cx="{tx + 22 + k * 20}" cy="{ty + 19}" r="6" fill="{c}"/>')
    s.append(f'\n<text class="mono" x="{tx + tw / 2}" y="{ty + 24}" font-size="12.5" fill="#8B949E" text-anchor="middle">pavan@ai-lab: ~/prod</text>\n')

    # terminal script: (text, css class, reveal time in s)
    t = 0.6
    script = []

    def cmd(text):
        nonlocal t
        segs = [("$ ", "p", t)]
        t += 0.25
        for ch in text:
            segs.append((ch, "c", t))
            t += 0.065
        t += 0.3
        script.append(segs)

    def out(*segs, gap=0.0):
        nonlocal t
        line = []
        for text, cls, dt in segs:
            t += dt
            line.append((text, cls, t))
        script.append(line)
        t += 0.35 + gap

    cmd("whoami")
    out(("pavan kumar", "c", 0), (" — ", "dim", 0), ("ai engineer", "h", 0))
    cmd("cat focus.txt")
    out(("→ ", "p", 0), ("agents that run real operations, not demos", "o", 0))
    cmd("llm --failover")
    out(("groq", "bl", 0), (" ─▶ ", "dim", .22), ("gemini", "bl", 0), (" ─▶ ", "dim", .22),
        ("gpt-4o-mini", "bl", 0), (" ─▶ ", "dim", .22), ("offline", "bl", 0), ("  ✓", "ok", .25))
    cmd("deploy --env production")
    out(("✓ ", "ok", 0), ("tests", "o", 0), ("   ✓ ", "ok", .3), ("build", "o", 0),
        ("   ✓ ", "ok", .3), ("shipped", "c", 0))
    final_t = t

    y = ty + 38 + 34
    for line in script:
        spans = "".join(
            f'<tspan class="{cls}"><set attributeName="fill-opacity" to="0" dur="{rt:.2f}s"/>{esc(text)}</tspan>'
            for text, cls, rt in line
        )
        s.append(f'<text class="mono" x="{tx + 24}" y="{y}" font-size="16" xml:space="preserve">{spans}</text>\n')
        y += 27
    s.append(
        f'<text class="mono" x="{tx + 24}" y="{y}" font-size="16" xml:space="preserve">'
        f'<tspan class="p"><set attributeName="fill-opacity" to="0" dur="{final_t:.2f}s"/>$ </tspan>'
        f'<tspan class="p"><set attributeName="fill-opacity" to="0" dur="{final_t:.2f}s"/>'
        f'<animate attributeName="fill-opacity" values="1;0" calcMode="discrete" dur="1.1s" begin="{final_t:.2f}s" repeatCount="indefinite"/>▋</tspan>'
        f"</text>\n</g>\n"
    )
    s.append("</svg>\n")
    write("hero.svg", "".join(s))


# --------------------------------------------------------------------------- impact strip
def impact():
    W, H = 1000, 176
    cards = [
        ("E-INVOICING", "2,000+", "documents / month", "multi-tenant · LHDN", "📄"),
        ("DATA ENGINEERING", "100K+", "records processed", "python → sql pipelines", "🗄️"),
        ("SHIPPED", "6", "AI & ML systems built", "agents · voice · RAG · ML", "🤖"),
        ("RELIABILITY", "4", "LLM fallback layers", "groq→gemini→gpt→offline", "🛡️"),
    ]
    css = ".card{animation:rise .8s cubic-bezier(.2,.7,.2,1) both}"
    label = "Impact: " + "; ".join(f"{n} {l}" for _, n, l, _, _ in cards)
    s = [svg_open(W, H, label, css)]
    s.append("""<defs>
  <linearGradient id="num" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#E9D5FF"/><stop offset=".5" stop-color="#A78BFA"/><stop offset="1" stop-color="#60A5FA"/></linearGradient>
  <linearGradient id="top" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#22D3EE"/></linearGradient>
</defs>
""")
    cw, gap = 235, 20
    for i, (cap, num, lab, det, icon) in enumerate(cards):
        x = i * (cw + gap)
        s.append(f'<g class="card" style="animation-delay:{i * .12:.2f}s">\n')
        s.append(f'<clipPath id="c{i}"><rect x="{x + 1}" y="1" width="{cw - 2}" height="{H - 2}" rx="16"/></clipPath>\n')
        s.append(f'<rect x="{x + 1}" y="1" width="{cw - 2}" height="{H - 2}" rx="16" fill="#0D1117" stroke="#30363D"/>\n')
        s.append(f'<rect x="{x}" y="0" width="{cw}" height="3" fill="url(#top)" clip-path="url(#c{i})"/>\n')
        s.append(f'<text class="mono" x="{x + 24}" y="38" font-size="11" letter-spacing="1.5" fill="#8B949E">{cap}</text>\n')
        s.append(f'<text x="{x + cw - 22}" y="42" font-size="22" fill="#fff" text-anchor="end">{icon}</text>\n')
        s.append(f'<text class="sans" x="{x + 22}" y="96" font-size="46" font-weight="800" letter-spacing="-1" fill="url(#num)">{esc(num)}</text>\n')
        s.append(f'<text class="sans" x="{x + 24}" y="126" font-size="14.5" fill="#C9D1D9">{esc(lab)}</text>\n')
        s.append(f'<text class="mono" x="{x + 24}" y="150" font-size="12" fill="#6E7681">{esc(det)}</text>\n</g>\n')
    s.append("</svg>\n")
    write("impact.svg", "".join(s))


# --------------------------------------------------------------------------- project cards
BADGES = {
    "public": ("PUBLIC REPO ↗", "#0F2A1A", "#238636", "#3FB950"),
    "portfolio": ("PORTFOLIO ↗", "#0C1D33", "#1F6FEB", "#79C0FF"),
    "private": ("ENTERPRISE", "#1E1433", "#6E40C9", "#C4B5FD"),
}


def project(slug, icon, title, sub, badge, accent, desc, chips, stack):
    W, H = 480, 224
    css = ".r{animation:rise .8s cubic-bezier(.2,.7,.2,1) both}"
    s = [svg_open(W, H, f"{title} — {sub}. {' '.join(desc)} Stack: {stack}", css)]
    a1, a2 = accent
    s.append(f"""<defs>
  <linearGradient id="acc" x1="0" y1="0" x2="1" y2="0"><stop stop-color="{a1}"/><stop offset="1" stop-color="{a2}"/></linearGradient>
  <radialGradient id="tint" cx="0" cy="0" r="1"><stop stop-color="{a1}" stop-opacity=".16"/><stop offset="1" stop-color="{a1}" stop-opacity="0"/></radialGradient>
  <clipPath id="cl"><rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16"/></clipPath>
</defs>
<g class="r">
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="#0D1117"/>
<g clip-path="url(#cl)"><circle cx="0" cy="0" r="260" fill="url(#tint)"/><rect width="{W}" height="3" fill="url(#acc)"/></g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" stroke="#30363D"/>
<rect x="24" y="24" width="44" height="44" rx="12" fill="#161B22" stroke="url(#acc)"/>
<text x="46" y="54" font-size="22" fill="#fff" text-anchor="middle">{icon}</text>
<text class="sans" x="82" y="44" font-size="20" font-weight="700" fill="#E6EDF3">{esc(title)}</text>
<text class="mono" x="82" y="64" font-size="12" fill="#8B949E">{esc(sub)}</text>
""")
    btxt, bfill, bstroke, bcol = BADGES[badge]
    bw = len(btxt) * 7.1 + 20
    s.append(f'<rect x="{W - 24 - bw:.1f}" y="26" width="{bw:.1f}" height="22" rx="11" fill="{bfill}" stroke="{bstroke}"/>'
             f'<text class="mono" x="{W - 24 - bw / 2:.1f}" y="41" font-size="10.5" letter-spacing=".8" fill="{bcol}" text-anchor="middle">{esc(btxt)}</text>\n')
    for k, line in enumerate(desc):
        s.append(f'<text class="sans" x="24" y="{100 + k * 22}" font-size="15" fill="#C9D1D9">{esc(line)}</text>\n')
    x = 24
    for k, chip in enumerate(chips):
        w = len(chip) * 6.6 + 20
        stroke = "url(#acc)" if k == 0 else "#30363D"
        col = "#E6EDF3" if k == 0 else "#8B949E"
        s.append(f'<rect x="{x:.1f}" y="160" width="{w:.1f}" height="22" rx="11" fill="#161B22" stroke="{stroke}"/>'
                 f'<text class="mono" x="{x + w / 2:.1f}" y="175" font-size="11" fill="{col}" text-anchor="middle">{esc(chip)}</text>\n')
        x += w + 8
    s.append(f'<rect x="24" y="192" width="{W - 48}" height="1" fill="#21262D"/>\n')
    s.append(f'<text class="mono" x="24" y="211" font-size="11.5" fill="#6E7681">{esc(stack)}</text>\n</g>\n</svg>\n')
    write(f"projects/{slug}.svg", "".join(s))


PROJECTS = [
    ("discord-insights", "💬", "Discord Insights", "conversational analytics agent", "public", ("#5865F2", "#A78BFA"),
     ["Ask your data questions in plain English. An agent",
      "writes the SQL, checks it as an AST, runs it read-only",
      "and streams answers and charts back live over SSE."],
     ["sqlglot AST guard", "4-tier LLM failover", "plugin system"],
     "python · fastapi · postgresql · react · docker"),
    ("aria", "🎙️", "Aria", "real-time voice AI assistant", "portfolio", ("#A78BFA", "#22D3EE"),
     ["Low-latency voice assistant that listens, thinks and",
      "talks back over WebRTC — with interruption handling,",
      "so people can cut in mid-sentence like a real call."],
     ["WebRTC streaming", "interruption handling", "domain STT"],
     "python · pipecat · webrtc · groq llama · whisper"),
    ("e-invoice", "📄", "e-Invoice Pipeline", "multi-tenant ETL · compliance", "private", ("#60A5FA", "#34D399"),
     ["Pulls invoice data out of PDFs and spreadsheets, maps",
      "it to JSON schema and files Malaysian LHDN e-Invoices",
      "across tenants — 2,000+ documents every month."],
     ["PDF + Excel extraction", "multi-tenant", "LHDN compliant"],
     "python · microsoft graph · rest apis · oauth 2.0"),
    ("sales-agent", "🤖", "AI Sales Agent", "lead gen & sales automation", "private", ("#F472B6", "#A78BFA"),
     ["Ingests inbound email, researches the company,",
      "drafts a personalised reply and syncs the CRM —",
      "the top of the sales funnel, automated end to end."],
     ["email ingestion", "company research", "CRM sync"],
     "python · groq llama · microsoft graph · postgresql"),
    ("alfred", "🎩", "Alfred", "AI portfolio assistant", "public", ("#FBBF24", "#F472B6"),
     ["A chat assistant that answers questions about my",
      "experience and projects, grounded in a résumé",
      "knowledge base with short-term memory + summaries."],
     ["résumé-grounded", "context summaries", "llama 3.1"],
     "python · streamlit · groq"),
    ("churn-ml", "🔎", "E-commerce Churn ML", "customer churn prediction", "public", ("#34D399", "#60A5FA"),
     ["Predicts which e-commerce customers are about to",
      "leave, using an XGBoost model tuned end to end",
      "with cross-validated grid search."],
     ["XGBoost", "GridSearchCV", "ML pipeline"],
     "python · xgboost · scikit-learn"),
]


# --------------------------------------------------------------------------- stack map
STACK = [
    ("🧠", "AI & LLMs", [("Groq LLaMA", "#F55036"), ("Whisper", "#10A37F"), ("Pipecat", "#A78BFA"),
                         ("Gemini", "#8E75B2"), ("GPT-4o-mini", "#10A37F"), ("RAG", "#22D3EE"),
                         ("AI agents", "#C4B5FD"), ("prompt eng.", "#F472B6")]),
    ("⚙️", "Backend & APIs", [("Python", "#3776AB"), ("FastAPI", "#009688"), ("Pydantic", "#E92063"),
                              ("REST", "#60A5FA"), ("OAuth 2.0", "#EB5424"), ("SSE", "#E6EDF3"),
                              ("WebRTC", "#9CA3AF"), ("React", "#61DAFB"), ("Streamlit", "#FF4B4B")]),
    ("📊", "Data & ML", [("PostgreSQL", "#4169E1"), ("SQL", "#E38C00"), ("MongoDB", "#47A248"),
                         ("sqlglot", "#A78BFA"), ("XGBoost", "#189FDD"), ("scikit-learn", "#F7931E"),
                         ("Power BI", "#F2C811"), ("Chart.js", "#FF6384")]),
    ("☁️", "Infra & integrations", [("Docker", "#2496ED"), ("AWS", "#FF9900"), ("Git", "#F03C2E"),
                                    ("GitHub Actions", "#2088FF"), ("MS Graph API", "#0078D4"),
                                    ("Odoo CRM", "#A24689"), ("Firebase", "#DD2C00")]),
]


def stack():
    W, ncol = 900, 2
    cw, gap, pad = (900 - 20) / 2, 20, 20
    ph, pgap = 30, 8
    cols = []
    for icon, title, items in STACK:
        x, y, pos = 0, 0, []
        for name, color in items:
            w = len(name) * 7.8 + 38
            if x + w > cw - 2 * pad:
                x, y = 0, y + ph + pgap
            pos.append((x, y, w, name, color))
            x += w + pgap
        cols.append((icon, title, pos, y + ph))
    rows = [cols[i:i + ncol] for i in range(0, len(cols), ncol)]
    row_h = [int(58 + max(c[3] for c in r) + 20) for r in rows]
    H = sum(row_h) + gap * (len(rows) - 1)
    css = ".col{animation:rise .8s cubic-bezier(.2,.7,.2,1) both}"
    label = "Tech stack — " + "; ".join(f"{t}: " + ", ".join(n for n, _ in items) for _, t, items in STACK)
    s = [svg_open(W, H, label, css)]
    s.append('<defs><linearGradient id="top" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#7C3AED"/>'
             '<stop offset="1" stop-color="#22D3EE"/></linearGradient></defs>\n')
    for i, (icon, title, pos, _) in enumerate(cols):
        r, c = divmod(i, ncol)
        cx, cy, ch = c * (cw + gap), sum(row_h[:r]) + gap * r, row_h[r]
        s.append(f'<g class="col" style="animation-delay:{i * .1:.1f}s">\n')
        s.append(f'<clipPath id="k{i}"><rect x="{cx + 1}" y="{cy + 1}" width="{cw - 2}" height="{ch - 2}" rx="16"/></clipPath>')
        s.append(f'<rect x="{cx + 1}" y="{cy + 1}" width="{cw - 2}" height="{ch - 2}" rx="16" fill="#0D1117" stroke="#30363D"/>')
        s.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="3" fill="url(#top)" clip-path="url(#k{i})"/>\n')
        s.append(f'<text x="{cx + pad}" y="{cy + 40}" font-size="16" fill="#fff">{icon}</text>'
                 f'<text class="mono" x="{cx + pad + 26}" y="{cy + 38}" font-size="12" letter-spacing="1.4" fill="#C9D1D9">{esc(title.upper())}</text>\n')
        for x, y, w, name, color in pos:
            px, py = cx + pad + x, cy + 58 + y
            s.append(f'<rect x="{px:.1f}" y="{py}" width="{w:.1f}" height="{ph}" rx="{ph / 2}" fill="#161B22" stroke="#30363D"/>'
                     f'<circle cx="{px + 15:.1f}" cy="{py + ph / 2}" r="4.5" fill="{color}"/>'
                     f'<text class="mono" x="{px + 27:.1f}" y="{py + 19.5}" font-size="13" fill="#E6EDF3">{esc(name)}</text>\n')
        s.append("</g>\n")
    s.append("</svg>\n")
    write("stack.svg", "".join(s))


# --------------------------------------------------------------------------- contact buttons
ICONS = {
    # globe
    "portfolio": '<g stroke="#fff" stroke-width="1.6" fill="none"><circle cx="9" cy="9" r="7.5"/>'
                 '<ellipse cx="9" cy="9" rx="3.4" ry="7.5"/><path d="M1.5 9h15M2.8 5h12.4M2.8 13h12.4"/></g>',
    # LinkedIn "in"
    "linkedin": '<rect width="18" height="18" rx="3.5" fill="#fff"/><g fill="#0A66C2"><rect x="3.2" y="7" width="2.8" height="8"/>'
                '<circle cx="4.6" cy="4.4" r="1.6"/><path d="M7.8 7h2.7v1.2c.5-.9 1.5-1.4 2.7-1.4 2.2 0 2.9 1.4 2.9 3.6V15h-2.8v-4c0-1-.2-1.9-1.3-1.9-1.2 0-1.5.9-1.5 1.9v4H7.8z"/></g>',
    # envelope
    "email": '<g stroke="#fff" stroke-width="1.6" fill="none" stroke-linejoin="round"><rect x=".8" y="2.8" width="16.4" height="12.4" rx="2.2"/>'
             '<path d="M1.5 4l7.5 6 7.5-6"/></g>',
}


def button(slug, label, bg):
    tw = len(label) * 9.4
    W, H = int(24 + 18 + 10 + tw + 24), 44
    grad = ('<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#7C3AED"/>'
            '<stop offset="1" stop-color="#2563EB"/></linearGradient>')
    fill = "url(#bg)" if bg == "grad" else bg
    s = [svg_open(W, H, label)]
    s.append(f'<defs>{grad}</defs>\n<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="{(H - 1) / 2}" fill="{fill}" stroke="#ffffff" stroke-opacity=".14"/>\n')
    s.append(f'<g transform="translate(24 13)">{ICONS[slug]}</g>\n')
    s.append(f'<text class="sans" x="52" y="27.5" font-size="15" font-weight="700" fill="#fff" letter-spacing=".2">{esc(label)}</text>\n</svg>\n')
    write(f"buttons/{slug}.svg", "".join(s))


# --------------------------------------------------------------------------- about-me editor card
ABOUT = [
    'class PavanKumar(AIEngineer):',
    '    """Turns manual business queues into AI systems that run on their own."""',
    '',
    '    role       = "AI Engineer @ Envision Beyond"',
    '    experience = {',
    '        "Envision Beyond":    "e-Invoicing at 2,000+ docs/mo · Graph API + Odoo CRM",',
    '        "Spire Technologies": "Data Analyst Consultant · Python–SQL, 100K+ records",',
    '    }',
    '    builds     = ["AI agents", "voice AI", "RAG", "enterprise ETL", "LLM failover"]',
    '    education  = "B.E. CS (Data Science) · MVJ College of Engineering · 2020–24"',
    '    certified  = ["Google Data Analytics", "HackerRank Python", "HackerRank Problem Solving"]',
]


def _tokens(line):
    import re
    out, pos = [], 0
    pat = re.compile(r'(?P<doc>""".*?""")|(?P<str>"[^"]*")|(?P<kw>\bclass\b)|(?P<cls>\b[A-Z][A-Za-z]+\b)'
                     r'|(?P<attr>^\s+[a-z_]+(?=\s*=))')
    for m in pat.finditer(line):
        if m.start() > pos:
            out.append((line[pos:m.start()], "#E6EDF3"))
        kind = m.lastgroup
        color = {"doc": "#8B949E", "str": "#A5D6FF", "kw": "#FF7B72", "cls": "#D2A8FF", "attr": "#79C0FF"}[kind]
        out.append((m.group(), color))
        pos = m.end()
    if pos < len(line):
        out.append((line[pos:], "#E6EDF3"))
    return out


def about():
    W, lh, top = 900, 24, 38
    H = top + 22 + lh * len(ABOUT) + 16
    css = ".r{animation:rise .8s cubic-bezier(.2,.7,.2,1) both}.cur{animation:blink 1.1s steps(1) infinite}"
    s = [svg_open(W, H, "whoami --verbose: " + " ".join(l.strip() for l in ABOUT), css)]
    s.append(f'<defs><clipPath id="ed"><rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14"/></clipPath>'
             f'<linearGradient id="top" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#22D3EE"/></linearGradient></defs>\n')
    s.append(f'<g class="r"><rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="#0D1117"/>\n'
             f'<g clip-path="url(#ed)"><rect width="{W}" height="{top}" fill="#161B22"/><rect y="{top}" width="{W}" height="1" fill="#21262D"/>'
             f'<rect width="{W}" height="2" fill="url(#top)"/><rect y="{top + 1}" width="46" height="{H}" fill="#0B0E14"/></g>\n'
             f'<rect x="1.5" y="1.5" width="{W - 3}" height="{H - 3}" rx="13.5" stroke="#30363D"/>\n')
    for k, c in enumerate(["#FF5F56", "#FFBD2E", "#27C93F"]):
        s.append(f'<circle cx="{22 + k * 20}" cy="{top / 2}" r="6" fill="{c}"/>')
    s.append(f'<rect x="96" y="7" width="150" height="{top - 7}" rx="6" fill="#0D1117"/>'
             f'<text class="mono" x="112" y="{top / 2 + 5}" font-size="12.5" fill="#E6EDF3">🐍 pavan_kumar.py</text>\n'
             f'<text class="mono" x="{W - 20}" y="{top / 2 + 5}" font-size="12" fill="#6E7681" text-anchor="end">python · utf-8</text>\n')
    y = top + 30
    for n, line in enumerate(ABOUT, 1):
        s.append(f'<text class="mono" x="32" y="{y}" font-size="13" fill="#484F58" text-anchor="end">{n}</text>')
        spans = "".join(f'<tspan fill="{c}">{esc(t)}</tspan>' for t, c in _tokens(line))
        cur = '<tspan class="cur" fill="#A78BFA">▋</tspan>' if n == len(ABOUT) else ""
        s.append(f'<text class="mono" x="62" y="{y}" font-size="14.5" xml:space="preserve">{spans}{cur}</text>\n')
        y += lh
    s.append("</g>\n</svg>\n")
    write("about.svg", "".join(s))


if __name__ == "__main__":
    hero()
    impact()
    for p in PROJECTS:
        project(*p)
    stack()
    about()
    button("portfolio", "Portfolio", "grad")
    button("linkedin", "LinkedIn", "#0A66C2")
    button("email", "Email", "#1F2937")
