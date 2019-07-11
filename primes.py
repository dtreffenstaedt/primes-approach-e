#!/bin/python3
import time
import math

def isprime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def calce(currentRow = [2,3,5], rows = 0, nums = 0, num = 7):
    start = time.time()
    print("number of primes: highest prime: current approximation ( relative deviation ) execution time")

    with open("data/fine.dat", "a") as fine: 
        with open("data/backup.dat", "w") as backup: 
            while True:
                num = num + 1
                if isprime(num):
                    l = len(currentRow)
                    if l < 2:
                        currentRow.append(num)
                    elif (num - currentRow[l-1]) <= (currentRow[l-1]-currentRow[l-2]):
                        nums = nums + len(currentRow)
                        rows = rows + 1
                        appr = nums/rows
                        backup.seek(0)
                        backup.write(str(currentRow))
                        backup.write(" ")
                        backup.write(str(rows))
                        backup.write(" ")
                        backup.write(str(nums))
                        backup.write(" ")
                        backup.write(str(num))
                        backup.write("\n")
                        backup.truncate()
                        currentRow = [num]
                        if (rows % 10) == 0:
                            fine.write(str(nums))
                            fine.write(" ")
                            fine.write(str(appr))
                            fine.write("\n")
                            end = time.time()
                            #print("                                                                                                                          ", end='\r')
                            print(str(nums).rjust(10, '0'), ": ", str(num).rjust(15, '0'), ": ", str(appr).ljust(20, '0'), " (", str(abs(appr-math.exp(1))/math.exp(1)).ljust(25, '0'), ") ", str(end-start)[:5], end='\r')
                    else:
                        currentRow.append(num)

calce()
