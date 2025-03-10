import copy
# from cal_abstraction import TimeSpan, NamedTuple, ensure_type
from cal_abstraction import *
# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = NamedTuple("TimeSpanSeq", [("timespans", List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(time_spans = None):
    """creates a new timespan seq with or without a first timespan"""

    if time_spans == None:
        time_spans = []

    else:
        ensure_type(time_spans, List[TimeSpan])

    return TimeSpanSeq(time_spans)


def tss_is_empty(tss):
    """checks if the timespan seq is empty"""

    ensure_type(tss,TimeSpanSeq)
    return len(tss.timespans) == 0


def tss_plus_span(tss, ts):
    """add a timespan into the existing timespan seq in the right position"""

    ensure_type(tss,TimeSpanSeq)
    ensure_type(ts,TimeSpan)

    def insert_ts(timespans):
        """returns list of timespans with inserted timespan"""

        if not timespans or time_precedes(ts_start(ts), ts_start(timespans[0])):    # if timespan not empty and span start is before first span in timespans
            return [ts] + timespans
        else:
            return [timespans[0]] + insert_ts(timespans[1:])

    timespansseq = copy.deepcopy(tss)
    timespansseq = new_time_span_seq(insert_ts(timespansseq.timespans))
    return timespansseq


def tss_iter_spans(tss):
    """returns a list of the timespans in the seq as a list"""

    ensure_type(tss,TimeSpanSeq)
    if tss:
        for span in tss.timespans:
            yield span


def digit(num):
    if num < 10:
        return f'0{num}'
    return f'{num}'


def show_time_spans(tss):
    """prints all the time spans in the seq"""

    ensure_type(tss,TimeSpanSeq)

    print('===================================')
    for span in tss_iter_spans(tss):
        print(f"{digit(hour_number(time_hour(ts_start(span))))}:{digit(minute_number(time_minute(ts_start(span))))} - {digit(hour_number(time_hour(ts_end(span))))}:{digit(minute_number(time_minute(ts_end(span))))}")
    print('===================================')


def tss_keep_spans(tss, pred):
    """returns a list with the values that satisfy pred from the time span seq"""

    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result


def testing():
    testing_span_seq = new_time_span_seq()
    print('empty', tss_is_empty(testing_span_seq))
    show_time_spans(testing_span_seq)
    ts1 = new_time_span(new_time(new_hour(11),new_minute(30)),new_time(new_hour(13),new_minute(15)))
    ts2 = new_time_span(new_time(new_hour(12),new_minute(15)),new_time(new_hour(13),new_minute(0)))

    testing_span_seq = tss_plus_span(testing_span_seq, ts2)
    testing_span_seq = tss_plus_span(testing_span_seq, ts1)
    print('empty', tss_is_empty(testing_span_seq))
    show_time_spans(testing_span_seq)

    for span in tss_iter_spans(testing_span_seq):
        print(span)
    
    def pred(span):
        if ts_start(span) < new_time(new_hour(12),new_minute(0)):
            return True
        return False
    
    result = tss_keep_spans(testing_span_seq, pred)
    show_time_spans(result)


if __name__ == '__main__':
    testing()