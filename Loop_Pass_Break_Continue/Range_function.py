'''
    * range(): 
        -- It is a build in function
        -- it is generates integers as a list
    * Syntax:
        range(start,stop,step)
        3-argument ==> by default start = 0, step = 1

'''
print(range(5))
print(list(range(5)))

# start value 0, stop value 5 
print(list(range(0,5)))

# start value 0, stop value 5 and step is a 1
print(list(range(0,10,1)))

# start value 0, stop value 10 and step is 1
print(list(range(0,10,1)))

# start value a 30, stop value a 1 and step is a -1(Right to Left)
print(list(range(30,1,-2)))

# start value a -20, stop value a -2 and step is a -2(Left to Right)
print(list(range(-2,-20,-2)))

# Even Number
print(list(range(0,20,2)))

# Even Number Negative
print(list(range(0,-20,-2)))

my_list = [1,2,3,4,'ok',5]
print(range(len(my_list)))

for i in list(range(len(my_list))):
    print(f"Index ==> {i}")

print("-----------------")

for i in range(len(my_list)):
    print(f"Index is {i} ==> Value is {my_list[i]}")

