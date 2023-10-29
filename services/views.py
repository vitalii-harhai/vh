from django.shortcuts import render
from django.conf import settings

import services.days_calculator_functions as calc_function
import json
import datetime
import locale

TABS = ('before_tab', 'between_tab', 'after_tab')


def index(request):
    return render(request, 'services/services.html')


def calculator(request):

    if settings.DEBUG:
        locale.setlocale(locale.LC_TIME, 'uk_UA')  # for mac OS
    else:
        locale.setlocale(locale.LC_TIME, 'uk_UA.utf8')  # for linux OS

    today = datetime.date.today()

    context = {}

    with open('static/calendar.json', mode="r") as file:
        json_calendar = json.load(file)

    # ACTIVE TAB
    active_tab = str(request.GET.get('active_tab')).replace('-', '_')

    if active_tab not in TABS:
        active_tab = 'after_tab'

    for tab in TABS:
        if tab == active_tab:
            value_tab = {'nav_link': ' active', 'aria_selected': 'true', 'tab_pane_fade': ' show active'}
        else:
            value_tab = {'nav_link': '', 'aria_selected': 'false', 'tab_pane_fade': ''}
        context.update({tab: value_tab})

    # BEFORE
    before_date = request.GET.get('before_date', default=str(today))
    before_calendar_days = request.GET.get('before_calendar_days', default='')
    before_calendar_days = calc_function.get_days_from_request(before_calendar_days)
    before_bank_days = request.GET.get('before_bank_days', default='')
    before_bank_days = calc_function.get_days_from_request(before_bank_days)

    context.update({'before_date': before_date})
    context.update({'before_calendar_days': before_calendar_days})
    context.update({'before_bank_days': before_bank_days})

    before_message = calc_function.count_days_from_date(
        date=calc_function.get_date_from_request(before_date),
        cal=before_calendar_days,
        bank=before_bank_days,
        calendar=json_calendar,
        reverse=True
    )

    context.update({'before_message': before_message})

    # BETWEEN
    between_start_date = request.GET.get('between_start_date', default=str(today))
    between_end_date = request.GET.get('between_end_date', default=str(today))

    context.update({'between_start_date': between_start_date})
    context.update({'between_end_date': between_end_date})

    between_message = calc_function.count_days_between_dates(
        start=calc_function.get_date_from_request(between_start_date),
        end=calc_function.get_date_from_request(between_end_date))
    context.update({'between_message': between_message})

    # AFTER
    after_date = request.GET.get('after_date', default=str(today))
    after_calendar_days = request.GET.get('after_calendar_days', default='')
    after_calendar_days = calc_function.get_days_from_request(after_calendar_days)
    after_bank_days = request.GET.get('after_bank_days', default='')
    after_bank_days = calc_function.get_days_from_request(after_bank_days)

    context.update({'after_date': after_date})
    context.update({'after_calendar_days': after_calendar_days})
    context.update({'after_bank_days': after_bank_days})

    after_message = calc_function.count_days_from_date(
        date=calc_function.get_date_from_request(after_date),
        cal=after_calendar_days,
        bank=after_bank_days,
        calendar=json_calendar
    )

    context.update({'after_message': after_message})

    return render(request, 'services/tabs.html', context=context)
