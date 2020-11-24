import time

memo = [] # 메모에 활용할 list


def bu(N):
    global memo

    memo[1] = 0 
    seq = [[0], [1]] # 노드 시퀀스 메모 list
    min_val = [] # 최소 노드 시퀀스

    for n in range(2, N+1):
        memo[n] = memo[n-1] + 1 # C(N) = C(N-1) + 1
        min_val = seq[n-1] + [n] # 위의 점화식에 따른 노드 기록

        if n % 3 == 0: # 만약 3으로 나눠지는 수라면
            if memo[n//3]+1 < memo[n]: # C(N//3) + 1 <= C(N-1) + 1
                memo[n] = memo[n//3]+1 # 최소 값 갱신
                min_val = seq[n//3] + [n] # 그에 따른 최소 노드 시퀀스 갱신

        if n % 2 == 0: # 만약 2로 나눠지는 수라면
            if memo[n//2]+1 < memo[n]: # C(N//2) + 1 <= C(N-1) + 1
                memo[n] = memo[n//2]+1 # 최소 값 갱신
                min_val = seq[n//2] + [n] # 그에 따른 최소 노드 시퀀스 갱신
        seq.append(min_val) # 최종 최소 노드 시퀀스를 seq에 append
    seq = seq[-1] # 마지막 seq item 추출
    seq.reverse() # 내림차순으로 정렬하기 위해 역순으로 배치
    return memo[N], seq


def main():
    global memo
    print('Bottom-up Algorithm')
    n = int(input('> Enter a natural number\n'))
    start = time.time()
    memo = [0 for _ in range(n+1)]  # 0으로 n+1 길이만큼 초기화. 0번째 인덱스는 사용하지 않음.
    min_num, seq = bu(n)
    end = time.time()
    print('> minimum number of operation is', min_num)
    print('> Operation sequence is', seq)
    print("> Operation time:", end - start)
    input('> press any key to exit')

main()
