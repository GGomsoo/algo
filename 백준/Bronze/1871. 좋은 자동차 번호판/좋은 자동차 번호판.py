# 좋은 자동차 번호판 - 마라톤 문제
# 브론즈 II

T = int(input())
for _ in range(T):
    car_number = input()
    front_number = car_number.split("-")[0]
    back_number = int(car_number.split("-")[1])

    int_front_number = (ord(front_number[0])-65) * (26**2) + (ord(front_number[1])-65) * (26**1) + (ord(front_number[2])-65) * (26**0)
    # print(int_front_number)
    result = abs(int_front_number - back_number)
    # print(result)

    if result <= 100:
        print("nice")
    else:
        print("not nice")