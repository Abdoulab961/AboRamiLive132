import json
from datetime import datetime

# بيانات تجريبية
matches = {
    "matches": [
        {
            "homeTeam": "ريال مدريد",
            "awayTeam": "برشلونة",
            "time": "22:00",
            "competition": "الدوري الإسباني"
        },
        {
            "homeTeam": "ليفربول",
            "awayTeam": "مانشستر سيتي",
            "time": "21:00",
            "competition": "الدوري الإنجليزي"
        }
    ]
}

# حفظ البيانات في matches.json
with open("matches.json", "w", encoding="utf-8") as f:
    json.dump(matches, f, ensure_ascii=False, indent=2)

print("تم تحديث matches.json بنجاح:", datetime.now())
