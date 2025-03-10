import copy
from cal_abstraction import *
from cal_ui import *

def ap_remove(cal_day,start):
    """returns new versions without unwanted appointment"""

    def remove_app(ap_list):
        """returns and searches list without unvanted appointment"""
        
        if not ap_list:
            print("No appointments matching the description this day.\n")
            return []

        elif time_equals(start,ts_start(app_span(ap_list[0]))):
            print("The appointment has been removed.")
            return ap_list[1:]

        else:            
            return [ap_list[0]] + remove_app(ap_list[1:])

    return CalendarDay(cd_day(cal_day),remove_app(cal_day.appointments))


def remove(cal_name, day, mon, start):
    """reformate for remove booking"""
    day = new_day(day)
    mon = new_month(mon)
    new_date(day, mon)
    cal_year = get_calendar(cal_name)
    start = new_time_from_string(start)
    old_day = cm_get_day(cy_get_month(mon,cal_year),day)
    day = ap_remove(old_day,start)
    new_calendar_month = cm_plus_cd(cy_get_month(mon, cal_year), day)
    new_calendar_year = cy_plus_cm(cal_year,new_calendar_month)
    insert_calendar(cal_name,new_calendar_year)


if __name__ == "__main__":
    create("Jayne")
    book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
    book("Jayne", 20, "sep", "15:00", "16:00", "help train")
    show("Jayne", 20, "sep")
    remove("Jayne", 20, "sep", "12:00")
    remove("Jayne", 20, "sep", "15:01")
    show("Jayne", 20, "sep")

