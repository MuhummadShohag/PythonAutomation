'''
    *** Sys.argv: returns a list of command line arguments passed to a python script.

'''
# Importing sys module
import sys

#print(sys.argv)

# if you want to see get script name
#print(sys.argv[0])

'''

    user_str=input("Enter your string: ")
    user_action=input("Enter your action on your string( Valid actions are: lower/upper/title: ")

    if user_action == 'lower':
        print(f'{user_str.lower()}')
    elif user_action == 'upper':
        print(f'{user_str.upper()}')
    elif user_action == 'title':
        print(f'{user_str.title()}')
    else:
        print('Please Enter your action on your valid string')

'''



if len(sys.argv) != 3:
    print('Usage: ')
    print(f'{sys.argv[0]}<Your_Require_String><lower/upper/title>')
    sys.exit()

user_str=sys.argv[1]
user_action=sys.argv[2]

if user_action == 'lower':
    print(f'{user_str.lower()}')
elif user_action == 'upper':
    print(f'{user_str.upper()}')
elif user_action == 'title':
    print(f'{user_str.title()}')
else:
    print('Please Enter your action on your valid string')


'''
    Your Comand line display:
        ** if you enter this way command:python sys_argv.py "python"
            Result:
                Usage:
                sys_argv.py<Your_Require_String><lower/upper/title>

        ** if you enter this way command:python sys_argv.py "python" title
            Result:
                Python  

'''

