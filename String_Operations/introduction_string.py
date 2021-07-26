'''
    *What is String in python?
        -A string is a sequence of characters
        -A charcters is simply a symbol.For example, the english language has 26 characters.
        -Computers do not deal with characters, they deal with numbers(binary).
          Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0 and 1.
        -This conversion of character to a number is called encoding and the reverse process is decoding.ASCIll and unicode are 
         some of the popular encoding used. 

        *In python,string is a sequence of unicode charcter.Unicode was introduced to include every character
          in all language uniformity in encoding
'''
#===========How to create a stringin python===============
a='Shohag'
b="Student"
c="""Univerity Student""" #Not use three single quota like ''' '''.But Use three Double quote Look like """ """ when use multiple line of information

print(f"My name is {a}\nI am a {b}\nI am also {c}")
print("My name is {}\nI am a {}\nI am also {}".format(a, b, c))

#=========== How to access characters in string? =========================

my_str="" # It is empty string
my_new_str=" " # It is one of the character even though it is space into quatation.

print(f"{bool(my_str)} and {bool(my_new_str)}")

my_scrip="Python Scripting"
print(f"{my_scrip}")
print(my_scrip[1:4]) # It is slicing python and it is left to right way
print(my_scrip[-1:-10]) # it is right to left way road
print(my_scrip[-1]) # ending charcter indexing starting -1;

str_o_4=my_scrip[0:5] # 0 to 4 index not 5 beacuse n-1 for last range it is exclude.

#========== How to change or delete a string? ============================
'''
    *String are immutable.This means that elements of a string cannot be changed once 
    it has been assigned.We can simply reassign different strings to the same name
'''
#my_scrip[0]="n" # not working, can not modify
#del my_scrip[0] # not working

# but We can delete entair string
# del my_scrip
#========== Length of the String =========

print(f"{len(my_scrip)}") # range left to right 0 to 15 [0:16], but right to left -1 to -16 [-1:-16]

#========== How to add/Concatenate two strings?==============
a='Shohag'
b="Student"
d=a+" "+b+" "+c
print(d)






