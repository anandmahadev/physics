import re

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

with open('user.html', 'r', encoding='utf-8') as f:
    user_html = f.read()

m1 = re.search(r'<!-- ======= MODULE 1 ======= -->(.*?)<!-- end m1 -->', user_html, re.DOTALL).group(1)
m2 = re.search(r'<!-- ======= MODULE 2 ======= -->(.*?)<!-- end m2 -->', user_html, re.DOTALL).group(1)

m1 = m1.replace('id="m1"', 'id="c_m1"').replace('class="module active"', 'class="section active"')
m2 = m2.replace('id="m2"', 'id="c_m2"').replace('class="module"', 'class="section"')

# Also fix the inner onclicks for toggling
m1 = m1.replace('onclick="tog(this)"', 'onclick="tog_c(this)"')
m2 = m2.replace('onclick="tog(this)"', 'onclick="tog_c(this)"')

css_to_add = "\n  /* Chemistry Specific Styles */\n" + \
    "  .mod-label { font-size: 11px; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: #aaa; margin-bottom: 1.5rem; }\n" + \
    "  .qcard { border-bottom: 1px solid #f0f0f0; }\n" + \
    "  .qhead { display: flex; align-items: flex-start; gap: 14px; padding: 14px 0; cursor: pointer; }\n" + \
    "  .qno { font-size: 11px; font-weight: 600; color: #aaa; min-width: 24px; margin-top: 3px; flex-shrink: 0; }\n" + \
    "  .qtxt { font-size: 14px; font-weight: 500; flex: 1; color: #1a1a1a; line-height: 1.5; }\n" + \
    "  .arrow { color: #ccc; font-size: 16px; flex-shrink: 0; margin-top: 1px; transition: transform .2s; }\n" + \
    "  .qcard.open .arrow { transform: rotate(90deg); }\n" + \
    "  .qbody { display: none; padding: 0 0 18px 38px; }\n" + \
    "  .qcard.open .qbody { display: block; }\n" + \
    "  .ans { color: #333; font-size: 13.5px; line-height: 1.8; }\n" + \
    "  .ans b { font-weight: 600; color: #1a1a1a; }\n" + \
    "  .sec { font-size: 11px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; color: #aaa; margin: 16px 0 8px; }\n" + \
    "  .sec:first-child { margin-top: 0; }\n" + \
    "  ul.pts { list-style: none; padding: 0; display: flex; flex-direction: column; gap: 7px; }\n" + \
    "  ul.pts li { padding-left: 14px; position: relative; font-size: 13.5px; color: #333; line-height: 1.7; }\n" + \
    "  ul.pts li::before { content: '-'; position: absolute; left: 0; color: #ccc; }\n" + \
    "  ol.steps { padding-left: 20px; display: flex; flex-direction: column; gap: 7px; }\n" + \
    "  ol.steps li { font-size: 13.5px; color: #333; line-height: 1.7; padding-left: 4px; }\n" + \
    "  .box { background: #fafafa; border: 1px solid #ebebeb; border-radius: 8px; padding: 12px 14px; margin: 12px 0; font-size: 13px; color: #444; line-height: 1.75; }\n" + \
    "  .box b { color: #1a1a1a; }\n" + \
    "  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 10px 0; }\n" + \
    "  .cell { background: #fafafa; border: 1px solid #ebebeb; border-radius: 8px; padding: 12px; font-size: 13px; color: #444; line-height: 1.7; }\n" + \
    "  .cell .ct { font-size: 11px; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; color: #888; margin-bottom: 8px; }\n" + \
    "  .note { font-size: 12.5px; color: #888; border-left: 2px solid #e8e8e8; padding-left: 12px; margin-top: 12px; line-height: 1.65; font-style: italic; }\n" + \
    "  .pill { display: inline-block; font-family: monospace; font-size: 12px; background: #f4f4f4; border: 1px solid #e8e8e8; padding: 2px 9px; border-radius: 12px; margin: 2px 3px; color: #333; }\n"

# Only insert CSS if it's not already there
if "Chemistry Specific Styles" not in orig:
    orig = orig.replace('</style>', css_to_add + '</style>')

chemistry_section = f"""
    <!-- CHEM MODULE 1 -->
    <div class="section active" id="c_m1">
{m1}
    </div>

    <!-- CHEM MODULE 2 -->
    <div class="section" id="c_m2">
{m2}
    </div>"""

target_html = """    <!-- CHEM MODULE 1 -->
    <div class="section active" id="c_m1">
      <h2>Module 1 Title Here</h2>
      <!-- Add your Chemistry Module 1 content here -->
    </div>

    <!-- CHEM MODULE 2 -->
    <div class="section" id="c_m2">
      <h2>Module 2 Title Here</h2>
      <!-- Add your Chemistry Module 2 content here -->
    </div>"""

orig = orig.replace(target_html, chemistry_section)

if "function tog_c(" not in orig:
    orig = orig.replace('</script>', '\n  function tog_c(header) {\n    header.parentElement.classList.toggle(\'open\');\n  }\n</script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(orig)

print("Merged successfully!")
