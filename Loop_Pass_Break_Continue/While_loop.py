'''
    *While Loop:
        -While loop is used to execute a block of statements repeatedly until a given a condition is satisfied.
        
        -The while loop in python is used to iterate over a block of code as long as the test expression (condition) is true
        -We generally use this loop when we do not know beforehand, the number of times to iterate
'''
import time

# If you want to print infinity number of times
# while True:
while False:
    print("ok")

# while True:
while False:
    print("Monitoring file system usage")
    time.sleep(1)

value = 4
while value <= 20:
    print(value)
    value = value+3

count_value = 0
while count_value <= 5:
    print(count_value,"ok")
    count_value += 1

