def printIncreasingPower(x):
    # code here
    i = 1

    # Loop to jump in powers of 2
    while(i * i <= x):

        print(i * i, end=" ")

        i += 1