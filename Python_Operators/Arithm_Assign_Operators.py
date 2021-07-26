'''
    * Arithmetic Operators:
        --Addition +
        --Subtraction -
        --Multiplication *
        --Division /
        --Modulo %
        --Floor division //
        --Exponential **
    * Assignment Operators
        -- +=
        -- -=
        -- *=
        -- /=
        -- %=

'''

#===========Arithmetic Operators================

print(4+6)

# Addition Operators
a=10
b=3
result=a+b
print(result)

# Substraction Operators
c=a - b
print(c)

# Multiplication Operators
c=a * b
print(c)

# Division Operators
c=a/b
print(c)

# Modulo Operators result come reminder
c=a % b
print(c)

# Floor Division Operators result without floting Points
c=a // b
print(c)

# Exponential Operators
c=a ** b
print(c)

#===========Assignment Operators================
x=3
x=x+2 # '=' it is assignment operators
print(x)

a=5
b=6
a += b
# a -= b
# a *= b
# a /= b
# a %= b
print(a)


#========== Creating Addition Calculation===========

a=eval(input('Enter First Number: '))
b=eval(input("Enter Second Number: "))
result=a+b

print(f"The Addition of {a} And {b} Is {result}")



