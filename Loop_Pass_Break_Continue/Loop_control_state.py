'''
    * Loop Control Statement:
        1.Break ==> it is useful to stop of our iteration in our loop
        2.Continue ==> It is skip the remaining line in the iteration
        3.Pass ==> it is simply does nothing, while continue goes on with the next loop iteration.

'''
# ===== Break =======
# When you set break after print, it is just do 1 interate
for each in [3,4,5,9,1]:
    print(each)
    break

for each in [3,4,5,9,1]:
    if each == 5:
        break
    print(each)
    

a = ['a','b','c']
for i in a:
    if i == 'b':
        break
    print(i)

value = 0
while True:
    if value == 10:
        break
    print(value)
    value += 1


#==== Continue ======
for i in a:
    if i == 'b':
        continue
    print(i)

value = 0
while value <= 10:
    if value != 7:
        print(value)
    value += 1


#=== Pass ============
if True:
    pass

for i in range(10):
    pass