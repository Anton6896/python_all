

def subgen():
    x = 'ready to accept message'
    message = yield x
    print(f'subgen received {message}')


class SomeException(Exception):
    pass


"""
python -i my_coroutine.py
>>> g = subgen()
>>> g.send(None) <- must have an None as start value

"""

def average_in():
    my_count = 0
    my_sum = 0
    my_average = None

    while True:
        try:
            x = yield my_average
        except Exception:
            print('reg exception')
        
        # g.throw(SomeException)
        except SomeException:
            print('some data -------------')

        else:
            my_count += 1
            my_sum += x
            my_average = round(my_sum / my_count, 2)
