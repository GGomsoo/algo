# 쇠막대기
# 실버 II

bar = input()
stack = []
result = 0

for i in range(len(bar)):
    if bar[i] == "(":
        stack.append(bar[i])
    else:
        stack.pop()
        if bar[i-1] == "(":
            result += len(stack)
        else:
            result += 1

print(result)