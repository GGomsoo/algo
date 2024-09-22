seven = input()
num_seven = int(seven)

if "7" not in seven and num_seven % 7 != 0: # 7 포함 X, 7로 나누어 떨어지지도 않음
    print(0)

elif "7" not in seven and num_seven % 7 == 0: # 7 포함 X, 7로 나누어 떨어짐
    print(1)

elif "7" in seven and num_seven % 7 != 0: # 7 포함 O, 7로 나누어 떨어지지 않음
    print(2)

elif "7" in seven and num_seven % 7 == 0: # 7 포함 O, 7로 나누어 떨어짐
    print(3)