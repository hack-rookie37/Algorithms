import time

memo = []  # 메모에 활용할 list
node = []  # 노드별 자식 노드 list e.g. [1: [], 2: [1], 3: [1], 4: [2,1], ...]


def td(N):
    global memo, node
    if N == 1:  # base case
        return 0, [1]
    if memo[N-1] != -1:  # memo된 값이 있으면 그 값 return
        return memo[N-1], node[N-1]
    min_val = N  # 최소 연산 회수는 N을 -1번 하는 횟수
    mod_three = N // 3  # 3으로 나눔 소수부분은 버림
    mod_two = N // 2  # 2로 나누고 소수부분은 버림

    if N % 3 != 0:
        mod_three = 0  # 3으로 나눠 떨어지는 수가 아니라면 0 할당

    if N % 2 != 0:
        mod_two = 0  # 2으로 나눠 떨어지는 수가 아니라면 0 할당

    parameters = (mod_three, mod_two, N-1)  # 재귀함수식에 전달할 parameter 튜플
    #parameters = (N-1, mod_two, mod_three)
    arr = []
    for para in parameters:
        if para == 0:  # 파라미터가 0이면 함수 호출하지 않음
            continue
        value, at = td(para)
        value += 1
        if value < min_val:  # 최소값 보다 value가 더 작으면
            min_val = value  # 새로운 최소값 설정
            memo[N-1] = min_val  # 최소값 메모
            arr = [N] + at  # 현재 노드와 하위 노드 리스트
            node[N-1] = arr  # 노드 리스트 메모

    return min_val, arr  # 최소값과 노드리스트


def main():
    global memo, node
    print('Top-Down Algorithm')
    n = int(input('> Enter a natural number (under 1993!)\n'))
    memo = [-1 for _ in range(n)]  # -1은 계산 안됨을 의미함.
    node = [[] for _ in range(n)]  # 빈 리스트 안의 리스트로 초기화
    start = time.time()
    min_num, seq = td(n)
    end = time.time()
    print('> minimum number of operation is', min_num)
    print('> Operation sequence is', seq)
    print("> Operation time:", end - start)
    input('> press any key to exit')


main()
