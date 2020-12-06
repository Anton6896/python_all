
def fib(n: int) -> int:
    #! the regular approach 
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def fib_2(n: int, memo=dict()) -> int:
    #* this way to do tree lookup 
    #* by using memoization decreasing the time complexity
    if n in memo:  # look for keys
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib_2(n-1, memo) + fib_2(n-2, memo)
    return memo[n]


if __name__ == "__main__":
    print(f"fibionaci : {fib_2(100)}")
