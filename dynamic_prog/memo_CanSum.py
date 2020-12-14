

# * actual question can you do that ( find the number ) =============================


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


def mem_one(arr: list, target: int, memo: dict) -> bool:  # memozing
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


# * question if you can do it show me how you did that ( return list of numbers )  =============================
def get_options(target: int, arr: list) -> list:
    # time : O(arr^target * target)
    # size : O(target^2)
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


def get_options_memo(target: int, arr: list, memo: dict) -> list or None:
    # time O(target^2 * arr)
    if target in memo:
        return memo[target]
    elif target == 0:
        return []
    elif target < 0:
        return None

    for i in arr:
        target_r = target - i
        option = get_options_memo(target_r, arr, memo)  # list 

        if option != None:
            option.append(i)
            memo[target] = option
            return option

    memo[target] = None
    return None


# * optimize the last question (show me the smallest option for this task  )  =============================
def bestSum(target: int, arr: list) -> list:
    # get the smallest arr that in sum return target
    if target == 0:
        return []
    elif target < 0:
        return None

    shortestCombination = None

    for num in arr:
        target_r = target - num
        option = bestSum(target_r, arr)  # put to stack

        if option is not None:  # if option is list
            option.append(num)  # get from stack
            if shortestCombination is None or len(option) < len(shortestCombination):
                shortestCombination = option  # alias

    return shortestCombination


def best_sum_memo(target: int, arr: list, memo: dict) -> list or None:
    # get the smallest arr that in sum return target
    # in this case must use numpy function copy() for deep copy of objects (lists)
    if target in memo:
        if memo[target] is not None:
            return memo[target].copy()
        return memo[target]
    elif target == 0:
        return []
    elif target < 0:
        return None

    shortest_combination = None

    for num in arr:
        target_r = target - num
        option = best_sum_memo(target_r, arr, memo)  # return array

        if option is not None:
            option.append(num)
            # if not exists create, else conpare
            if (shortest_combination is None) or (len(option) < len(shortest_combination)):
                shortest_combination = option.copy()  # deep copy

    if shortest_combination is not None:
        memo[target] = shortest_combination.copy()

    return shortest_combination


if __name__ == "__main__":
    # print(f"find sum : {one([2, 4], 7)}")  # false
    # print(f"find sum : {one([5, 3, 4, 7], 7)}")  # true
    # print(f"find sum : {one([7, 14], 300)}") # False (too match time)
    # print(f"find sum : {mem_one([7, 14], 301, {})}")  # true
    # print(f"find sum : {mem_one([5, 3, 4, 7], 7, {})}")  # true

    # print()
    # print(f'arr : {get_options(7, [2,3])}')  # ok
    # print(f'arr : {get_options(7, [5,3,4,7])}')  # ok
    # print(f'arr : {get_options(7, [2,4])}')  # None

    # print()
    # print(f'mem arr : {get_options_memo(7, [5,3,4,7], {})}')
    print(f'get option memo : {get_options_memo(7, [2,3], {})}')
    # print(f'mem arr : {get_options_memo(301, [7,14], {})}')

    print(f"\nbest sum : {bestSum(7,[5,3,4,7])}")
    print(f"best sum : {bestSum(8,[2,3,5])}")
    print(f"best sum : {bestSum(8,[1,4,5])}")

    print(f"\nbest sum memo: {best_sum_memo(7,[5,3,4,7],{})}")
    print(f"best sum memo: {best_sum_memo(8,[2,3,5],{})}")
    print(f"best sum memo: {best_sum_memo(8,[1,4,5],{})}")
    print(f"best sum memo: {best_sum_memo(100,[1,2,5,25],{})}")

# requirements.txt
