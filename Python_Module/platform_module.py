'''
    How to use platform module in a script?
        *First import platform module using below synstax:
            -import platform 
                or
            -import platform as pt
                or 
            - from platform immport *
                or
            -- from platform immport architecture, machine
    How to list all functions and varibales of a any modules?       
        -- By (Dir(module))
'''
import platform as pt

# list of operation into platfrom
print(dir(pt))

# Your Computer Architecture
print(pt.architecture())

# Your Computer Machine
print(pt.machine())


# Your Computer System
print(f'This is {pt.system()} os')

# Your Computer Release
print(f'This release is Windows: {pt.release()}')

# Your Computer Processor
print(f'This release is Windows: {pt.processor()}')

# Your Computer information by one function
print(f'This release is Windows: {pt.uname()}')

# Python Version
print(f'Ptyhon Version is: {pt.python_version()}')

# Python Version getting with tuple
print(f'Ptyhon Version is: {pt.python_version_tuple()}')



