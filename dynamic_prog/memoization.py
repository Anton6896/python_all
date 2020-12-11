
"""
well the recept is make this work in recursion tree 
and then adjust memoization as optimization way 
"""


def fib(n: int) -> int:
    # the regular approach
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def fib_2(n: int, memo=dict()) -> int:
    # * this way to do tree lookup
    # * by using memoization decreasing the time complexity
    if n in memo:  # look for keys
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib_2(n-1, memo) + fib_2(n-2, memo)
    return memo[n]


def gt(r, c) -> int:
    # count the ways to travel in grid (top left -> down right)
    # the regular recursion -> time O(2^(n+m))
    if r == 1 and c == 1:
        return 1
    elif r == 0 or c == 0:
        return 0
    # count the sum of choices
    return gt(r-1, c) + gt(r, c-1)


def gt_plus(r, c, memo={}) -> int:
    # time  -> O(n*m)
    # space -> O(n+m)
    key_1 = str(r)+','+str(c)
    if key_1 in memo:
        return memo[key_1]

    if r == 1 and c == 1:
        return 1
    elif r == 0 or c == 0:
        return 0

    memo[key_1] = gt_plus(r-1, c, memo) + gt_plus(r, c-1, memo)
    return memo[key_1]


if __name__ == "__main__":
    print(f"fibonacci : {fib_2(6)}")

    # print(f'the regular tester {gt(3,3)}')
    # print(f'the regular tester {gt(2,2)}')
    # print(f'the regular tester {gt(1,1)}')

    print(f'the memo way tester {gt_plus(2,2)}')
    print(f'the memo way tester {gt_plus(5,4)}')
    print(f'the memo way tester {gt_plus(18,18)}')