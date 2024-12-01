N = int(input())
ans = 1

while True:
    if N == 0:
        print(ans)
        break

    ans *= N
    N -= 1