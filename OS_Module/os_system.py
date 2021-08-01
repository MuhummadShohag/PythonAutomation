'''
    * os.system is used to execute os commands
    * if you execute your operating system coomand with python,it is helpful
'''
import os

# if you forget getcwd(), it is helpful os.system('dir'), show your directory and file on your operating system
# print(os.getcwd())
# print(os.system('dir'))
# print(os.system('ls')) --> Linux system

# os.system('cls'), it is clear of your command script
# print(os.system('cls'))
# print(os.system('clear')) --> Linux system

# os.system(date), it show current date 
# dat="date"
# print(os.system(dat))

# os.system() is not store any variable, but if condition way you can do this one
# a=os.system('dir')
if os.system('dir') == 0:
    print("Your Command Successfully Execute")
else:
    print("Your Command is not Successfully Execute")





