#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
print("*************************************\n\n")
n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
print("*************************************\n\n")
n = 21
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
print("*************************************\n\n")
n = 19170307
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
print("*************************************\n\n")
#n = 30
#print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 2147483640
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
