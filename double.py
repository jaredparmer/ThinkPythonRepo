""" exercise 16.2 of Downey, _think python_ 2nd ed
"""

from datetime import datetime


def print_dow(d=datetime.today()):
    weekday = datetime.weekday(d)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']
    print(f"Today is {days[weekday]}.")


""" birthdate is Datetime object.
"""
def birthday_info(birthdate):
    today = datetime.today()
    print(f"You are {today.year - birthdate.year} years old!")
    next_bday = birthdate.replace(year=today.year)
    if next_bday < today:
        next_bday = next_bday.replace(year=next_bday.year + 1)

    diff = next_bday - today
    print(f"Your next birthday is in {diff.days} days, {diff.seconds // 3600} "
          f"hours, {(diff.seconds % 3600) // 60} minutes, and "
          f"{diff.seconds % 60} seconds!")


while True:
    bday = input("What is your birthday? (yyyy-mm-dd, 'Q' to quit) ")
    if bday == 'Q':
        break
    data = bday.split(sep='-')
    for i in range(len(data)):
        data[i] = int(data[i])
    birthday = datetime(*data)
    birthday_info(birthday)
