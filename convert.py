import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove accordion logic and convert qcard to card
text = re.sub(r'<div class="qcard[^>]*>', '<div class="card">', text)

# Convert qhead, qno, qtxt into q
def repl_qhead(match):
    qno = match.group(1).strip()
    qtxt = match.group(2).strip()
    return f'<div class="q">{qno}. {qtxt}</div>'
text = re.sub(r'<div class="qhead"[^>]*><div class="qno">(.*?)</div><div class="qtxt">(.*?)</div><div class="arrow">.*?</div></div>', repl_qhead, text)

# Convert qbody and ans
text = text.replace('<div class="qbody"><div class="ans">', '<div class="a">')
# the closing div of qbody is just an extra /div, let's fix it at the end of every answer
# We'll just replace </div></div> closing the qbody with </div> because qbody had 2 divs. 
text = text.replace("    </div></div>\n  </div>", "    </div>\n  </div>")

# Convert .sec to bold
text = re.sub(r'<div class="sec">(.*?)</div>', r'<b>\1</b><br>', text)

# Convert .note to .tip
text = text.replace('class="note"', 'class="tip"')

# Convert .box to .eg
text = text.replace('class="box"', 'class="eg"')

# Convert lists (ul.pts and ol.steps) to points
def convert_list(match):
    items = re.findall(r'<li>(.*?)</li>', match.group(0), flags=re.DOTALL)
    out = []
    for i, item in enumerate(items, 1):
        out.append(f'<div class="point"><div class="pnum">{i}</div><div class="ptxt">{item.strip()}</div></div>')
    return '\n'.join(out)

text = re.sub(r'<ul class="pts">(.*?)</ul>', convert_list, text, flags=re.DOTALL)
text = re.sub(r'<ol class="steps">(.*?)</ol>', convert_list, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Converted successfully!")
