# 오큰수
# 골드 IV
import sys; input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

## 정답은 나오지만 시간초과
# for i in range(N):
#     stack = []
#     for j in range(i, N):
#         if A[i] < A[j]:
#             stack.append(A[j])
    
#     if stack:
#         print(stack[0], end=" ")
#     else:
#         print(-1, end=" ")

NGE = [-1] * N # 오큰수 리스트
stack = [0] # stack에서 idx 관리. 0부터 시작

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]: # 스택에 값이 있고, 스택의 오른쪽부터 탐색.
        # 스택값을 idx로 사용하는 값보다 i를 idx로 사용하는 값이 더 크다면
        NGE[stack.pop()] = A[i] # 오큰수에 stack.pop의 값을 idx로 사용, 해당 값을 할당.
    
    stack.append(i) # 위 while 조건 해당하지 않다면, stack에 idx로 삼을 i값을 추가

print(*NGE) # 오큰수 배열을 언패킹하여 출력