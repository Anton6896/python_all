#  fibionachi by using tabulation

def fib(n: int) -> int:
    # O(n) <- time and place

    #  +2 for safety
    arr = [0 for x in range(n+1)]
    arr[1] = 1

    for i in range(0, n):
        if (i+1 <= n):
            arr[i+1] += arr[i]
        if (i+2 <= n):
            arr[i+2] += arr[i]

    return arr[n]


# -------------------------    grid traveler

def grid_traveler(x: int, y: int) -> int:
    # how many ways to path thru the greed

    # 2d arr x*y filled by 0  (+2 for place safety )
    grid = [[0 for x in range(x+2)]
            for y in range(y+2)]  

    grid[1][1] = 1

    for j in range(0, y+1):
        for i in range(0, x+1):
            if (i+1 <= x):
                grid[i+1][j] += grid[i][j]
            if (j+1 <= y):
                grid[i][j+1] += grid[i][j]

    # for i in grid:
    #     print(i)

    return grid[x][y]


if __name__ == "__main__":
    print(f"fibionachi ::  6 : {fib(6)}")
    print(f"fibionachi ::  50 : {fib(50)}")
    print()

    print(f"grid ::  ways to end : {grid_traveler(2,3)}")
    print(f"grid ::  ways to end : {grid_traveler(18,18)}")
