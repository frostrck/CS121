

def add_one_and_multiply(a, x):
    """ Add 1 to a, and multiply by x"""

    
    # Replace "None" with the correct expression
    r = (a+1)*x

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return r


def within_range(x, lb, ub):
    """ Is x strictly between lb and ub?"""

    ### EXERCISE 2 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    r = (x > lb) and (x<ub)

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return r


def number_string(x):
    """
    Given a number x, produce a string: "POSITIVE", "NEGATIVE", "ZERO"
    (depending on whether the number is positive, negative, or zero)
    """

    ### EXERCISE 3 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable s should contain the value
    # we ask you to compute in this exercise.
    s = None
    if x > 0:
        s="POSITIVE"
    elif x == 0:
        s="ZERO"
    else: 
        s="NEGATIVE"
    ### DO NOT MODIFY THE FOLLOWING LINE!
    return s


def num_divisible(lb, ub, p, q):
    """
    How many numbers between lb and ub (inclusive)
    are divisible by both p and q?
    """

    ### EXERCISE 4 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise.
    n = 0
    for x in range(lb, ub+1):
        if (x % p == 0) and (x % q == 0):
            n +=1

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return n 


def count_negative(lst):
    """
    Count the number of negative numbers in the list
    """

    ### EXERCISE 5 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise.
    n = 0
    for x in lst:
        if x < 0:
            n += 1

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return n


def negate_list(lst):
    """
    Produce a *new* list with its values negated
    """

    ### EXERCISE 6 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise
    new_lst = []
    for x in lst:
        new_lst.append(-1*x)
    ### DO NOT MODIFY THE FOLLOWING LINE!
    return new_lst
