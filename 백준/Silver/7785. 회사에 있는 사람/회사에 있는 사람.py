# 회사에 있는 사람
# 실버 V

import sys; input = sys.stdin.readline

N = int(input())

employee = dict()

for _ in range(N):
    log = input().split()
    name = log[0]
    commute = log[1]

    if commute == "enter":
        employee[name] = commute
    
    elif commute == "leave":
        employee.pop(name)

result = sorted(employee, reverse=True)
for i in result:
    print(i)