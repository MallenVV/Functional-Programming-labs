# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests
from lab8d import free_spans


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()

    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time

    # -------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.

    store_test_case(                  # testing over start and end
        test_cases,
        2,
        start_str="08:00",  # Search interval starts
        end_str="17:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00"],
        )

    store_test_case(                  # testing no booking
        test_cases,
        3,
        start_str="02:00",  # Search interval starts
        end_str="22:00",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["02:00-22:00"],
        )

    store_test_case(                  # testing start and end at same time
        test_cases,
        4,
        start_str="10:00",  # Search interval starts
        end_str="10:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=[],
        )
        
    store_test_case(                  # testing a lot of bookings and small empty slots
        test_cases,
        5,
        start_str="06:00",  # Search interval starts
        end_str="20:00",  # Search interval ends
        booking_data=["05:00-06:30", "07:00-09:00", "09:30-12:30", "13:00-18:00", "18:45-19:40"],  # This day's appointments
        exp_result=["06:30-07:00", "09:00-09:30", "12:30-13:00", "18:00-18:45", "19:40-20:00"],
        )

    store_test_case(                  # testing overlapping bookings 
        test_cases,
        6,
        start_str="07:00",  # Search interval starts
        end_str="17:00",  # Search interval ends
        booking_data=["09:00-13:00", "09:00-18:00"],  # This day's appointments
        exp_result=["07:00-09:00"],
        )
    
    store_test_case(                  # testing one overlapping appointment
        test_cases,
        7,
        start_str="07:00",  # Search interval starts
        end_str="17:00",  # Search interval ends
        booking_data=["06:00-18:00"],  # This day's appointments
        exp_result=[],
        )

    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
