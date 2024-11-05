N = int(input())

buildings = []
for _ in range(N):
    b = int(input())
    buildings.append(b)

stack = []
cnt = 0
for b in buildings:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)
    
    cnt += len(stack)-1

print(cnt)