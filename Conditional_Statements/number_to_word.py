#============ Number Finding To World Through If Condition ================
'''
    a=eval(input("Enter Your Number: "))
    if a==1:
        print('One')
    if a==2:
        print('Two')
    if a==3:
        print('Three')
    if a==4:
        print("Four")
    if a==5:
        print("Five")
    if a not in [1,2,3,4,5]:
        print("Your given number out of range number.Please Enter number range between 1 to 5")


'''
'''
    a=eval(input("Enter Your Number: "))
    if a==1:
        print('One')
    elif a==2:
        print('Two')
    elif a==3:
        print('Three')
    elif a==4:
        print("Four")
    elif a==5:
        print("Five")
    else:
        print("Your given number out of range number.Please Enter number range between 1 to 5")

'''
range_number=[1,2,3,4,5]
a=eval(input("Enter Your Number: "))
if a in range_number:
    if a == 1:
        print('One')
    elif a == 2:
        print('Two')
    elif a == 3:
        print('Three')
    elif a == 4:
        print("Four")
    else:
        print("Five")
else:
    print("Your given number out of range number.Please Enter number range between 1 to 5")


#======================== The Useful Technique ================
range_number_dict={1:'One',2:'Two',3:'Three',4:'Four',5:'Five'}
input_number=eval(input("Enter Your Desire Number: "))
'''

    if input_number in [1,2,3,4,5]:
        print(range_number_dict.get(input_number))
    else:
        print("Your given number out of range number.Please Enter number range between 1 to 5")

'''
if input_number in range_number_dict.keys():
    print(range_number_dict.values(input_number))
else:
    print("Your given number out of range number.Please Enter number range between 1 to 5")
