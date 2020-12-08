

def one(arr: list, target: int) -> bool:  # brute force
    # if it passible to generate some number
    # by using an given array
    # assuming num > 0 in arr
    if target == 0:
        return True
    elif target < 0:
        return False

    for i in arr:
        r_target: int = target - i
        # looking for one time True
        if one(arr, r_target):
            return True

    return False


def mem_one(arr: list, target: int, memo={}) -> bool:  # memozing
    # O(arr*target) -> time
    # O(target) -> space
    if target in memo:
        return memo[target]
    elif target == 0:
        return True
    elif target < 0:
        return False

    for i in arr:
        r_target = target - i
        if mem_one(arr, r_target, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


def get_options(target: int, arr: list) -> list:
    # time : O(target^arr * arr)
    if target == 0:
        return []
    elif target < 0:
        return None

    for i in arr:
        target_r = target - i
        option = get_options(target_r, arr)
        if option != None:
            option.append(i)
            return option

    return None


def get_options_memo(target: int, arr: list, memo={}) -> list:
    # time : O(target * arr)
    if target in memo:
        return memo[target]
    elif target == 0:
        return []
    elif target < 0:
        return None

    for i in arr:
        target_r = target - i

        option = get_options_memo(target_r, arr, memo)
        if option != None:
            memo[target] = option.append(i)
            return memo[target]

    memo[target] = None
    return None


if __name__ == "__main__":
    # print(f"find sum : {one([2, 4], 7)}")  # false
    # print(f"find sum : {one([5, 3, 4, 7], 7)}")  # true
    # print(f"find sum : {one([7, 14], 300)}") # False (too match time)
    print(f"find sum : {mem_one([7, 14], 301)}")  # true
    print(f"find sum : {mem_one([5, 3, 4, 7], 7)}")  # true
    print()
    print(f'arr : {get_options(7, [2,3])}')  # ok
    print(f'arr : {get_options(7, [5,3,4,7])}')  # ok
    print(f'arr : {get_options(7, [2,4])}')  # None
    print()
    print(f'mem arr : {get_options_memo(7, [5,3,4,7])}')
    print(f'mem arr : {get_options_memo(7, [2,3])}')
    print(f'mem arr : {get_options_memo(301, [7,14])}')
