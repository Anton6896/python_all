
# walrus
def my_walrus():
    food = []
    # while True:
    #     type_ = input('enter food : ')
    #     if type_ == 'exit':
    #         break
    #     food.append(type_)

    while (type_ := input('enter food: ')) != 'exit':
        food.append(type_)
    print(food)

    # nums = []
    # while (num := input('enter num: ')).isdigit():
    #     nums.append(num)
    
    # print(nums)
    
    

if __name__ == '__main__':
    my_walrus()
