
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
    }.get(operation, lambda: None)


