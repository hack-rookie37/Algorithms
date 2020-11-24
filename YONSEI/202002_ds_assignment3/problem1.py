#import numpy as np
import time
import matplotlib.pyplot as plt

'''
Problem 1
'''
memo = [-1 for _ in range(10000)]

def main():
    
    #Recursion
    '''re = []
    for i in range(1, 70):
        start = time.time()
        #print(i, Recursion(i))
        Recursion(i)
        re.append(time.time() - start)
        #print(time.time() - start)'''

    #print('--------')
    #DP
    dp = []
    for i in range(3000,4000):
        start = time.time()
        #print(i, DP(i))
        DP(i)
        dp.append(time.time() - start)
        #print(time.time() - start)

    index = [i for i in range(3000, 4000)]
    #plt.plot(index, re)
    plt.plot(index, dp)
    #plt.legend(['re','dp'])
    #plt.axis([1,70,0,0.0001])
    plt.show()

# R(N) = R(N-4) + 2R(N-5) + R(N-6) (N >= 8)
# R(8) = R(4) + 2R(3) + R(2)
def Recursion(N):
    #Base cases
    if N <= 2:
        return 0
    elif N <= 5:
        return 1
    elif N <= 7:
        return 2
    
    return Recursion(N-4) + (2 * Recursion(N-5)) + Recursion(N-6)

def DP(N):
    global memo

    #Base cases
    if N <= 2:
        return 0
    elif N <= 5:
        return 1
    elif N <= 7:
        return 2

    if memo[N-1] != -1:
        return memo[N-1]
    
    memo[N-1] = DP(N-4) + (2 * DP(N-5)) + DP(N-6)

    return memo[N-1]

main()

