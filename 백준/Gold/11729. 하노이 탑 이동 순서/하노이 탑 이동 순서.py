# 하노이 탑 이동 순서
# 골드 V
'''
N = 2 인 경우
장대 상황은 아래와 같음
1
2   _   _
1번 장대 순서 그대로 3번으로 옮기려면 순서가 다음과 같음
(1, 2 -> 1번원판 이동) -> (1, 3 -> 2번원판 이동) -> (2, 3 -> 1번원판 이동 == 완성)
N = 1 -> 장대에 원판이 하나뿐이다. -> 이동 시키자
'''
N = int(input())
K = 0
ans = []

def hanoi(n, start, end): # 원판 개수(층수), 시작 장대 번호, 끝 장대 번호
    global K
    K += 1 # 이동 횟수
    if n == 1: # 장대에 원판이 하나 뿐이다
        ans.append((start, end)) # 이동한다
        return # 다른 장대를 살펴보러 가자
    
    else: # 장대에 원판이 하나가 아닌 경우
        hanoi(n-1, start, 6-(start+end)) # 개수(층수)가 1이 될 때 까지 재귀
        ans.append((start, end)) # 맨 위 원판을 이동시킨 후, return 으로 돌아왔을 때 해당 원판도 이동시킨다
        hanoi(n-1, 6-(start+end), end) # 이후 다시 재귀 진행

hanoi(N, 1, 3)

print(K)
for a in ans:
    print(*a)