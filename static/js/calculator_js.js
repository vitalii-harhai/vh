function tab_js()
{
    let active_tab;

    try {
        active_tab = document.getElementsByClassName('nav-link active')[0].id;
    } catch (err) {
        active_tab = ''
    }

    let before_date;

    try {
        before_date = document.getElementById("before_date").value;
    } catch (err) {
        before_date = '';
    }

    let before_calendar_days;

    try {
        before_calendar_days = document.getElementById("before_calendar_days").value;
    } catch (err) {
        before_calendar_days = 0;
    }

    let before_bank_days;

    try {
        before_bank_days = document.getElementById("before_bank_days").value;
    } catch (err) {
        before_bank_days = 0;
    }

    let between_start_date;

    try {
        between_start_date = document.getElementById("between_start_date").value;
    } catch (err) {
        between_start_date = '';
    }

    let between_end_date;

    try {
        between_end_date = document.getElementById("between_end_date").value;
    } catch (err) {
        between_end_date = '';
    }

    let after_date;

    try {
        after_date = document.getElementById("after_date").value;
    } catch (err) {
        after_date = '';
    }

    let after_calendar_days;

    try {
        after_calendar_days = document.getElementById("after_calendar_days").value;
    } catch (err) {
        after_calendar_days = 0;
    }

    let after_bank_days;

    try {
        after_bank_days = document.getElementById("after_bank_days").value;
    } catch (err) {
        after_bank_days = 0;
    }

    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
//            document.getElementById("content").innerHTML = xhttp.responseText;
            document.body.innerHTML = xhttp.responseText;
        }
    };

    xhttp.open(
        "GET",
        `?&active_tab=${active_tab}&before_date=${before_date}&before_calendar_days=${before_calendar_days}&before_bank_days=${before_bank_days}&between_start_date=${between_start_date}&between_end_date=${between_end_date}&after_date=${after_date}&after_calendar_days=${after_calendar_days}&after_bank_days=${after_bank_days}`,
        true
    );

    xhttp.send();
}