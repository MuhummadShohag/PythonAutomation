'''
    *What is a module?
        --A module is a file containing Python definitions and statements. That means module containing
        python functions,classes and variables.

    *What is the use of module?
        --Reusability
    Note: If scripts name is mymodule.py then module name is mymodule

    *Types of Python Modules:
        --Default Modules
        --Third Parthy Modules
    ---- Import either default or third party modules before using them

    ****If you use module affective way, your python script become a nice and shorter and smart
'''
# ==================================== Import Module Different Name===================================

# 1 Way Aproach
import math

# 2 Way Aproach
import math as m

# 3 Way Approach
from math import pow,sin 

# 4 Way Approach 
from math import *

# 5 Way Approach through this way import multiple module
import math,subprocess,shutil

# Import Custome Module
import customeModule
print(customeModule.a)
print(customeModule.b)
# if you want to read document about modules or inforamtion how to use 
print(help(math))

# ====== This way you see list all functions and varibales of a any modules =============
print(dir(math))

print(math.cos(10))
print(math.pi)
print(math.pow(20,2))
print(math.e)
print(math.factorial(5))
print(math.radians(10))
print(math.remainder(10,3))

# if you want to show python default module
print(help('modules'))

# if you want to install module
#===> pip install module_name