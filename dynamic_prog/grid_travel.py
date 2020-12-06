
def gt(r, c) -> int:
    # count the ways to travel in griad (top left -> down right)
    # the regular recursio -> time O(2^(n+m))
    if r == 1 and c == 1:
        return 1
    elif r == 0 or c == 0:
        return 0

    # count the sum of choises
    return gt(r-1, c) + gt(r, c-1)


def gt_plus(r, c, memo={}) -> int:
    # time -> O(n*m)
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
    # print(f'the regular tester {gt(3,3)}')
    # print(f'the regular tester {gt(2,2)}')
    # print(f'the regular tester {gt(1,1)}')

    print(f'the memo way tester {gt_plus(2,2)}')
    print(f'the memo way tester {gt_plus(5,4)}')
    print(f'the memo way tester {gt_plus(18,18)}')
