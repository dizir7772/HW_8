from datetime import datetime, timedelta

users = [
    {"name": "Bill", "birthday": "22 July 1992"},
    {"name": "Jill", "birthday": "20 July 1994"},
    {"name": "Jan", "birthday": "22 July 1993"},
    {"name": "Sara", "birthday": "19 July 1985"},
    {"name": "Kim", "birthday": "19 July 1995"},
]


def get_birthdays_per_week(users):
    weekday = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
        'Next_Monday': ''
        }
    start = datetime.now().date()
    end = start + timedelta(days=7)
    for i in users:
        birthday = datetime.strptime(i["birthday"], "%d %B %Y")
        birthday_date = datetime(start.year, birthday.month, birthday.day)
        if start <= birthday_date.date() <= end:
            day = birthday_date.weekday()
            if day == 0:
                weekday['Monday'] += i['name']
                weekday['Monday'] += ', '
            if day == 1:
                weekday['Tuesday'] += i['name']
                weekday['Tuesday'] += ', '
            if day == 2:
                weekday['Wednesday'] += i['name']
                weekday['Wednesday'] += ', '
            if day == 3:
                weekday['Thursday'] += i['name']
                weekday['Thursday'] += ', '
            if day == 4:
                weekday['Friday'] += i['name']
                weekday['Friday'] += ', '
            if day in (5, 6):
                weekday['Next_Monday'] += i['name']
                weekday['Next_Monday'] += ', '

    for key, value in weekday.items():
        count = 0
        if len(value) > 0:
            print(key + ': ' + value[:-2])
        else:
            count += 1
    if count > 0:
        print("No one has a birthday this week")