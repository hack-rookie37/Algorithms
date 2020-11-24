#Coin change minimum DP (top-down)

import time
import os

dp = [] # memoization을 위한 배열, 초기에 -1값으로 세팅된다. 원소의 개수는 change와 같다.
gcl = [] # memoization으로 인해 이미 탐색한 배열의 하위 노드들의 코인정보를 담는 list (global coin list)

def minimum_coins(coin_list, change):
    global dp, gcl # 전역변수
    min_coins = change
    #print('node: ', change)
    if change in coin_list:
        dp[change - 1] = 1 # memoization // ex) dp[4] = 1 # 노드 5의 값을 1로 기록.
        return 1, [change] 
    else:
        cl = []
        if dp[change - 1] != -1: # memo한 값이 존재하면
            return dp[change - 1], gcl[change - 1] # 재귀를 하지 않고 바로 그 값과, 하위 노드의 coin 정보를 담은 list를 return.
        for coin in coin_list:
            if coin < change: 
                mt, t = minimum_coins(coin_list, change - coin)
                num_coins = 1 + mt 
                if num_coins <= min_coins: 
                    min_coins = num_coins
                    cl = t + [coin]
                    gcl[change - 1] = cl # dp에 memo된 값으로 바로 return될 경우에 같이 return할 list. ex) gcl[2] = [1, 1, 1] # 3노드는 1노드 3개 후손으로 가짐.
        dp[change - 1] = min_coins # dp에 min_coin을 memo
    return min_coins, cl

print("Minimum Coin Change V2.0 - DP")


while True:
    print("\n--To quit - CTRL + C--\n")
    
    unit = input("Enter the Coin Unit\n")
    unit = unit.split()
    coin_list = [int(i) for i in unit]
    #coin_list.sort(reverse = True)
    change = int(input("Enter the Total Change\n"))

    ##Start
    start_time = time.time()
    dp = [-1 for _ in range(change)] # memo list를 -1 값으로 change의 개수만큼 set.
    gcl = [None for _ in range(change)] # None으로 chagne 수 만큼 초기화.
    min, c = minimum_coins(coin_list, change)


    unit = {}
    for i in coin_list:
        unit[i] = c.count(i)

    ##print##
    print("Answer: You need ", end='')
    for key, value in unit.items():
        print("%s %s's" % (value, key), end='')
        if list(unit.keys())[-1] == key:
            print(". ")
            break
        else:
            print(", ", end='')
            continue
    print("필요한 총 동전 개수는 %s개 입니다." % min)
    print("Running time is %s sec(s)" % (time.time() - start_time))
