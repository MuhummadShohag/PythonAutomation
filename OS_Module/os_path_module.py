'''
    * os.path is a sub module of os
    * os.path module is used to work on path
'''

import os

# all list of os path function and variable
# print(dir(os.path))

# os.path.sep, it is seperate of your operating system
# print(os.path.sep)

# create new file
path="path"
'''
    with open('good.txt','w') as fb:
        pass
        fb.write("New File Create")

    print(os.listdir(path))

'''
# os.path.basename(path) ,it is basename of your path
# print(os.path.basename(path))

# os.path.dirname(path) ,it is directory name of your path, it is importing, when installing package
# print(os.path.dirname(path))

# os.path.join(), it is join two path
path1="path"
path2="path"
print(os.path.join(path1,path2))

# os.path.split(path), it split path, result are basename and director name into tuple
# print(os.path.split(path))

# os.path.getsize(path), it is show your path size in bytes
print(os.path.getsize(path))

# os.path.exits(path), it return Boolean value, it is exit or not on your operating system
if os.path.exists(path):
    print("Your file is there")
else:
    print(f"{path} is not present on the host")

# os.path.isfile(path), it return Boolean value, file exit or not on your operating system
if os.path.isfile(path):
    print("Your file is there")
else:
    print(f"File is not present on the host")

# os.path.isdir(path), it return Boolean value, directory exit or not on your operating system
if os.path.isdir(path):
    print("Your Directory is there")
else:
    print(f"Directory is not present on the host")


print(os.listdir())

