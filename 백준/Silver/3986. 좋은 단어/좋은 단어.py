# 좋은 단어
# 실버 IV

N = int(input())
result = 0

for _ in range(N):
    word = input()
    stack = []

    for w in word:
        if len(stack) == 0:
            stack.append(w)
        else:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
    
    if len(stack) == 0:
        result += 1

print(result)