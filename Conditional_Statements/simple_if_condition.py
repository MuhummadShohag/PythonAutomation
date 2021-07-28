'''
    *If is called simple conditional statement
    *Used to control the execution of set of lines or block of code or line

    if expression:
        statement1
        statement2
    *Expression like: comparision, identity, membership, logical Operators

'''
import os

get_terminal_size=os.get_terminal_size().columns
'''
    *If it is True, you can get output, otherwise it is not excute output

    input_str=input("Enter Your String: ")

    if True:
        print(input_str.center(get_terminal_size).title())
        print(input_str.ljust(get_terminal_size).title())
        print(input_str.rjust(get_terminal_size).title())

    if False:
        print(input_str.center(get_terminal_size).title())
        print(input_str.ljust(get_terminal_size).title())
        print(input_str.rjust(get_terminal_size).title())

'''
input_str=input("Enter Your String: ")
print(input_str)
user_conf=input("Do you want to align text: Say yes or no? ")

if user_conf == 'yes': # it is comparision operator which output is boolean: True/False
    print(input_str.center(get_terminal_size).title())
    print(input_str.ljust(get_terminal_size).title())
    print(input_str.rjust(get_terminal_size).title())


my_even_no=[0,2,4,6,8,10]
user_no=eval(input("Enter Your Number: "))

if user_no in my_even_no: # it is membership operator which output is boolean: True/False
    print("Your given number is my even number")


    



