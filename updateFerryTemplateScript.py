from pathlib import Path

template = Path("template.html")
output = Path("Direct ferries template.html")

replacements = {
    "666666": "12345677",
      "Mykhailo Hriha": "Vasyl Pomazanskiy",
      "Vasyl-Chiprian Hriha": "Ion Creanga",
      "start 1": "Thu 8 Nov 2026 23:10",
    "start 2": "Thu 9 Nov 2026 23:30",
    "arrival 1": "Sun 13 Nov 2026 10:10",
    "arrival 2": "Mon 14 Nov 2026 12:10",
    "CE6666CE": "CE0012CH",
    "196.61£": "150.00£"
}

text = template.read_text(encoding="utf-8")

for old, new in replacements.items():
    text = text.replace(old, new)

output.write_text(text, encoding="utf-8")

print("index.html successfully generated from template.html")