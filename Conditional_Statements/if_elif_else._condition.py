
#======= Get Title Format ===========
input_str=input("Enter your string: ")
print(input_str)

user_conf=input("Do you want to convert your given string into title format? Say yes or no ")
if user_conf=="yes":
    print(input_str.title())
else:
    print(input_str)

# ======== Find Greater Number ===============

''' 
    a=eval(input("Enter Your First Number: "))
    b=eval(input("Enter Your Second Number: "))

    if a > b:
        print(f"{a} is greater than {b}")
    elif a < b:
        print(f"{a} is less than {b}")
    elif a==b:
        print(f"{a} is the same {b}")

'''

# if expression has three posibilities, you can use 'Else', Else is default block

a=eval(input("Enter Your First Number: "))
b=eval(input("Enter Your Second Number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is the same {b}")
