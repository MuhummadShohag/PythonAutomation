'''
    * Tuple Data Structure is mutuble, you can not modify tuple data

    **Real Work: When you want to change of data any part of list that time use List
        other wise use tuple data beacuse it is mutuble.
'''

my_empty=()
my_tuple=(3,4,5)

# Empty Tuple Always Showed False Boolean 
'''

    bool(empty_tuple) ==> False
    bool(non_empty_tuple) ==> True

'''
print(bool(my_empty))
print(bool(my_tuple))

my_tuple=(3,4,[1,2,3],5,6)
print(my_tuple)

# Getting data with index
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[2][0])


# my_tuple[0]=1 --> you can not modify tuple part of tuple but modify whole tuple

print(dir(my_tuple))

# how many time particular data in here
print(my_tuple.count(3))

# Showed index tuple value
print(my_tuple.index(3))

# if you want to length of tuple 
print(len(my_tuple))

# If you want to entire tuple
print(my_tuple[:])
print(my_tuple)
print(my_tuple[0:])

# Slicing Data

print(my_tuple[:3]) # from 0 to 2
print(my_tuple[-1])

# Anather way tuple

x=2, # x=1,2,3 without comman it is become a interger data
print(x,type(x))