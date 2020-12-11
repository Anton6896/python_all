#  fibionachi by using tabulation

def fib(n: int) -> int:
    # O(n) <- time and place

    #  +2 for safety
    arr = [0 for x in range(n+2)]
    arr[1] = 1

    for i in range(0, n):
        arr[i+1] += arr[i]
        arr[i+2] += arr[i]

    return arr[n]


def grid_traveler(m: int, n: int) -> int:
    # how many ways to path thru the greed 
    
    pass


if __name__ == "__main__":
    print(f"fibionachi 6 : {fib(6)}")
    print(f"fibionachi 50 : {fib(50)}")
