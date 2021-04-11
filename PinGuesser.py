from random import randint as r
from time import time
from itertools import count as c
from os import system as cmd
# Imports


# Set Variables


def main(passwd, length, UI):
    cmd('cls' if os.name == 'nt' else 'clear')
    MaxNum = 10 ** length
    i = 1
    t1 = round(time() * 1000)
    if passwd >= MaxNum:
        print("No way")
        print("Debug: pin =", passwd)
        print("How many numbers:", length)
        exit()
    if UI == True:
        for i in c(start=1):
            x = r(0, MaxNum)
            print(i, "Pokusů   ", length, ": Počet čísel", "   ", "Pin:", x)
            if x == passwd:
                print("Pin is guessed:", x)
                t2 = round(time() * 1000)
                t = t2 - t1
                print(t / 1000, "sekund")
                print(i, "pokusů")
                exit()
    if UI == False:
        print("Guessing...")
        for i in c(start=1):
            x = r(0, MaxNum)
            if x == passwd:
                print("Pin is guessed:", x)
                t2 = round(time() * 1000)
                t = t2 - t1
                print(t / 1000, "sekund")
                print(i, "pokusů")
                exit()


print(c(start=1))


# Main function


if __name__ == "__main__":
    main(123, 4, False)
