from pathlib import Path
import re

latex_file = Path(__file__).parent / "rcci_template.tex"

latex_content = latex_file.read_text(encoding='utf8')

subs = [
    ("á", r"\'a"),
    ("é", r"\'e"),
    ("í", r"\'i"),
    ("ó", r"\'o"),
    ("ú", r"\'u"),
    ("ü", r'\"u'),
    ("ñ", r"\~n"),
    ("Á", r"\'A"),
    ("É", r"\'E"),
    ("Í", r"\'I"),
    ("Ó", r"\'O"),
    ("Ú", r"\'U"),
    ("Ü", r'\"U'),
    ("Ñ", r"\~N"),
]

for find, replace in subs:
    latex_content = re.sub(find, replace, latex_content)

latex_file.write_text(latex_content, encoding="utf8")
