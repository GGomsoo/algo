# 종이의 개수
# 실버 II

def divide(y, x, N):
    global minus, zero, one
    number = P[y][x]
    for j in range(y, y+N):
        for i in range(x, x+N):
            if P[j][i] != number:
                divide(y, x, N//3)
                divide(y, x+N//3, N//3)
                divide(y, x+(N//3)*2, N//3)
                divide(y+N//3, x, N//3)
                divide(y+N//3, x+N//3, N//3)
                divide(y+N//3, x+(N//3)*2, N//3)
                divide(y+(N//3)*2, x, N//3)
                divide(y+(N//3)*2, x+N//3, N//3)
                divide(y+(N//3)*2, x+(N//3)*2, N//3)
                return
    
    if number == -1:
        minus += 1
    elif number == 0:
        zero += 1
    else:
        one += 1

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

minus = zero = one = 0

divide(0, 0, N)
print(minus, zero, one, sep="\n")