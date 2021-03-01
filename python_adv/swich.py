
# basic if
def switch_regular(operation, x, y):
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    else:
        return None


# new great switch
def switch_good(operation, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
    }.get(operation, lambda: 'no option')()  # <- all as a function


if '__main__' == __name__:
    print(switch_regular('add', 2, 3))
    print(switch_good('add', 2, 3))

