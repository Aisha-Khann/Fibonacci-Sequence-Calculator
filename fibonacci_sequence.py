# This is the starter template for the week 1 participation assignment

#problem 1
# Input n: integer
# constraints: n > 0
# Output: nth Fibonacci number
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |    1    |     0    |
# |---------|----------|
# |    5    |     3    |
# |---------|----------|
# |   20    |   4181   |
# |---------|----------|
def fibonacciRecursive( n ):
    if  n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2) # return nth Fibonacci number

# test the fibonacciRecursive function
print(fibonacciRecursive(1))  # Output: 0
print(fibonacciRecursive(5))  # Output: 3
print(fibonacciRecursive(20)) # Output: 4181


#problem 2
# Input n: integer
# constraints: n > 0, no recursion in implementation
# Output: nth Fibonacci number
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |    1    |     0    |
# |---------|----------|
# |    5    |     3    |
# |---------|----------|
# |   20    |   4181   |
# |---------|----------|
def fibonacciIterative(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    count = 2

    while count < n:
        a, b = b, a + b
        count += 1

    return b # return nth Fibonacci number

# test the fibonacciIterative function
print(fibonacciIterative(1))  # Output: 0
print(fibonacciIterative(5))  # Output: 3
print(fibonacciIterative(20)) # Output: 4181
