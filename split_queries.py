import re
from pathlib import Path

text = Path("sales.session.sql").read_text(encoding="utf-8")
Path("queries").mkdir(exist_ok=True)

parts = re.split(r"(?m)^-- (\S+\.sql)\s*$", text)
for i in range(1, len(parts), 2):
    name, body = parts[i], parts[i + 1].strip() + "\n"
    n = i // 2 + 1
    Path("queries", f"{n:02d}_{name}").write_text(body, encoding="utf-8")
    print("wrote", f"{n:02d}_{name}")