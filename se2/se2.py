def is_pythagorean_triple(a, b, c):
    """
    Do a, b, and c form a Pythagorean Triple?

    a, b, c: ints

    Returns: bool
    """
    triple = None
    if a**2 + b**2 == c**2:
        triple = True
    else:
        triple = False
    ### EXERCISE 1 -- Replace pass with your code
    return triple


def characterize_nums(lst):
    """
    Characterize a list by counting the number of negative
    numbers, zeros, and positive numbers.

    lst: list of ints

    Returns: (int, int, int)
    """
    negative = 0
    zero = 0
    positive = 0


    for i in range(len(lst)):
        if lst[i] < 0:
            negative += 1
        elif lst[i] == 0:
            zero += 1
        else:
            positive += 1
    ### EXERCISE 2 -- Replace pass with your code
    return (negative, zero, positive)


def compute_matching(lst1, lst2):
    """
    Given two lists of equal length, compute a list
    that where the ith element is True if the lists
    match at index i.

    lst1, lst2: lists

    Returns: list of bools
    """
    ### Leave this assertion
    assert len(lst1) == len(lst2)

    match = []

    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            match.append(True)
        else: 
            match.append(False)
    ### EXERCISE 3 -- Replace pass with your code
    return match


def compute_matching_indices(lst1, lst2):
    """
    Given two lists of equal length, compute a list that of the
    indices where the two lists have the same value.

    lst1, lst2: lists

    Returns: list of integer indices
    """
    ### Leave this assertion
    assert len(lst1) == len(lst2)

    index = []

    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            index.append(i)
        else:
            pass
    ### EXERCISE 4 -- Replace pass with your code
    return index


def destructive_negate(lst):
    """
    Negate the value of each element in the list *in place*.

    lst: list of ints
    """
    
    for i in range(len(lst)):
        lst[i] = -1 * lst[i]

    ### EXERCISE 5 -- Replace pass with your code
    pass


def win_lose_or_draw(board, row, col):
    """
    Returns "Win", "Lose", or "Draw" depending on whether sum of the 
    values in the row is larger, smaller, or the same as the sum
    of the values in the column

    board: list of lists of ints
    row: int
    col: int

    Returns: string: "Win", "Lose", or "Draw"
    """
    sum_row = 0 
    sum_col = 0
    result = None

    for i in range(len(board[row])):
        sum_row += board[row][i]
        
    for j in range(len(board)):
        sum_col += board[j][col]

    if sum_row > sum_col:
        result = "Win"
    elif sum_row == sum_col:
        result = "Draw"
    else: 
        result = "Lose"
    ### EXERCISE 6 -- Replace pass with your code
    return result
