'''
    ***Any operating system, Path is always a 'String'
'''
import os
import sys

#=========== Find all files in a directory with required extension .py/.sh/.log/.txt etc ==============

req_path = input("Enter Your Directory Path: ") 

if os.path.exists(req_path):
    if os.path.isfile(req_path):
        print(f"{req_path} is a your desire file path")
    else:
        adf = os.listdir(req_path)
        if len(adf) == 0:
            print(f"The given path is {req_path} is an empty path")
        else:
            req_extension = input("Enter Your Desire File Extension (.py/.sh/.txt): ")
            req_file = []
            for each_file in adf:
                if each_file.endswith(req_extension):
                    req_file.append(each_file)
                if len(req_file) == 0:
                    print(f"There are no {req_extension} files in the location of {req_path}")
                else:
                    print(f"There are {len(req_file)} files in the location of {req_path} with an given extension of {req_extension}")
                    print(f"So, the files are {req_file}")
                    for each_cf in req_file:
                        print(os.path.join(req_path,each_cf))
else:
    print("Please Enter Valid Directory Path")

#======== Read a path and check if given path is a file or a directory ==============
path = input("Enter Your Path: ")
if os.path.exists(path):
    if os.path.isfile(path):
        print(f"The {path} is a File")
    else:
        print(f"The {path} is a Directory")
else:
    print("Enter Your Correct Path")


#========= Read a Directory path and identify all files and directory =====================

input_path = input("Enter Your Directory: ")

if os.path.exists(input_path):
    d = os.listdir(input_path)
else:
    print("Please Enter Your Valid Path")
    sys.exit()

all_file_dir = d
print(f"This is all File and Directory Under Your Path: {all_file_dir}")
for e_f_d in all_file_dir:
    all_f_d = os.path.join(input_path,e_f_d)
    if os.path.isfile(all_f_d):
        print(f"{all_f_d} is a file path")
    else:
       print(f"{all_f_d} is a directory path")

 
#========== Read a string and print chars and their index values ===============================
'''
    ***One way
    user_str = input("Enter Your String: ")
    a= list(enumerate(list(user_str)))
    for i,s in a:
    print(f"{s} ==> {i}")

    ***Second way
    for i in range(len(user_str)):
    print(f"{user_str[i]} ==> {i} ")

'''
user_str = input("Enter Your String: ")
index = 0
for i in user_str:
    print(f"{i} ==> {index}")
    index = index + 1



                
                
    

