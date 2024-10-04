# 먹을 것인가 먹힐 것인가
# 실버 III

def eating(start, end, target):
    temp = -1 # 초기값 -1
    while start <= end:
        mid = (start + end) // 2

        if target > B[mid]: # 타겟이 B 배열의 중간값보다 큰 경우
            temp = mid # 큰 쌍의 갯수 = mid의 갯수
            start = mid + 1 # 시작점 수정
        else: # 반대의 경우
            end = mid - 1 # 끝점 수적
    
    return temp # return하는 temp의 값은 mid의 idx값

T = int(input())
for _ in range(T):
    N, M = map(int, input().split()) # A의 수, B의 수
    # 입력 받으면서 오름차순으로 정렬한다
    A = sorted(map(int, input().split())) 
    B = sorted(map(int, input().split()))

    cnt = 0 # 큰 쌍의 갯수
    start, end = 0, M-1 # 이분 탐색 시작, 끝

    for num in A: # A 배열의 수들을 하나씩 탐색
        # +1 하는 이유
        # 함수 내 temp의 초기값은 -1
        # 만약 target이 B 배열의 모든 원소보다 값이 작다면 -1을 return 한다
        # target이 B 배열의 원소보다 큰 경우엔, temp에 mid를 할당.
        # 함수는 idx값인 mid를 return 한다.
        # 실제 값은 idx + 1을 더해줘야 한다.
        cnt += eating(0, M-1, num) + 1
    
    print(cnt)