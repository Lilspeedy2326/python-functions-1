def guess_number(target):
    num = -1
    while target != num:
        num = int(input("guess a number"))
        if num == target:
            print("you guessed right!")
        elif num > target:
            print("too hight!")
        else:
            print("too low!")
            
guess_number(42)
