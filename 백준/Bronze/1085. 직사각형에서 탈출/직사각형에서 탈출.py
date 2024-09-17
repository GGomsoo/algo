# 직사각형에서 탈출
# 브론즈 III

x, y, w, h = map(int, input().split())

# x 좌표 중, 직사각형 경계선까지 가는 최솟값
min_x = min(x, w-x)

# y 좌표 중, 직사각형 경계선까지 가는 최솟값
min_y = min(y, h-y)

# 둘 중 더 가까운
min_result = min(min_x, min_y)

print(min_result)