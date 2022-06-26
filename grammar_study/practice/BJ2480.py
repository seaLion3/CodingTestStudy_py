def prizeOutPut(): 
    dice_lst = list(map(int, input().split()))
    lenOfSet = len(set(dice_lst))
    if lenOfSet == 1:
        print(10000 + dice_lst[0] * 1000)
    elif lenOfSet == 2:
        dice_lst.sort()
        print( 1000 + dice_lst[1] * 100)
    else:
        print( max(dice_lst) * 100 )


prizeOutPut()
