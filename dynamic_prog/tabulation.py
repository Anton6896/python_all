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


# -------------------------    grid traveler

def grid_traveler(x: int, y: int) -> int:
    # how many ways to path thru the greed

    # check if numbers are different
    

    grid = [[0 for x in range(x+2)]
            for y in range(y+2)]  # 2d arr x*y filled by 0  (+2 for place safety )
    grid[1][1] = 1

    for j in range(0, y+1):
        for i in range(0, x+1):
            grid[i+1][j] += grid[i][j]
            grid[i][j+1] += grid[i][j]

    return grid[x][y]


if __name__ == "__main__":
    print(f"fibionachi ::  6 : {fib(6)}")
    print(f"fibionachi ::  50 : {fib(50)}")
    print()

    print(f"grid ::  ways to end : {grid_traveler(3,2)}")
    print(f"grid ::  ways to end : {grid_traveler(18,18)}")
