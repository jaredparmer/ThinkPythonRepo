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


def double_day(bday1, bday2, factor=2):
    gap = bday2 - bday1
    double_day = bday2 + gap / (factor - 1)
    print(f"Your {factor}-Factor Day is ", end='')
    print(double_day.strftime('%B') + ' ' + double_day.strftime('%d') + ', '
          + double_day.strftime('%Y'))


# driver code for birthday_info
while True:
    bday = input("What is your birthday? (yyyy-mm-dd, 'Q' to quit) ")
    if bday == 'Q':
        break
    data = bday.split(sep='-')
    for i in range(len(data)):
        data[i] = int(data[i])
    birthday = datetime(*data)
    birthday_info(birthday)

# driver code for double_day
while True: 
    bday1 = input("What is the first birthday? (yyyy-mm-dd, 'Q' to quit) ")
    if bday1 == 'Q':
        break
    data = bday1.split(sep='-')
    for i in range(len(data)):
        data[i] = int(data[i])
    bday1 = datetime(*data)

    bday2 = input("What is the second birthday? (yyyy-mm-dd, 'Q' to quit) ")
    if bday2 == 'Q':
        break
    data = bday2.split(sep='-')
    for i in range(len(data)):
        data[i] = int(data[i])
    bday2 = datetime(*data)

    factor = input("What is the factor? (integer, 'Q' to quit) ")
    if factor == 'Q':
        break

    double_day(bday1, bday2, int(factor))
