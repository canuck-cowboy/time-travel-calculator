import datetime


def find_day(num_days):
    """
    calculate the day of the week and the date after a specified number of days from today. could be in the
    past or future.

    :param num_days: number of days to advance from today
    :return: a tuple that holds the weekday and the future date
    """
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # get the numeric value of today's date: 0-6 (0 being Monday and 6 being Sunday)
    today_numeric = datetime.date.today().weekday()
    # calculate the numeric value of the future weekday  by adding (num_days param to today_numeric) % 7
    new_numeric_day = (today_numeric + num_days) % 7
    # Compute the future date by adding num_days param to today's date using the timedelta function
    # (timedelta(days=) is used to represent the difference between two dates)
    new_date = datetime.date.today() + datetime.timedelta(days=num_days)
    return weekdays[new_numeric_day], new_date


def find_hour(hours_to_advance):
    # get a datetime object that includes year-month-day hour:minute:sec:microsecond of the current time
    current_time = datetime.datetime.now()
    # add hours_to_advance to the current time. We can only do that using datetime.timedelta
    new_time = current_time + datetime.timedelta(hours=hours_to_advance)
    # return the new datetime object
    return new_time


def get_user_input(prompt):
    """
    This function ensures that the user enters a valid integer
    :param prompt:
    :return:
    """
    while True:
        try:
            travel = int(input(prompt))
            break
        except ValueError:
            print('You should enter an integer.')
    return travel


def main():
    # ensure that the first user input is one of these options
    base = ['d', 'days', 'h', 'hours']
    # This control variable determines whether we are going to use the find_day() or find_hour() function
    time_unit_choice = None
    while time_unit_choice not in base:
        time_unit_choice = input('Shall we journey through time by (D)ays or (H)ours: ').lower()

    # if the user chooses d or days
    if time_unit_choice in base[:2]:
        days_advanced = get_user_input("How many DAYS shall we advance or go back from today: ")
        # compute future/past day and dates using the find_day(arg) function
        new_day, new_date = find_day(days_advanced)
        # print the result. Note that strftime() works on datetime objects only
        print('We arrive on a', new_day, '- Date:', new_date.strftime('%Y-%m-%d'))

    # if the user chooses h or hours
    elif time_unit_choice in base[2:]:
        hours_advanced = get_user_input("How many HOURS shall we advance or go back from today: ")
        # compute new time using the find_hour(arg) function. we get a datetime object that we NEED to format
        new_hour = find_hour(hours_advanced)
        # print the result. Note that strftime() works on datetime objects only
        print('We arrive at', new_hour.strftime("%H:%M - %b %d, %Y"))


if __name__ == '__main__':
    main()
