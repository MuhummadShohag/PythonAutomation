'''
    *Introduction to sys module:
        -- The sys module provides functions and variables used to manipulate 
            different part of the python runtime environment.
    
    *How to use sys module?
        -- import sys
    
    *How to get help on sys module?
        -- dir(sys), help(sys)

'''
# Importing sys module
import sys

# To show documentation about sys module
# print(help(sys))

# To see list about sys module
print(dir(sys))

# To see python platform
print(sys.platform)

# To see python environment details
print(sys.version)
print(sys.version_info) # with tuple way you can see

# To see how many modules you are importing to run python script
print(sys.modules) 

# To geeting list of path, it is environment varibale for python
print(sys.path)

# To stop your runtime python environment or stop python script 
# sys.exit()

# sys.exit(2)--> if you want to return code, by default 0





