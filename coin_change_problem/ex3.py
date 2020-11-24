#Coin change minimum DP (top-down)

import time

dp = []
gcl = []
min_depth = 0 # 최적 경로의 depth를 기록한다. 초기 값은 0 (루트 노드의 깊이는 0)

def minimum_coins(coin_list, change, depth):
    global dp, gcl, min_depth
    depth += 1 # 현재 노드의 깊이는 부모 노드의 깊이 + 1
    min_coins = change
    #print('node: ', change, 'depth: ', depth, 'min_depth: ', min_depth)
    if change in coin_list:
        dp[change - 1] = 1
        min_depth = depth # 최초의 경로를 찾아서 리프 노드에 닿았을 경우 이를 min으로 기록.
        return 1, [change] 
    else:
        cl = []
        if dp[change - 1] <= change:
            return dp[change - 1], gcl[change - 1]
        for coin in coin_list:
            if min_depth != 0 and depth >= min_depth: # 분기한정. 탐색을 진행하기 전, 현재 노드의 깊이가 min보다 크거나 같다면 더 이상 하위노드 탐색을 하지 않는다.
                break
            if coin < change: 
                mt, t = minimum_coins(coin_list, change - coin, depth)
                num_coins = 1 + mt 
                if num_coins <= min_coins: 
                    min_coins = num_coins
                    cl = t + [coin]
                    gcl[change - 1] = cl
        dp[change - 1] = min_coins
    return min_coins, cl

print("Minimum Coin Change V2.1 - DP&BB")


while True:
    
    print("\n--To quit - CTRL + C--\n")

    unit = input("Enter the Coin Unit\n")
    unit = unit.split()
    coin_list = [int(i) for i in unit]
    coin_list.sort(reverse = True)
    change = int(input("Enter the Total Change\n"))

    ##Start
    start_time = time.time()
    dp = [change + 1 for _ in range(change)]
    gcl = [ []  for _ in range(change)]
    depth = -1
    min, c = minimum_coins(coin_list, change, depth)


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
    print(dp)
    #print(dp)
    #print(gcl[-1])
