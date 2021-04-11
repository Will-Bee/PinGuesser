from random import randint as r
from time import time
from itertools import count as c
# Imports

# Set Variables

def main(passwd, length):
    MaxNum = 10 ** length
    i = 1
    t1 = round(time() * 1000)
    if passwd >= MaxNum:
        print("No way")
        print("Debug: pin =", passwd)
        print("How many numbers:", length)
        exit()
    for i in c(start=1):
        x = r(0, MaxNum)
        print(i, "Pokusů   ", length, "Počet čísel", "   ", "Pin:", x)
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
    main(123, 4)
