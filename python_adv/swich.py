# basic if
def switch_regular(operation, x, y):
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    else:
        return None


def printing_name(name):
    print(name)


# new great switch
def switch_good(operation, x=0, y=0):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
    }.get(operation, lambda: 'no option')()  # <- all as a function


if __name__ == '__main__':
    print(switch_good('add', 2, 3))

