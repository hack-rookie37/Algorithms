#Coin change minimum BackTracking

import time

def minimum_coins(coin_list, change): #coinlist = 코인 유닛(종류)이 담긴 list, change = 잔액
    min_coins = change # 1로 지불하는 경우를 min으로 초기화.
    #print('node: ', change)
    if change in coin_list: # 만약 코인의 종류 중에 잔액과 동일한 것이 있으면
        return 1, [change] # 1개로 지불할 수 있고, 해당 코인을 기록하기 위해 cl[]로 반환. 
    else:
        cl = [] # 어떤 코인을 썼는지 기록할 list.
        for coin in coin_list: # coin_list를 순회하면서 backtracking 시작.
            if coin < change: # 잔액보다 작은 종류의 coin을 사용해야 하므로
                mt, t = minimum_coins(coin_list, change - coin) # a
                num_coins = 1 + mt # num_coins는 아래 노드에서 사용된 코인 개수 + 1
                if num_coins < min_coins: # 최소의 코인 수보다 작다면
                    min_coins = num_coins # min_coins를 더 작은 것으로 갱신
                    cl = t + [coin] # 그리고 사용된 coin 종류들 list에 갱신
    return min_coins, cl # 최소 코인수와, 사용된 coin 종류를 return

print("Minimum Coin Change V1.0 - BT")

while True:
    print("\n--To quit - CTRL + C--\n")
    
    #user input
    unit = input("Enter the Coin Unit\n")
    unit = unit.split()
    coin_list = [int(i) for i in unit]
    #coin_list.sort(reverse = True)
    change = int(input("Enter the Total Change\n"))

    ##Start
    start_time = time.time()
    min, c = minimum_coins(coin_list, change) # min = 최소 코인 개수, c = 사용된 코인 list

    #dictionary
    unit = {}
    for i in coin_list: # key = i, value = count(i)
        unit[i] = c.count(i) # ex unit = {x: a, y: b, z: c} // (x, y, z) = units, (a, b, c) = # of coins each

    ##print##
    print("Answer: You need ", end='')
    for key, value in unit.items():
        print("%s %s's" % (value, key), end='') # value key's // ex) 2 1's
        if list(unit.keys())[-1] == key: # 마지막 key라면 . 찍고 줄바꿈
            print(". ")
            break
        else:
            print(", ", end='') # 마지막 key가 아니라면 , 찍고 줄 바꾸지 않음
            continue
    print("필요한 총 동전 개수는 %s개 입니다." % min)
    print("Running time is %s sec(s)" % (time.time() - start_time))