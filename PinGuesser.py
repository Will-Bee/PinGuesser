from random import randint as r
from time import time, sleep
from itertools import count as c
from os import system as cmd, name as osname
# Imports



def main(passwd, length, console_output, live_output):
    cmd('cls' if osname == 'nt' else 'clear')

    if console_output == True:
        if live_output == True:
            MaxNum = 10 ** length
            t1 = time()
            for i in c(start=1):
                x = r(0, MaxNum)
                print(i, "Tries   ", length, "Nums lenght", "   ", "Current pin:", x)
                if x == passwd:
                    t2 = time()
                    print("Pin is guessed:", x)
                    t = t2 - t1
                    print(t, "Seconds, with output")
                    print(i, "Tries")
                    return i,t
                    break

        elif live_output == False:
            MaxNum = 10 ** length
            t1 = time()
            for i in c(start=1):
                x = r(0, MaxNum)
                if x == passwd:
                    t2 = time()
                    print("Pin is guessed:", x)
                    t = t2 - t1
                    print(t, "Seconds")
                    print(i, "Tries")
                    return i,t
                    break

    elif console_output == False:
        if live_output == True:
            MaxNum = 10 ** length
            t1 = time()
            for i in c(start=1):
                x = r(0, MaxNum)
                if x == passwd:
                    t2 = time()
                    t = t2 - t1
                    return i,t
                    break

        elif live_output == False:
            MaxNum = 10 ** length
            t1 = time()
            for i in c(start=1):
                x = r(0, MaxNum)
                if x == passwd:
                    t2 = time()
                    t = t2 - t1
                    return i,t
                    break



if __name__ == "__main__":
    main(7332, 4, True, False)
