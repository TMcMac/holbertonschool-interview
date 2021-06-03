#!/usr/bin/python3
"""A short function for use with 0-generator.py """
import sys


def parse_data():
    """
    parse_data is a function that will read lines from stdin
    which include file sizes and status codes from websites.

    The function will sum up the file sizes into a total, and
    every 10 lines read (or at the time of a keyboard interrupt)
    the program will output a total size of the summed file sizes
    and a tally of the status codes we received.
    """

    count = 0  # Tracks 10 iterations for printing
    codes = []  # All valid status codes received
    statuscodes = [200, 301, 400, 401, 403, 404, 405, 500]  # Valid codes
    filesizes = []  # list of file sizes received

    try:
        for line in sys.stdin:  # Reading lines from stdin
            if line == "":  # if empty line, skip
                continue
            count += 1
            parsing = line.split()  # Break up line by spaces
            filesizes.append(int(parsing[-1]))  # last element is filesize
            if int(parsing[-2]) in statuscodes:  # second to last is status code
                codes.append(int(parsing[-2]))
            if count % 10 == 0:  # Every ten rounds print data
                print("File size: {}".format(sum(filesizes)))  # sumall file sizes
                codes_dict = {i: codes.count(i) for i in codes}  # dict of codes and count
                for k, v in codes_dict.items():
                    print("{}: {}".format(k, v))
        # we leave the loop if we run out of lines
        # If we didn't just print we need to
        if count % 10 != 0:
            print("File size: {}".format(sum(filesizes)))
            codes_dict = {i: codes.count(i) for i in codes}
            for k, v in codes_dict.items():
                print("{}: {}".format(k, v))
    # If a ctrl C is sent, final print and quit
    except KeyboardInterrupt:
        print("File size: {}".format(sum(filesizes)))
        codes_dict = {i: codes.count(i) for i in codes}
        for k, v in codes_dict.items():
            print("{}: {}".format(k, v))
        return

if __name__ == '__main__':
    parse_data()

