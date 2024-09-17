# 부호
# 브론즈 III
# N개 정수 주어지면, 정수들의 합 S의 부호 구하기
import sys; input = sys.stdin.readline

tc = 3
for _ in range(tc):
    N = int(input().strip())

    total = 0
    for _ in range(N):
        num = int(input())
        total += num

    if total == 0:
        print(0)
    elif total > 0:
        print("+")
    else:
        print("-")