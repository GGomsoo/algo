P, K = map(int, input().split())
cnt = 1

while True:
    if P == K:
        print(cnt)
        break
    else:
        if P < K:
            K -= 1
            cnt += 1
        else:
            K += 1
            cnt += 1