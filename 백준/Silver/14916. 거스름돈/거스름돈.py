# 거스름돈
# 실버 V

N = int(input())
cnt = 0

# 손님이 2원과 5원짜리로만 거슬러달라고 한다.
# 최소 동전 개수를 구하라.
# 거슬러줄 수 없는 경우 -1을 출력한다.

while N > 0:
    if N == 1:
        cnt = -1
        break

    if N % 5 == 0:
        cnt += N // 5
        break

    else:
        N -= 2
        cnt += 1

print(cnt)