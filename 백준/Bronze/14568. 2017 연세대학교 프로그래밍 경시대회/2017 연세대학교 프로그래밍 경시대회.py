# 문제2. 사탕 (# 14568)

candy = int(input())
result = 0

for A in range(candy + 1):
    for B in range(candy + 1):
        for C in range(candy + 1):
            if A + B + C == candy:
                if (A >= B + 2) and (A !=0 and B !=0 and C !=0) and (C % 2 == 0):
                    result += 1

print(result)