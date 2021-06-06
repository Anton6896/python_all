"""
bubble sort in place
"""


def bubble_sort(arr: list):
    n = len(arr)

    for i in range(n):
        # if go thru list without swapping means that list is ordered
        swapped = False
        # for each iteration -1 from total items
        # bubble will push highest to end
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    my_list = [10, 2, 4, 1, 45, 7, 23]
    bubble_sort(my_list)
    print(my_list)
