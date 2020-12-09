

# if i can do that at all (do you can concat the word from bank of words)
def can_constract(target: str, arr: list) -> bool:
    if target == '':
        return True

    for word in arr:
        # python way
        if target.startswith(word):
            suffix = target.replace(word, '')  # return new obj

            if can_constract(suffix, arr):
                return True

        # not an python way
        # if target.index(word) == 0:
        #     suffix = target[len(word):]

    return False


def can_constract_memo(target: str, arr: list, memo=dict) -> bool:
    if target in memo:
        return memo[target]
    elif target == '':
        return True

    for word in arr:
        # python way
        if target.startswith(word):  # preffix
            suffix = target.replace(word, '')  # return new obj

            if can_constract_memo(suffix, arr, memo):
                memo[target] = True
                return True

        # not an python way
        # if target.index(word) == 0:
        #     suffix = target[len(word):]

    memo[target] = False
    return False


def count_construct(target: str, arr: list, memo=dict) -> int:
    # return number of possible options to create word
    if target in memo:
        return memo[target]
    elif target == '':
        return 1

    total: int = 0

    for prefix in arr:
        if target.startswith(prefix):
            number: int = count_construct(
                target.replace(prefix, ''), arr, memo)
            total += number

    memo[target] = total
    return total


def all_construct(target: str, arr: list, memo: dict) -> list:
    #* return array 2d of option to concat the word, with catch memo 
    if target in memo:
        return memo[target]
    elif target == '':
        return [[]]

    result: list = []

    for prefix in arr:
        if target.startswith(prefix):
            suffix: str = target.replace(prefix, '')
            alllist: list = all_construct(suffix, arr, memo)  # return [[]]
            # insert preffix to ech array in stack
            list(map(lambda x: x.insert(0, prefix), alllist))
            # spread out array in result ( concatenate array ) -> [1,2] + [3,4] = [1,2,3,4]
            result += alllist

    memo[target] = result
    return result


if __name__ == "__main__":
    # testers

    # print(
    #     f"can concat : {can_constract('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])}"
    # )

    # print(
    #     f"can concat : {can_constract('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])}"
    # )

    # print(
    #     f"can concat: {can_constract('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])}"
    # )

    # print(
    #     f"can concat: {can_constract_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], {})}"
    # )
    # print(
    #     f"can concat : {can_constract_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {})}"
    # )

    # print(
    #     f"total number of ways : {count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], {})}"
    # )

    print("\nreturn an arrays 2d with variation to build the word \n")
    print(
        f"total number of ways : {count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], {})}"
    )

    print(
        f"all construct :\n {all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {})}"
    )

    print(
        f"can concat:\n {all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], {})}"
    )

    print(
        f"all construct :\n {all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], {})}"
    )

    # print("\n\n my test ")
    # myp = [
    #     ['a', 'b'],
    #     ['c', 'd']
    # ]

    # list(map(lambda x: x.insert(0, 't'), myp))
    # print(myp)
