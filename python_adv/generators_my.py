# generator practice
# https://www.youtube.com/watch?v=bD05uGo_sVI&ab_channel=CoreySchafer

def square_number(num_list):
    for i in num_list:
        # yield is holding positioin in memory
        # and action to this position
        # but not holding an result
        yield (i*i)


def square_number_tester():
    nums_my = square_number([1, 2, 3, 4, 5])
    # print(next(nums_my))
    # print(next(nums_my))
    # print(next(nums_my))

    print('regular form ', end=': ')
    for num in nums_my:
        print(num, end=", ")
    print()

    print("list form ", end=": ")
    nums_my_2 = [(x*x) for x in [1, 2, 3, 4, 5]]  # list regular
    print(nums_my_2)
    print('advanced way', end=": ")
    nums_my_2 = ((x*x) for x in [1, 2, 3, 4, 5])  # generator

    for n in nums_my_2:
        print(n, end=", ")
    print()


if "__main__" == __name__:
    square_number_tester()
