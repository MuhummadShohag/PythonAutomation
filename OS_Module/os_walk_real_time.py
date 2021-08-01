#================ How to do a system wide search for a file? =======================

import os
import platform
import string

'''
    req_input=input("Enter Your File Name: ")
    path=path

    for r,d,f in os.walk(path):
        if len(f) != 0:
            for each_file in f:
                if each_file == req_input: 
                    print(os.path.join(r,each_file))  

    # For Linux System
    for r,d,f in os.walk("/"):
        if len(f) != 0:
            for each_file in f:
                if each_file == request_input:
                    print(os.path.join(r,each_file))

'''
request_input = input("Enter Your File Name: ")

if platform.system() == "Windows":
    posiible_dayo = string.ascii_lowercase
    valid_dayo=[]
    for a in posiible_dayo:
        if os.path.exists(a+":\\"):
            valid_dayo.append(a+":\\")
    print(valid_dayo)

    for each_dayo in valid_dayo:
        for r,d,f in os.walk(each_dayo):
            for each_file in f:
                if each_file == request_input:
                    print(os.path.join(r,each_file))
else:
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file == request_input:
                print(os.path.join(r,each_file))

