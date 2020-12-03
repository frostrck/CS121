from tree import Tree


def sum_cubes(n):
    """
    Recursively calculates the sum of the first n
    positive cubes.

    Input:
        n: positive integer.
    
    Returns: (integer) the value of the sum
        1^3 + 2^3 + ... + n^3
    
    This function may not use any loops or list
    comprehensions.
    """

    if n==1:
        return 1
    elif n >= 1:
        return n ** 3 + sum_cubes(n - 1)


def sublists(lst):
    """
    Computes all sublists of the input list.

    Input:
        lst: list of values
    
    Returns: (list of list of values) list of all
        sublists of lst.
    """

    if lst == []:
        return [[]]

    sub = []
    first = lst[0] 
    small_sub = sublists(lst[1:])
    sub = sub + small_sub

    for item in small_sub:
        sub.append([first] + item) 
    
    return sub

    


def min_depth_leaf(tree):
    """
    Computes the minimum depth of a leaf in the tree
    (length of shortest path from the root to a leaf).

    Input:
        tree: a Tree instance.
    
    Returns: (integer) the minimum depth of of a leaf
        in tree.
    """
    
    min_depth = []

    if tree.num_children() == 0:
        return 0
    
    for child in tree.children:
        min_depth.append(min_depth_leaf(child))
    
    return min(min_depth) + 1 



def repeated_value(tree):
    """
    Determines whether there is a node in the input
    tree that has an ancestor with the same value.

    Input:
        tree: a Tree instance.
    
    Returns: a boolean indicating whether there is a 
    node in the tree that has an ancestor with the 
    same value.
    """
    
    ancestor_values = set()
    repeated_value_r(tree, ancestor_values)


def repeated_value_r(tree, ancestor_values):
    """
    Helper function for repeated_value. Takes in a tree
    which may be a subtree of the original tree of
    interest, and determines if there is a node in the 
    input tree that has an ancestor in the original tree
    with the same value.

    Inputs:
        tree: a Tree instance, which may be a subtree of
            of the original tree.
        ancestor_values: the set of values of nodes in
            the original tree that are ancestors of the
            input tree.
    
    Returns: a boolean indicating whether there is a node
        in the input tree that has an ancestor in the
        original tree with the same value.
    """
    
    if tree.num_children() == 0:
        if tree.value in ancestor_values:
            return True
        else:
            return False
    
    
    for child in tree.children:
        if child.value in ancestor_values:
            return True
        ancestor_values.add(tree.value)
        if repeated_value_r(child, ancestor_values):
            return True

    return False







    
