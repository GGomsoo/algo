# 단순한 문제 (Small) - 마라톤 문제
# 브론즈 IV

T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    x = y = z = 1
    result = []

    while (1 <= x <= a) and (1 <= y <= b) and (1 <= z <= c):
        if (x % y) == (y % z) == (z % x):
            result.append((x, y, z))
            x += 1
            y += 1
            z += 1
    
    print(len(result))