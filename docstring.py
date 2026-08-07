def add(n1,n2):
    """
    This function takes two numbers as input and returns their sum.
    Parameters:
    n1 (int or float): The first number to be added.
    n2 (int or float): The second number to be added.
    Returns:
    int or float: The sum of n1 and n2.
    """
    return n1 + n2

# to print the docstring of the function, you can use the __doc__ attribute of the function. In this case, add.__doc__ will return the docstring of the add function.
print(add.__doc__)   # Output: This function takes two numbers as input and returns their sum.
print(add(5, 10))  # Output: 15
