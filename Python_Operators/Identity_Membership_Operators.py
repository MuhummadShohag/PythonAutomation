'''
    Identity Operators:
        -- Identity Operators are used to find the type of: Class/type/object.
        -- There are two types of identity operators
            1. is
            2. is not
    Membership Operators:
        -- Membership Operators are used to valid the membership of a value
        -- There are two type membership operators:
            1. in
            2. not in


'''
#================== Identity Operators=================
x=4
y=6
type(x)
type(y)

type(x) == type(y)

c="Hi"
type(c)

# Compare is type of data between two varibale or objects
type(x) is type(y) 

type(x) is not type(c)

#================== Membership Operators =================
a=[1,2,3,4,5]
b=1

print(a in b)

valid_pyhton=['1','1.5','3.5','3.7']
host_python='3.7'

if host_python in valid_pyhton:
    print('Host deployed of valid python version')
elif host_python not in valid_pyhton:
    print('Host is not deployed of valid python version')
else:
    print("Raise Error")

