# 파티가 끝나고 난 뒤
# 브론즈 IV
# 서로 다른 5개의 신문 보면서, 실제 참가자와 기사에 적힌 참가자 수 비교 후 출력

L, P = map(int, input().split())
participants = list(map(int, input().split()))

for i in range(5):
    remember_sg = L * P
    print(participants[i] - remember_sg, end=" ")