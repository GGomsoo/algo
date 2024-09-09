T = int(input())

for i in range(1, T+1):
    total = 0
    for a in list(map(int, input().split())):
        if a % 2 != 0:
            total += a
    print(f'#{i}', total)