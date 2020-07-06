"""
Here is the one and only "Fibonacci sequence"
where the result of the current number is the sum of the previous 2

"""

# Fibonacci:


def fib(n):

    if n == 0:
        result = 0

    elif (n == 1) or (n == 2):
        result = 1

    # this step calls fib for the previous two elements
    else:
        result = fib(n-1) + fib(n-2)

    return result


# Memoization: runs above algorithm, with a notebook writting
#              down every result from fib(n) up to fib(n-1)


def fib2(n, memo):

    if memo[n]:
        return memo[n]

    elif n == 0:
        result = 0

    elif (n == 1) or (n == 2):
        result = 1

    else:
        result = fib(n-1) + fib(n-2)

    memo[n] = result

    return result


def memo(n):
    memo = [None] * (n + 1)
    return fib2(n, memo)


def fib_bottom_up(n):
    if n == 0:
        return 0
    elif (n == 1) or (n == 2):
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]
