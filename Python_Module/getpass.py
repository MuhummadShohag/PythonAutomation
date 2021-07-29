'''

    How to use GetPass module in a script?
        *First import GetPass module using below synstax:
            -import getpass 
                or
            -import getpass as gp
                or 
            - from getpass immport *
                or
            -- from getpass immport getpass,getuser

    getpass(): prompts the user for a password without echoing.The getpass module
            provide a secure way to handle the password prompts where programme interect the users
            via the terminal
    getuser(): function display the login name of the user.This functions check the environment
    variables LOGNAME, USER, LNAME AND USERNAME, in order to the value of the first non-empty string.
    How to list all functions and varibales of a any modules?       
        -- By (Dir(module))

'''
import getpass

# print(help(getpass))
print(dir(getpass))
db_pass=getpass.getpass()
print(f'Enter Your Passworld: {db_pass}')

db_user=getpass.getuser()
print(f'Your Operating System Name is: {db_user}')
