# 와글와글 숭고한 - 마라톤 문제
# 브론즈 IV

SoongKoHan = list(map(int, input().split()))

if sum(SoongKoHan) >= 100:
    print("OK")
else:
    min_participation = min(SoongKoHan)
    # print(SoongKoHan.index(min_participation))
    if SoongKoHan.index(min_participation) == 0:
        print("Soongsil")
    elif SoongKoHan.index(min_participation) == 1:
        print("Korea")
    else:
        print("Hanyang")