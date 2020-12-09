

# if i can do that at all (do you can concat the word from bank of words)
def can_constract(target: str, arr: list) -> bool:
    if target == '':
        return True

    for word in arr:
        # python way
        if target.startswith(word):
            suffix = target.replace(word, '')
            if can_constract(suffix, arr) == True:
                return True

        # not an python way
        # if target.index(word) == 0:
        #     print(f'index "{word}" yes zero : {target[len(word):]}')

    return False


if __name__ == "__main__":
    print(
        f"can concat : {can_constract('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])}"
    )

    print(
        f"can concat : {can_constract('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])}"
    )

    print(
        f"can concat: {can_constract('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])}"
    )
