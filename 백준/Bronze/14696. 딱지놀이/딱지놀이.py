# 딱지놀이
# 브론즈 I
# 별 4 / 동그라미 3 / 네모 2 / 세모 1

N = int(input()) # 게임 라운드 수
for _ in range(N):
    temp_A = list(map(int, input().split())) # A 딱지의 그림 갯수, 그림정보
    temp_B = list(map(int, input().split())) # B 딱지의 그림 갯수, 그림정보

    A = temp_A[1:] # A의 딱지
    B = temp_B[1:] # B의 딱지

    for i in range(4, 0, -1): # 4부터 1까지 역순으로 for문 진행
        if A.count(i) > B.count(i): # 그림 i의 갯수가 A가 더 많은 경우
            print("A")
            break
        elif A.count(i) < B.count(i): # B가 더 많은 경우
            print("B")
            break
        elif i == 1: # for문 끝까지 반복했을 때, 다 같은 경우는 무승부
            print("D")