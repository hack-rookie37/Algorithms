import time

'''
recurrence relation
R(N) = min{ R(N//3), R(N//2), R(N-1) } + 1
'''
def recursion(N):
	if N == 1: #base case
		return 0, [1]
	min_val = N # 최소 연산 회수는 N을 -1번 하는 횟수
	mod_two = N // 2 # 2로 나누고 소수부분은 버림
	mod_three = N // 3 # 3으로 나눔 소수부분은 버림
	
	if N % 3 != 0:
		mod_three = 0 # 3으로 나눠 떨어지는 수가 아니라면 0 할당
	
	if N % 2 != 0:
		mod_two = 0 # 2으로 나눠 떨어지는 수가 아니라면 0 할당
		
	parameters = (mod_three, mod_two, N-1) # 재귀함수식에 전달할 parameter 튜플
	
	for para in parameters:
		if para == 0: # 파라미터가 0이면 함수 호출하지 않음
			continue
		value, at = recursion(para)
		value += 1
		if value < min_val: # 최소값 보다 value가 더 작으면
			min_val = value # 새로운 최소값 설정
			arr = [N] + at # 현재 노드와 하위 노드 리스트
	
	return min_val, arr # 최소값과 노드 리스트

def main():
    print('Recursion Algorithm')
    n = int(input('> Enter a natural number\n'))
    start = time.time()
    min_num, seq = recursion(n)
    end = time.time()
    print('> minimum number of operation is', min_num)
    print('> Operation sequence is', seq)
    print("> Operation time:", end - start)
    input('> press any key to exit')
    
main()