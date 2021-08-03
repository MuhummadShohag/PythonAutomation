'''
    Why Loops:
        -- All programming languages need a way to execute block of code many times, this is possible
           with loops.
    Python has two types of loops:
            1. For Loop
            2. While Loop
    For Loop:
        --- The for loop in python is used to iterate over a sequence (list, tuple, string) or other iterable objects      
    
    While Loop:
        --- While loop is used to execute a block of statements repeatedly until a given a condition is satisfied.

    ***Loops: Execute a block of code many times
    ***Beacuse of this loop, whatever the line you have under your loop, those line ( print("ok" ) will repeat some certain number of times again and again imediately,
       how many number of times your loop is going to repeat ,it is depend how many values is here like [1,2,3,4,5]
    
    *** Same theory work tuple, string, dictionary and any other iterable objects
    *** 1 Iteration: whatever the line you have under your loop, if those line repeating one ,it called 1 iteration 
    Example:
        for i in [1,2,3,4,5]:
            print("ok")

'''
'''
    my_list = [1,2,3,'ok',5] 
    print(my_list[0])
    print(my_list[1])
    print(my_list[2])
    print(my_list[3])
    print(my_list[4])
    *** Instead of this suiation, loop work properly
'''
my_list = [1,2,3,'ok',5] 
for i in my_list:
    print(i)



#================== For Loop doing work with String =========================
for i in "working with for loop":
    print(i)
    print("string")

my_string = "working with for loop"
'''
    * One Way:
        print("\n".join(my_string))

'''
for i in my_string:
    print(i)


#==================  For Loop doing work with List ===============================
for i in [1,2,3,4,5]:
    print("string")

my_list = [1,2,3,4,5]
for i in my_list:
    print(i)

my_lists = [1,2,3,4,5,6,7,8,9,10]
for i in my_lists:
    if i%2==0:
        print(f"{i} is a even number")
    else:
        print(f"{i} is a odd number")

my_list = [(1,2),(4,5),(6,7)]
for i in my_list:
    print(i)

my_list = [[1,2],[4,5],(6,7)]
for i,v in my_list:
    print(f" First item {i} and Second Item {v}")

print("--------------")

#==================== For Loop doing work with Tuple ==========================
for i in (1,2,3,4):
    print("tuple")

my_list = [(1,2),(4,5),(6,7)]
for i,v in my_list:
    print(f" First item {i} and Second Item {v}")

print("--------------")
#================= For Loop doing work with Dictionary ======================

# Dictionary Only keys
my_dic = {0:1,1:2,2:3}
print(my_dic.keys())

# Dictionary Only Values
print(my_dic.values())

print("--------------")
for k,v in {0:1,1:2,2:3}.items():
    print(f"Dictionary Key is {k} ====> Dictionary Value is {v} ")

print("--------------")
my_dic = {0:1,1:2,2:3}
for k, v in my_dic.items():
     print(f"Dictionary Key is {k} ====> Dictionary Value is {v} ")


