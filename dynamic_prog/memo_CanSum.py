

def one(arr: list, target: int) -> bool:  # brut force
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


def mem_one(arr: list, target: int, memo={}):  # memozing
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


if __name__ == "__main__":

    # print(f"find sum : {one([2, 4], 7)}")           # false
    # print(f"find sum : {one([5, 3, 4, 7], 7)}")     # true
    # print(f"find sum : {one([2, 3], 7)}")           # true
    print(f"find sum : {mem_one([7, 14], 300)}")           # False
