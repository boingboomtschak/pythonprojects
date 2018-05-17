board1 =[1,2,3,4,5,6]
board2 =["!","@","$","@","$","!"]
guess = input("what would you like to guess?")
for item in board1:
    if int(guess) == item:
        print(board2[item-1])
    else:
        print(item)
guess2 = input("what number does it match?")
if board2[guess-1] == board2[guess2-1]:
    print("win")
else:
    print("loss")