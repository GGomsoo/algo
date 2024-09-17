# 집 주소
# 브론즈 III
# 0은 공간 4, 1은 공간 2, 2~9는 공간 3 차지
# 각 숫자 사이에 여백 1
# 숫자와 호수판 사이에 여백 1
# 마지막 0은 처리X

while True:
    address_num = input()
    if address_num == "0":
        break
    
    blank = len(address_num) + 1
    temp = 0

    for i in address_num:
        num = int(i)

        if num == 1:
            temp += 2
        elif 2 <= num <= 9:
            temp += 3
        else:
            temp += 4
    
    total = blank + temp
    print(total)
