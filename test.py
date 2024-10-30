import json
from datetime import datetime

days_of_week = {
    "Monday": "Понедельник",
    "Tuesday": "Вторник",
    "Wednesday": "Среда",
    "Thursday": "Четверг",
    "Friday": "Пятница",
    "Saturday": "Суббота",
    "Sunday": "Воскресенье"
}


week = datetime.now().isocalendar()
today_date = datetime.now().strftime("%d.%m.%Y")
weekday = datetime.now().strftime("%A")


with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
today = data[str(week[1] % 2)][str(week[2])]


def get_today_fan():
    return (f"""
*📅 {today_date}, {days_of_week[weekday]}*
Группа: __1-ТИВ-2__

||🎓 {today[0][0]}||
🕰 {today[0][1]}
🏢: {today[0][2]}

✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦✦

||🎓 {today[1][0]}||
🕰 {today[1][1]}
🏢: {today[1][2]}
""")


def mark_down_v2(text):
    return (text.replace('-', r'\-')
            .replace('.', r'\.')
            .replace('(', r'\(')
            .replace(')', r'\)'))
