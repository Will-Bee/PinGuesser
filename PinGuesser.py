from random import randint as r
from time import time
# Imports

# Set Variables

def main(passwd, howManyNumbers):
    length = 10 ** howManyNumbers
    i = 1
    t1 = round(time() * 1000)
    if passwd >= length:
        print("No way")
        print("Debug: pin =", passwd)
        print("How many numbers:", howManyNumbers)
        exit()
    while True:
        x,i = r(0, length), i + 1
        print(i, "Pokusů   ", howManyNumbers, "Čísel / Čísla", "   ", "Pin:", x)
        if x == passwd:
            print("Pin is guessed:", x)
            t2 = round(time() * 1000)
            t = t2 - t1
            print((t2 - t1) / 1000, "sekund")
            print(i, "pokusů")
            exit()


# Main function


if __name__ == "__main__":
    main(497627, 6)