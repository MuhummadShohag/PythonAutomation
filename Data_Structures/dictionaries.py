
'''
    * Dictionary is immutable, you can change or modify data

'''
my_dict={}
print(my_dict,type(my_dict))
print(bool(my_dict))

my_dict={'fruit':'apple','animal':'cat',1:1,2:'two'}
print(my_dict)

print(my_dict['fruit'])
print(my_dict['animal'])

# When do not find key, it is raise of error
print(my_dict[1])

# it is not raise error
print(my_dict.get(2))

# it is clear all key value representation data
my_dict.clear()


my_dict=my_dict
print(my_dict)
# assign data
my_dict['three']=3
print(my_dict)

# if is availbe in dictonary that time it is update your old value dictionary
my_dict['three']=56
print(my_dict)

my_dict.clear()

my_dict['three']=56
my_dict['two']=2
print(my_dict)
# it is taken list of keys and values
print(my_dict.keys())
print(my_dict.values())

# you can see key and value one time
print(my_dict.items())

y=my_dict.copy()
print(id(y),id(my_dict))

# Update dictionary
my_new_dic={'four':4}
my_dict.update(my_new_dic)
print(my_dict)

# Remove key value dictionary
my_dict.pop('four')
print(my_dict)

# Remove ramdomly  key value dictionary
my_dict.popitem()
print(my_dict)

keys=['a','b','c','d','e']
new_dict=dict.fromkeys(keys)
print(new_dict)

new_dict['a']=1
print(new_dict)

# Set dafult value in dictionary which default way show if is not define in dictionary
new_dict.setdefault('f',2)
print(new_dict)






