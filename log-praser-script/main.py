import os
import pandas_praser
from pandas_praser import pandas_function_to_prase_logs


def function_seeking_line_with_error(): #OOM ISSUE
    log_file = open('sample-log.log').read().splitlines()
    path = os.path.abspath(os.getcwd())
    for line in log_file:
        if "ERROR" in line:
            print(line)

def streaming_function_seeking_line_with_error():
    with open('sample-log.log') as f:
        count_lines = 0
        for line in f:
            if "ERROR" in line:
                count_lines += 1
                print(line)
        print(f"\nThere is {count_lines} ERROR lines in the log file")


if __name__ == "__main__":
    #function_seeking_line_with_error()
    #streaming_function_seeking_line_with_error()
    pandas_function_to_prase_logs()