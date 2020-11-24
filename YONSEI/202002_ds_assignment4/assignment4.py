from copy import deepcopy
import pandas as pd
import numpy as np


# Problem 1
########## DO NOT modify ###########
class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next
#####################################


class LinkedList:
    def __init__(self):
        # DO NOT modify __init__() class; No additional class variables are allowed
        self._head = None

    def __str__(self):
        cur = self._head
        str = []
        while cur != None:
            str.append(cur.get_data())
            cur = cur.get_next()
        return '{}'.format(str)

    def add(self, item):
        new_node = Node(data=item)
        new_node.set_next(self._head)
        self._head = new_node

    def erase(self, func):
        cur = self._head
        before = None
        while cur != None:
            if func(cur):
                if cur == self._head:
                    self._head = cur.get_next()
                    del cur
                    cur = self._head
                else:
                    before.set_next(cur.get_next())
                    del cur
                    cur = before.get_next()
            else:
                before = cur
                cur = cur.get_next()

    def search(self, func):
        cur = self._head
        index = 0
        li = []
        while cur != None:
            if func(cur):
                li.append(index)
            cur = cur.get_next()
            index += 1
        return li

    def sort(self, func):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.get_next()

        if count <= 1:
            return

        for i in range(count-1):  # if count == 7, (6) 0...5
            cur = self._head
            before = None
            for _ in range(count-i-1):  # 6 5 4 3 2 1
                if func(cur) > func(cur.get_next()):  # sorting
                    if cur == self._head:
                        self._head = cur.get_next()
                        cur.set_next(self._head.get_next())
                        self._head.set_next(cur)
                        before = self._head
                    else:
                        before.set_next(cur.get_next())
                        cur.set_next(cur.get_next().get_next())
                        before = before.get_next()
                        before.set_next(cur)
                else:
                    before = cur
                    cur = cur.get_next()



#test data
l = LinkedList()

l.add(9)
l.add(3)
l.add(8)
l.add(6)
print(l)

l.erase(lambda x: x.get_data() > 6)
print(l)

l.add(7)
l.add(3)
l.add(9)
l.add(4)
l.add(2)
print(l.search(lambda x: x.get_data() < 4))

def sorting_criterion(x):
    return x.get_data() % 5

l.sort(sorting_criterion)
print(l)


# Problem 2


def sequential_search(search_list, num):
    ret = []
    for i, item in enumerate(search_list):
        if item == num:
            ret.append(i)
    return ret


def binary_search(search_list, num, start=0, end=-1):
    if end == -1:
        end = len(search_list)-1
    if start > end:
        return []
    ret = []
    mid = (start + end) // 2
    if num == search_list[mid]:
        ret.append(mid)
        for i in range(mid-1, -1, -1):
            if search_list[i] == num:
                ret.append(i)
                continue
            else:
                break
        for i in range(mid+1, end+1):
            if search_list[i] == num:
                ret.append(i)
                continue
            else:
                break
    elif num > search_list[mid]:
        ret = binary_search(search_list, num, start=mid+1, end=end)
    else:
        ret = binary_search(search_list, num, start=start, end=mid-1)
    return ret


# test data
search_list = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6]

print(sequential_search(search_list, 5))
print(binary_search(search_list, 3))


def insertion_sort(sort_list, func, sfunc=None, start=0, gap=1):
    for i in range(start+gap, len(sort_list), gap):
        key = sort_list[i]
        j = i
        while j > 0:
            if func(sort_list[j-1]) > func(key):
                sort_list[j] = sort_list[j-1]
                j -= 1
            elif func(sort_list[j-1]) == func(key):
                if sfunc == None:
                    break
                elif sfunc(sort_list[j-1]) < sfunc(key):
                    sort_list[j] = sort_list[j-1]
                    j -= 1
                else:
                    break
            else:
                break
        sort_list[j] = key
        
        
def shell_sort(sort_list, func1, func2):
    gap = len(sort_list) // 2
    while gap > 0:
        for start in range(gap):
            insertion_sort(sort_list, func1, func2, start, gap)
        gap = gap // 2


sort_list = [1, 2, 3, 4, 5, 6]
sort_list2 = [1, 2, 3, 4, 5, 6]

insertion_sort(sort_list, lambda x: x ** 2 - 10 * x)
print(sort_list)
shell_sort(sort_list2, lambda x: x % 2, lambda x: x % 3)
print(sort_list2)

# Problem 3
########## DO NOT modify ###########
class Sorting:
    def __init__(self):
        pass

    def random_list(self, length):
        import random
        arr = []
        for _ in range(length):
            arr.append(random.randint(1, 1000))
        return arr

    def sorting_func(self, x):
        return eval('+'.join(str(x)))
#####################################
    def bunch(self, sort_list, func):  # 같은 item을 nest 시켜주는 함수
        bunch = [sort_list[0]]  # 같은 nest에 첫 번째 값을 넣음.
        new = []  # bunch를 묶어서 새롭게 return 될 list
        j = 0  # bunch가 초기화 될 때 len=0 이 되기 때문에 sort_list의 index와 비교하기 위한 gap 상수
        for i in range(len(sort_list)-1):  # sort_list 끝까지 탐색하는데, i+1까지 가야하므로 길이-1 만큼 loop
            # bunch의 item과 sort_list item의 func output 값이 같으면
            if func(bunch[i-j]) == func(sort_list[i+1]):
                bunch.append(sort_list[i+1])  # 같은 nest로 묶는다
            else:
                new.append(bunch)  # 아니면 현재까지의 bunch를 new list에 추가한다.
                bunch = [sort_list[i+1]]  # 그 다음 값으로 bunch를 초기화한다.
                j = i + 1  # 현재 인덱스를 j에 기억한다.
        new.append(bunch)  # loop가 끝나고 난 뒤 마지막 bunch를 new에 추가한다.
        sort_list = new  # sort_list를 nested된 list인 new로 갱신한다.
        return sort_list  # nested list return

    def bubble_sort(self, sort_list, func):
        if len(sort_list) <= 1:  # list의 길이가 1 미만이면 정렬 안함.
            return sort_list
        for size in reversed(range(len(sort_list))): # 버블정렬은 뒤에서부터 완료된다. 마지막 index가 size이다.
            for i in range(size): # size 만큼 loop를 돌면서 값을 비교한다.
                if func(sort_list[i]) < func(sort_list[i+1]): # func output 비교해서 큰 값을 앞으로
                    # swap
                    sort_list[i], sort_list[i + 1] = sort_list[i+1], sort_list[i]
        sort_list = self.bunch(sort_list, func) # nested list로 만들어준다.
        return sort_list

    def selection_sort(self, sort_list, func):
        if len(sort_list) <= 1: # list의 길이가 1 미만이면 정렬 안함.
            return sort_list
        for size in reversed(range(len(sort_list))): # 한 칸씩 (뒤에서부터 최솟값 찾아서 채움) 정렬이 완성되므로 size를 점점 줄여나간다.
            min_i = 0 # 최솟값 인덱스
            for i in range(1, 1+size): # loop
                if func(sort_list[i]) < func(sort_list[min_i]): # min보다 작은 값이 발견되면
                    min_i = i # min을 최솟값으로 갱신
                # swap
                sort_list[min_i], sort_list[size] = sort_list[size], sort_list[min_i]
        sort_list = self.bunch(sort_list, func) # nested list로 만들어준다.
        return sort_list

    def merge_sort(self, sort_list, func1, func2=None, depth=-1):
        if len(sort_list) <= 1: # list의 길이가 1 미만이면 정렬 안함.
            return sort_list
        depth += 1 # 현재 재귀 깊이
        if len(sort_list) > 1:
            mid = len(sort_list) // 2 # 반으로 분할하기 위한 index
            ll, rr = sort_list[:mid], sort_list[mid:] # list를 mid를 중심으로 ll(왼쪽), rr(오른쪽)로 분할한다.
            self.merge_sort(ll, func1, func2) # ll에 대해 merge sort
            self.merge_sort(rr, func1, func2) # rr에 대해 merge sort

            li, ri, i = 0, 0, 0 # ll index, rr index, sort_list index
            while li < len(ll) and ri < len(rr): # ll과 rr이 각각 마지막 index에 도달하기까지 loop
                if func1(ll[li]) > func1(rr[ri]): # ll list item이 rr list item보다 func output이 크면
                    sort_list[i] = ll[li] # sort_list에 ll의 item을 넣는다.
                    li += 1 # ll index 증가
                elif func1(ll[li]) == func1(rr[ri]):
                    if func2 != None:
                        if func2(ll[li]) > func2(rr[ri]):
                            sort_list[i] = ll[li]
                            li += 1
                        else:
                            sort_list[i] = rr[ri]
                            ri += 1
                else: # 반대면
                    sort_list[i] = rr[ri]  # sort_list에 rr의 item을 넣는다.
                    ri += 1 # rr index 증가
                i += 1 # sort_list index 증가
            sort_list[i:] = ll[li:] if li != len(ll) else rr[ri:] # ll과 rr 중 하나가 마지막 idnex에 도달했으면 그렇지 않은 list로 전부 sort_list를 채움
        
        # 재귀(정렬)이 끝난 root node에서 마지막 return 전에 호출 
        if depth == 0:
            sort_list = self.bunch(sort_list, func1) # nested list로 만들어준다.
        return sort_list

    def quick_sort(self, sort_list, func1, func2=None, depth=-1):
        if len(sort_list) <= 1: # list의 길이가 1 미만이면 정렬 안함.
            return sort_list
        depth += 1 # 현재 재귀 깊이
        pivot = sort_list[len(sort_list) // 2] # 중앙 index를 pivot으로 잡는다.
        less_li, equal_li, great_li = [], [], [] # pivot기준으로 작은, 같은, 큰 list
        for item in sort_list: # sort_list 순회
            if func1(item) < func1(pivot): # item이 pivot보다 작으면 less_li에 append
                less_li.append(item)
            elif func1(item) > func1(pivot): # item이 pivot보다 크면 great_li에 append
                great_li.append(item)
            else:
                if func2 != None:
                    if func2(item) < func1(pivot):
                        less_li.append(item)
                    elif func2(item) > func2(pivot):
                        great_li.append(item)
                equal_li.append(item) # item이 pivot과 같으면 equal_li에 append

        # great + equal + less (내림차순)으로 quick sort 재귀 호출
        sort_list = self.quick_sort(
            great_li, func1, func2, depth) + equal_li + self.quick_sort(less_li, func1, func2, depth)
        # 재귀 함수(하위 노드)에서 return 받은 정렬된 sort_list를 현재 노드의 sort_list에 저장한다.
        
        # 재귀(정렬)이 끝난 root node에서 마지막 return 전에 호출 
        if depth == 0:
            sort_list = self.bunch(sort_list, func1)
        return sort_list

    def compute_sorting_time(self):
        pass

    def sort_medals(self):
        data = pd.read_csv('./medals.csv')
        
        li = data.values.tolist()
        
        self.selection_sort(li, lambda x: x[1]) # Gold
        self.merge_sort(li, lambda x: x[1], lambda x: x[2]) #Sliver
        self.quick_sort(li, lambda x: x[1], lambda x: x[3]) #Bronze
        #print(li) # Gold 1, Sliver 2, Bronze 3
        
        dataframe = pd.DataFrame(li)
        dataframe.to_csv('sorted.csv')
        print(dataframe)
        
        
       
        

s = Sorting()
'''
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
l2, l3, l4 = deepcopy(l1), deepcopy(l1), deepcopy(l1)

print(s.bubble_sort(l1, lambda x: x % 2))

print(s.selection_sort(l2, lambda x: x % 3))

print(s.merge_sort(l3, lambda x: x % 4))

print(s.quick_sort(l4, lambda x: x % 5))
'''
s.sort_medals()

