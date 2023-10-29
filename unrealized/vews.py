from django.shortcuts import render
from django.conf import settings
import datetime
import calendar
import locale


def month_name(number: int):
    names = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень',
             'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']
    return names[number - 1]


def create_calendar_view(first_day_view, start, end_day_view, end):
    month = []
    temp_date = first_day_view
    temp_week = []
    while temp_date <= end_day_view:
        for d in range(7):
            if temp_date < start or temp_date > end:
                day_style = ''
            elif temp_date == start or temp_date == end:
                day_style = 'font-weight: bold; background-color: #CECECE'
            else:
                day_style = 'background-color: #ECF0F1'
            temp_week.append((temp_date.day, day_style))
            temp_date += datetime.timedelta(1)
        else:
            month.append(temp_week)
            temp_week = []
    return month


def first_day_week(date: datetime) -> datetime:
    first_week_day = date - datetime.timedelta(date.isocalendar().weekday - 1)
    return first_week_day


def end_day_week(date: datetime) -> datetime:
    end_week_day = date + datetime.timedelta(7 - date.isocalendar().weekday)
    return end_week_day


def index(request):

    if settings.DEBUG:
        locale.setlocale(locale.LC_TIME, 'uk_UA')  # for mac OS
    else:
        locale.setlocale(locale.LC_TIME, 'uk_UA.utf8')  # for linux OS

    start_day = datetime.date(2023, 12, 3)
    first_day_start_month = datetime.date(start_day.year, start_day.month, 1)
    first_day_view_start_month = first_day_week(first_day_start_month)

    end_day = datetime.date(2023, 12, 21)
    end_day_end_month = datetime.date(end_day.year, end_day.month, calendar.monthrange(end_day.year, end_day.month)[1])
    end_day_view_end_month = end_day_week(end_day_end_month)

    start_month = []
    end_month = []

    if start_day.month == end_day.month:
        start_month = create_calendar_view(
            first_day_view=first_day_view_start_month,
            start=start_day,
            end_day_view=end_day_view_end_month,
            end=end_day)
    else:
        start_month = create_calendar_view(
            first_day_view=first_day_view_start_month,
            start=start_day,
            end_day_view=datetime.date(start_day.year, start_day.month,
                                       calendar.monthrange(start_day.year, start_day.month)[1]),
            end=end_day)
        end_month = create_calendar_view(
            first_day_view=first_day_week(datetime.date(end_day.year, end_day.month, 1)),
            start=start_day,
            end_day_view=end_day_week(
                datetime.date(end_day.year, end_day.month, calendar.monthrange(end_day.year, end_day.month)[1])),
            end=end_day)

    context = {
        'start_month': start_month,
        'start_month_name': f"{month_name(start_day.month)} {start_day.year}",
        'end_month': end_month,
        'end_month_name': f"{month_name(end_day.month)} {end_day.year}"
    }

    return render(request, 'index.html', context=context)
