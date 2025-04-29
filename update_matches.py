import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://yalla-shoot-hd.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

matches = []

# تعديل حسب بنية الموقع
for card in soup.select('.match-card'):  # هذا مجرد مثال. يمكن يتغير
    try:
        home = card.select_one('.team1').get_text(strip=True)
        away = card.select_one('.team2').get_text(strip=True)
        time = card.select_one('.match-time').get_text(strip=True)
        comp = card.select_one('.match-title').get_text(strip=True)

        matches.append({
            "homeTeam": home,
            "awayTeam": away,
            "time": time,
            "competition": comp
        })
    except Exception:
        continue

# حفظ إلى ملف JSON
with open("matches.json", "w", encoding="utf-8") as f:
    json.dump({"matches": matches}, f, ensure_ascii=False, indent=2)

print(f"{len(matches)} matches saved at {datetime.now()}")
