'''
    * List is immutuble, you can modify
    * Modifing Oparation can not do with print

'''

# List Data Structure Store Multiple Data

# Empty List Always Showed False Boolean 
'''

    bool(empty_list) ==> False
    bool(non_empty_list) ==> True

'''
my_list=[]
print(bool(my_list))

my_list=[3,2,4,"python",5.6]

# if you want to length of list
print(len(my_list))

# First output
print(my_list[0])

#Fourt Value
print(my_list[4])

# Last Value
print(my_list[-1])

# Last Second Value
print(my_list[-2])

# If you want to this position with second value
print(my_list[3][1])

# If You Want To Entire Result
print(my_list)
print(my_list[:])
print(my_list[0:])

# Three more value
print(my_list[1:4])

# Assign Value beacuse of list is immutuble
my_list[0]=45
print(my_list)

print(dir(my_list))


a=[2,2,3,4,5,6,7,8]

# it is showed index number
print(my_list.index(2))
print(a.index(2,1))

# How Many Value Into List
print(a.count(2))

# clear of List; Modifing Oparation can not do with print
a.clear()

my_new_list=a #
my_one_list=a.copy() # Other memory location will be create id()--> Address location

print(id(a),id(my_new_list))
print(id(my_one_list))

# Adding someting ending position
a.append(56)
print(a)

# Adding Data base on index position
a.insert(1,45)

my_list=[5,6]
my_list.append(my_list)# it is add with list way

# it is adding value way without list way
my_list.extend(my_list)

# Removing Data from list
a.remove(2)
print(a)

# Removing Last data by default but if you data deleted with position
a.pop(0)

print(a.pop())

# it is sorting with descending order
a.reverse()
print(a)
# it is sorting with aescending order
a.sort()
print(a)














