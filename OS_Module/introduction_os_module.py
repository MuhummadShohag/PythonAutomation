'''
    OS_Module: This module is used to work/interact with operating system to automate many more task
    like creating directory, removing directory, identifying current directory and many more

    * You can work both operating system through os_module

'''
import os

# os.sep is the (or a most common) pathname separator ('/' or '\\') 
print(os.sep)

# When you taken path to your folder, you set also two lashes('\')
# path="path"
# print(path)

# os.getcwd(), it is show current working directory
print(os.getcwd())

# os.chdir(), it is changing directory
# print(os.chdir("path"))
# print(os.getcwd())

# os.listdir(), it is show list of directory
# print(os.listdir())
# print(os.listdir("path"))

# os.mkdir(), it is create new directory
# print(os.mkdir('good'))

# os.makedirs(), it is create new directory through recursive way
# print(os.makedirs("path"))

# print(os.listdir("path"))

# os.rmdir(), it is remove directory, os.remove(), it is remove file 
# print(os.rmdir("path"))

# os.rename(src,), it is rename file name
# print(os.makedirs("path"))
# a="path"
# b="path"
# print(os.rename(a,b))
# print(os.listdir())

# os.environ, to get enviroment of your operating system
# print(os.environ)

# os.getpid(), you can find process id
# print(os.getpid())

# print(os.remove("path"))
print(os.listdir())
os.system('cls')



