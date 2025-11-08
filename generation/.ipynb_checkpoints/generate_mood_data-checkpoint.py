import json
import random
from datetime import datetime, timedelta

male_names = ["Sergey", "Alex", "Ivan", "Dmitry", "Nikita", "Andrey", "Vlad", "Maksim", "Roman", "Egor"]
female_names = ["Anna", "Maria", "Elena", "Olga", "Alina", "Sofia", "Ksenia", "Polina", "Daria", "Viktoria"]

mood_emojis = {
    1: "😭",  # очень плохо
    2: "😔",  # грустно
    3: "😐",  # нейтрально
    4: "😊",  # хорошо
    5: "😄"   # отлично
}

sample_notes = [
    "День прошёл спокойно.",
    "Было весело с друзьями.",
    "Устала от учёбы.",
    "Погода подняла настроение.",
    "Ссорился с кем-то, день не задался.",
    "Сегодня чувствую себя отлично!",
    "Ничего особенного не произошло.",
    "Сходил в кино — понравилось.",
    "Грустно, но надеюсь завтра будет лучше.",
    "Получилось сделать всё запланированное."
    "Было очень тяжело удержаться и не спеть песню Борика ТЫЦН-ДЫЦН"
]

motivational_images = [
    {"category": "cats", "url": "https://i.pinimg.com/1200x/30/b2/af/30b2aff9cd919dd2b5715fb1b51f7456.jpg"},
    {"category": "cats", "url": "https://i.pinimg.com/736x/e1/79/1a/e1791aa1a6fb474837077e485aefe532.jpg"},

    {"category": "reminder", "url": "https://i.pinimg.com/736x/50/01/14/500114f10ff06173deaadbc6448b3b35.jpg"},
    {"category": "reminder", "url": "https://i.pinimg.com/736x/84/6d/d9/846dd93db6511814935d4f871d20c0b9.jpg"},

    {"category": "nature", "url": "https://i.pinimg.com/736x/c4/f8/ac/c4f8acf1c7ad89a976acaf7e61288f67.jpg"},
    {"category": "nature", "url": "https://i.pinimg.com/736x/7d/e7/72/7de77258f973086a7b17c1fbaf24091f.jpg"},

    {"category": "funny", "url": "https://i.pinimg.com/736x/f4/ed/e0/f4ede0597d74a1eee73af133afc70b6d.jpg"},
    {"category": "funny", "url": "https://i.pinimg.com/736x/9e/f0/12/9ef01201ec457250bffeeba8852fc080.jpg"},
    {"category": "funny", "url": "https://i.pinimg.com/1200x/32/01/4b/32014bd6589629861edfd0cc80d165b1.jpg"}
]

def generate_user(user_id):
    gender = random.choice(["male", "female"])
    name = random.choice(male_names if gender == "male" else female_names)
    age = random.randint(16, 30)
    moods = []

    start_date = datetime(2025, 10, 10)
    for i in range(30):  # записи за 30 дней
        date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        mood_score = random.randint(1, 5)
        moods.append({
            "date": date,
            "mood_score": mood_score,
            "mood_emoji": mood_emojis[mood_score],
            "note": random.choice(sample_notes)
        })

    return {
        "user_id": user_id,
        "name": name,
        "gender": gender,
        "age": age,
        "moods": moods
    }

data = {
    "users": [generate_user(i + 1) for i in range(20)],
    "motivational_images": motivational_images
}

with open("mood_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Файл сгенерирован")
