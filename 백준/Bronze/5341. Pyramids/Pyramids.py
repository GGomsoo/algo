# Pyramids
# 브론즈 V

# N개의 블록으로 피라미드 바닥 구축
# 다음 층에 N-1 개씩 구축
# 입력 0 들어오면 종료

while True:
    N = int(input())

    if N == 0:
        break

    ans = 0
    for i in range(N, -1, -1):
        ans += i
    
    print(ans)