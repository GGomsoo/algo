T = int(input())

for _ in range(T):
    N, C = map(int, input().split())

    temp = N % C

    if temp:
        print(N//C + 1)
    else:
        print(N//C)