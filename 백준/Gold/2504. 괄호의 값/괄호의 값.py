# 괄호의 값
# 골드 V
# 스택의 마지막 값이 아닌, 이전 괄호에 focus 해야한다...

P = list(input())
stack = []
result = 0
temp = 1

for i in range(len(P)):
    if P[i] == "(":
        stack.append(P[i])
        temp *= 2
    
    elif P[i] == "[":
        stack.append(P[i])
        temp *= 3
    
    elif P[i] == ")":
        if not stack or stack[-1] != "(":
            result = 0
            break

        if P[i-1] == "(":
            result += temp

        stack.pop()
        temp //= 2
    
    elif P[i] == "]":
        if not stack or stack[-1] != "[":
            result = 0
            break

        if P[i-1] == "[":
            result += temp

        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(result)