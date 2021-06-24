#!/usr/bin/python3

def validUTF8(data):

    if len(data) == 0:
       return True
    if len(data) == 1:
        if data[0] >= 32 and data[0] <= 126:
            return True
        else:
            return False
    for num in data:
        if num > 31 and num < 127:
            continue
        else:
            return False

    return True
