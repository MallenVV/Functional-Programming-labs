# Write your code for lab 8d here.
# from cal_abstraction import CalendarDay, Time
from cal_abstraction import *
from cal_ui import *
from lab8b import *
from settings import CHECK_AGAINST_FACIT

if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    """returns a list of timespans that are inbetween appointments"""

    free_seq = new_time_span_seq()
    free_start = start

    if time_equals(start, end):
        return [TimeSpanSeq]

    for app in cd_iter_appointments(cal_day):

        app_start = ts_start(app_span(app))
        app_end = ts_end(app_span(app))

        if time_precedes(start, app_start) and time_precedes(free_start, app_start):

            if time_precedes(free_start, app_start):
                free_seq = tss_plus_span(free_seq, new_time_span(free_start, app_start))
            
            elif time_precedes(free_start, end):
                free_seq = tss_plus_span(free_seq, new_time_span(free_start, end))

        if time_precedes(end, app_start):
            break

        free_start = app_end

    if time_precedes(free_start, end):
        free_seq = tss_plus_span(free_seq, new_time_span(free_start, end))

    return free_seq


def show_free(cal: str, day: int, month: str, start_str: str, end_str: str):
    """shows the timespans that are free from the calander day inbetween the end and start given"""
    
    cy = get_calendar(cal)
    cm = cy_get_month(new_month(month),cy)
    cal_day = cm_get_day(cm, new_day(day))
    
    start = new_time_from_string(start_str)
    end = new_time_from_string(end_str)

    seq = free_spans(cal_day, start, end)

    show_time_spans(seq)


if __name__ == '__main__':
    create("Jayne")
    book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
    book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
    show_free("Jayne", 20, "sep", "08:00", "19:00")