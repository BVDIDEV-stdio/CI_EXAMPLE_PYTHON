from random import randint

print("RUSSIAN ROULETTE BABY!")

while True:
    print("TYPE 1 TO PLAY OR TYPE 0 TO QUIT")
    response = int(input())
    if response == 1:
        loadedChamber = randint(1, 6)
        readyChamber = randint(1, 6)

        if loadedChamber == readyChamber:
            print("LMAO U DEAD")
            break
        else:
            print("CONGRATULATIONS, YOU SURVIVED")
    elif response == 0:
        break
    else:
        print("AYO WRONG INPUT")
