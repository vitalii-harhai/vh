import datetime


def get_date_from_request(request_date: str) -> datetime:
    """
    Converts string ISO format to datetime instance
    :param request_date: String date in ISO format
    :return: date as Datetime instance
    """
    year, month, day = str(request_date).split("-")
    date = datetime.date(int(year), int(month), int(day))
    return date


def get_days_from_request(request_value: str):
    """
    Converts string number to integer
    :param request_value: String number
    :return: number as integer
    """
    days = ''
    for elem in request_value:
        if elem.isdigit():
            days += elem
    return int(days) if days else 0


def count_days_from_date(date: datetime, cal: int, bank: int, calendar: dict, reverse=False) -> str:
    """
    Working day = (weekday OR working day) AND NOT day off
    :param reverse: if Reverse == True --> counting before date
    :param date: date as Datetime instance
    :param cal: number of calendar days
    :param bank: number of working days
    :param calendar: json file that contains working and non-working days
    :return: string 'calendar days + bank days'
    """
    message = ''

    # counting calendar days
    if reverse:
        end_day_cal = date - datetime.timedelta(days=cal)
    else:
        end_day_cal = date + datetime.timedelta(days=cal)

    if cal:
        message += f"{str(cal)}-й календарний день - {end_day_cal.strftime('%d.%m.%Y (%A)')}"

    # counting bank days
    end_day_bank = end_day_cal
    weekday = (1, 2, 3, 4, 5)

    i = 1
    while i <= bank or i == 1:

        if reverse:
            end_day_bank -= datetime.timedelta(days=1)
        else:
            end_day_bank += datetime.timedelta(days=1)

        year = str(end_day_bank.year)

        if (end_day_bank.isoweekday() in weekday or str(end_day_bank) in calendar.get(year, {}).get('working', [])) \
                and not str(end_day_bank) in calendar.get(year, {}).get('non-working', []):
            i += 1

    if reverse:
        if cal and bank:
            message += f", а {bank}-й робочий день - {end_day_bank.strftime('%d.%m.%Y (%A)')}"
        elif cal and not bank:
            message += f", а попередній робочий день - {end_day_bank.strftime('%d.%m.%Y (%A)')}"
        elif not cal and bank:
            message += f"{bank}-й робочий день - {end_day_bank.strftime('%d.%m.%Y (%A)')}"
    else:
        if cal and bank:
            message += f", а {bank}-й робочий день - {end_day_bank.strftime('%d.%m.%Y (%A)')}"
        elif cal and not bank:
            message += f", а наступний робочий день - {end_day_bank.strftime('%d.%m.%Y (%A)')}"
        elif not cal and bank:
            message += f"{bank}-й робочий день - {end_day_bank.strftime('%d.%m.%Y (%A)')}"

    return message


def count_days_between_dates(start: datetime, end: datetime) -> str:
    count_calendar_days = (end - start - datetime.timedelta(days=1)).days
    if count_calendar_days > 0:
        message = f'Між датами {str(count_calendar_days)} календарних днів'
    else:
        message = ''
    return message
