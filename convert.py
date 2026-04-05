"""
Physics HTML Notes Converter
---------------------------
Updates and refactors HTML structure for physics study materials, 
converting various question formats and stylistic elements to a 
more modern look and feel.
"""
import re

FILE_PATH = 'index.html'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def convert_html(text):
    # Remove accordion logic and convert qcard to card
    text = re.sub(r'<div class="qcard[^>]*>', '<div class="card">', text)

    # Convert .sec to bold
    text = re.sub(r'<div class="sec">(.*?)</div>', r'<b>\1</b><br>', text)

    # Convert qhead, qno, qtxt into q
    def repl_qhead(match):
        qno = match.group(1).strip()
        qtxt = match.group(2).strip()
        return f'<div class="q">{qno}. {qtxt}</div>'
    text = re.sub(r'<div class="qhead"[^>]*><div class="qno">(.*?)</div><div class="qtxt">(.*?)</div><div class="arrow">.*?</div></div>', repl_qhead, text)

    # Simple string replacements
    replacements = {
        '<div class="qbody"><div class="ans">': '<div class="a">',
        '    </div></div>\n  </div>': '    </div>\n  </div>',
        'class="note"': 'class="tip"',
        'class="box"': 'class="eg"'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Convert lists (ul.pts and ol.steps) to points
    def convert_list(match):
        items = re.findall(r'<li>(.*?)</li>', match.group(0), flags=re.DOTALL)
        out = []
        for i, item in enumerate(items, 1):
            out.append(f'<div class="point"><div class="pnum">{i}</div><div class="ptxt">{item.strip()}</div></div>')
        return '\n'.join(out)

    text = re.sub(r'<ul class="pts">(.*?)</ul>', convert_list, text, flags=re.DOTALL)
    text = re.sub(r'<ol class="steps">(.*?)</ol>', convert_list, text, flags=re.DOTALL)
    return text

if __name__ == "__main__":
    content = read_file(FILE_PATH)
    updated_content = convert_html(content)
    write_file(FILE_PATH, updated_content)
    print("Converted successfully!")
