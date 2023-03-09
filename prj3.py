                                 # snake,water,Game

import random

options = ["s","w","g"]

your_points = 0
my_points = 0
choice = 10
chance = 0

while(chance<10):
    your_choice=input(("<<enter your weapon for play>>>\n :s-snake, w = water, g=gun\n"))
    choice = random.choice(options)

    if your_choice=='s' and choice=='w':
        print("snake drink water:you win >> increase 1 point <<")
        your_points=your_points+1
        print("your_points=",your_points)
        print("mypoints",my_points)
        print("round lest:" ,9-chance)
        chance= chance+1

    elif your_choice == 's' and choice == 's':
        print("you got two snakes: dra match!")
        #my_points = my_points + 1
        print("your_points=", your_points)
        print("my points",my_points)
        print("round lest:", 9-chance )
        chance= chance + 1

    elif your_choice == 's' and choice == 'g':
        print("snake get shot by the gun:you lose chee chee chee !")
        my_points = my_points + 1
        print("your_points=", your_points)
        print("my points", my_points)
        print("round lest:", 9 - chance)
        chance = chance + 1

    elif your_choice == 'g' and choice == 'w':
        print("the gun drops in water..you lose!")
        my_points = my_points + 1
        print("your_points=", your_points)
        print("my points", my_points)
        print("round lest:", 9 - chance)
        chance = chance + 1

    elif your_choice == 'g' and choice == 'g':
        print("match draw!\n")
        my_points = my_points + 1
        print("your_points=", your_points)
        print("my points", my_points)
        print("round lest:", 9 -chance)
        chance= chance+ 1

    elif your_choice == 'w' and choice == 's':
        print("i drink your water:you lose chee chee chee!")
        my_points = my_points + 1
        print("your_points=", your_points)
        print("my points", my_points)
        print("round lest:", 9 - chance)
        chance = chance + 1

    elif your_choice == 'w' and choice == 'g':
        print("you drown my gun: you win")
        your_points = my_points + 1
        print("your_points=", your_points)
        print("my points", my_points)
        print("round lest:", 9 - chance)
        chance = chance + 1

    elif your_choice == 'w' and choice == 'w':
        print("lots of water : its draw")
        my_points = my_points + 1
        print("your_points=", my_points)
        print("my points", my_points)
        print("round lest:", 9 - chance)
        chance = chance + 1

    else:
        print("")
        print("your points:",your_points,"my_points",my_points)

    if your_points>my_points:
            print("you winn..you get award!..\n")
    elif my_points>your_points:
            print("you loose:>>[try again(,~~,)]<<\n")
    elif your_points==my_points:
            print("it match was draw TRY AGAIN \n")
    elif choice==chance:
            print("GAME OVER")
            quit()


# computer and snake
