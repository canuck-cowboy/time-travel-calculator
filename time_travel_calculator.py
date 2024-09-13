from datetime import date, timedelta


def find_day(num_days):
    """
    calculate the day of the week and the date after a specified number of days from today. could be in the
    past or future.

    :param num_days: number of days to advance from today
    :return: a tuple that holds the weekday and the future date
    """
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # get the numeric value of today's date: 0-6 (0 being Monday and 6 being Sunday)
    today_numeric = date.today().weekday()
    # calculate the numeric value of the future weekday  by adding (num_days param to today_numeric) % 7
    new_numeric_day = (today_numeric + num_days) % 7
    # Compute the future date by adding num_days param to today's date using the timedelta function
    # (timedelta(days=) is used to represent the difference between two dates)
    new_date = date.today() + timedelta(days=num_days)
    return weekdays[new_numeric_day], new_date


while True:
    try:
        days_advanced = int(input("How many days shall we advance or go back from today: "))
        break
    except ValueError:
        print('You should enter an integer.')

future_day, future_date = find_day(days_advanced)
print('We arrive on a', future_day, '- Date:', future_date)
