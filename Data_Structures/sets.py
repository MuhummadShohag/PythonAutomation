'''
    *Sets is unique data structure beacuse sets store data unique
    * Ascending order result, Unorder collection of data

'''
# Duplicated data is not store data
my_set={1,2,3,4,5,5}
print(my_set)

my_sets=set({})
print(my_sets,type(my_sets))
print(bool(my_sets))

a={1,2,3,4,5}
b={6,7,8,9,10}

# Adding two sets
b=a.union(b)
print(b)
print(dir(b))

# Adding sets value
b.add(11)
print(b)

# Substructed two sets
z=b.difference(a)
print(z)

# Showed unique value return
g=a.intersection(z)
print(g)
