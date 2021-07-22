#What is variable
'''
    A variable is nothing but a reserved memory location to store values.
    In other words a variable ina program gives data to the comuputer work on.
'''
#How declare and use a variable?
'''
    1.No need to declare variables before using them
    2.Don't write quotes around the varibale name
'''

a=10
b=10
result=a+b
print(f"{result} is a Addition of {a} and {b}")

x=4 
print(x)

y=5.5
print(y)

# you can not mension data type beacuse python is dynamic type language, it is automatic allow about this.

print(type(x))
print(type(y))

'''
    Re-Declare a Varibale?
    x=10
    print(x)
    x=15
    print(x)

    Delete a Varibale?
    del varible
'''

x=10
print(x)
x=15
print(x)

del x

'''
    # Rules to define a varibale names?
    1. its contains letters, numbers and underscore
    2.it should not a keywords
    3.can not caontain space
    4.it should not start with a number
    5.it is case sensative
'''
sojib="good"
print(sojib)
sojib1="good"
print(sojib1)
_sojib="Good"
print(_sojib)

# if, is look like letter but it is keyword


'''
   if=10
   print(if)
'''

'''
   sojib 1="Good"
   print(sojib 1)
'''

'''
   1sojib="Good"
   print(1sojib)

'''

x=30
print(x)

X=10
print(X)

#------------------------------------------------------Data Type-------------------------------------------------------------------------

x=5
print(id(x)) # Id x is variable memory location....

'''
    *Every Value in python has a data type e.p string, int, complex etc
    Since everything is an opps, data types are actually classes and variables are instance of these classes, 
    There are different kind of python data types

    Basic Data Types are:
    1.Numbers(int,float and complex)
    2.Strings
    3.Boalean

'''
x=3
y=5.6
z=3+6j
print(x)
print(y)
print(z)

x=3;y=5.6;z=3+6j
print(x)
print(y)
print(z)

x=3
y=5.6
z=3+6j
print(x,type(x))
print(y,type(y))
print(z,type(z))

lan_name="Python Script" # if it is a string must have write inside with quotation.
print(lan_name)

'''
my_name=Shohag ----shohag is not varible it is data so must have write inside with quotation.
print(my_name)

'''

my_name='Shohag'
print(my_name)

my_value=True # it is look like boolean
print(my_value,type(my_value))
'''
    my_values=true ---it is look like variable

'''

'''
    *** Any data type can be converted into boolean
        Boolean(any_data_type)=True or False
        =====================================
        bool(empty)=False==>bool(0),bool(None),bool([]),bool(()),bool({})
        bool(non-empty)=True
        ==============================================================
        Any data type can be converted into a string but reverse is not always true
'''

x=5.6
print(str(x))

print(bool(()))

x="2.1.2.5" # try to define your version always String
print(type(x))

'''print(int(x))--- you can not converted into number'''

x='5'
print(int(x))


            #=====Wroking with Multiple Variable and String in Print====#

x=5;y=5.6;lan_name="pyrhon _scripting"# One Way
print(x,y,lan_name)

print("{} {} {}".format(x,y,lan_name))

print("{} \n{} \n{}".format(x,y,lan_name))

print("{} \n{} \n{}".format(x,lan_name,y))

print(f"It is X {x} \nIt is Y{y} \nIt is Language Name{lan_name}") # It is best Way to Define

a=f"It is X {x} \nIt is Y{y} \nIt is Language Name{lan_name}"
print(a)

#=========================Input and output Syntax=================================

# Simple Addition Cal

'''
    a=2
    b=3
    result=a+b
    print(f"The addition of {a} and {b} is : {result}")
    ----Always output Same but i want to change calculation the way i innput 

'''

a=int(input("Enter A Value: "))# ---Always Output Data Type is String
b=int(input("Enter B Value: "))
result=a+b
print(f"The addition of {a} and {b} is : {result}")
print(f"The addition of {a} and {b} is : {type(result)}")

a=eval(input("Enter A Value: ")) # Always output whatever you want but if you enter just string value it is not working so you have to input "string" this way
b=eval(input("Enter B Value: "))# Recommanded
result=a+b
print(f"The addition of {a} and {b} is : {result}")
print(f"The addition of {a} and {b} is : {type(result)}")























