# Lambda Function: Write a lambda function that multiplies two numbers.
nums = lambda x, y: x * y
print(nums(2, 3))


# Recursive Function: Write a recursive function that calculates the sum of the first n numbers.
def cal(n):
    if n == 1:
        return 1
    return n + cal(n - 1)


cal(10)


# Variable-Length Arguments: Write a function that accepts any number of arguments and returns their average.
def fun(*args):
    return sum(args) / len(args)

print(f"{fun(1, 2, 3, 4, 234, 4356, 4657):.2f}")
