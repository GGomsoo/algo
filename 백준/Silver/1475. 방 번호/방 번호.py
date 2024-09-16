# 방 번호
# 실버 V
N = input()

# 0번부터 9번까지의 방 번호 플라스틱
room_num_set = [0] * 10

# 필요한 플라스틱 숫자가 몇개인지 갯수 누적
for i in N:
    room_num_set[int(i)] += 1

# 6과 9는 서로 대체가 가능한 숫자다.
total_6_9 = room_num_set[6] + room_num_set[9]
room_num_set[6] = room_num_set[9] = (total_6_9 + 1) // 2

print(max(room_num_set))