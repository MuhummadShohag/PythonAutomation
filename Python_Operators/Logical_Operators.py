'''
    *Logical Operators are useful to combine multiple conditions

    *There are three type of logical operators:
        1.And => It return True if both conditions is True, if Any one condition is False; Return-False
        2.Or => It return True if anyone conditions is True, if evry condition is False; Return-False
        3.Not => not True ==> False , not False ==> True

    *Working More Add Operators ==> All([And condition])
    *Working More Or Operators ==> Any([Or condition])

'''

#============ Logical Operators ===================

# Combining two And conditions
3>1 and 3>2

# Combining more than two And conditions
3>1 and 3>2 and 5>6

# All look like All And condition
all([3>1 and 3>2 and 5>6])# Working with multiple And Condition


# Combining two Or conditions
3>1 or 3>4

# Combining more than two And conditions
3>1 or 3>2 or 5>4

# Any look like All And condition
any([3>1 or 3>2 or 5>4])# Working with multiple Or Condition

# not True ==> False , not False ==> True
not 3>5
not 3>1 or 3>4 



