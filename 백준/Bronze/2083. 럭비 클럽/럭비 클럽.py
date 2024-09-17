# 럭비 클럽
# 브론즈 IV
# 17살 이상 or 80kg 이상 == 성인부(Senior), 나머지 청소년부(Junior)

while True:
    club_user = list(input().split())
    name = club_user[0]
    age = int(club_user[1])
    weight = int(club_user[2])

    if name == "#" and age == 0 and weight == 0:
        break

    if age > 17 or weight >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")