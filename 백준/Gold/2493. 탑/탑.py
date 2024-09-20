# 탑
# 골드 V
import sys; input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))

ans = [0] * N
stack = [] # 높이 비교할 탑 넣을 stack

for i in range(N):
    while stack:
        # 스택에는 i 이전의 탑들의 정보 (인덱스, 높이) 가 저장되어 있다.
        # 현재 i 값에 해당하는 탑의 높이가 스택에 마지막에 담은 탑의 높이보다 낮거나 같은 경우
        # 전파를 받을 수 있다.
        if tops[i] <= stack[-1][1]:
            ans[i] = stack[-1][0] + 1 # 해당 탑의 인덱스 + 1 값으로 할당
            break # while문을 빠져나온다
        
        # 이전에 담은 탑들과 높이를 비교해보면서
        # 나보다 낮은 탑은 스택에서 빼버린다
        else:
            stack.pop()
    
    # 스택이 비어있는 경우 탑의 인덱스, 탑의 높이를 stack에 추가한다
    stack.append((i, tops[i]))

print(*ans)