# 색종이 만들기
# 실버 II
# 분할 정복 / 재귀
import sys; input = sys.stdin.readline

N = int(input()) # 종이의 크기 N x N
paper = [list(map(int, input().split())) for _ in range(N)] # 종이
white = blue = 0 # 흰색, 파란색

# 전체 종이가 모두 같은 색으로 칠해져 있지 않으면
# 가로와 세로로 중간 부분을 잘라서
# 같은 크기의 4개의 N/2 x N/2 색종이로 나눈다
# 모두 하얀색/파란색이거나, 색종이가 한 칸이 되어 더이상 자를 수 없을 때 까지 반복한다
def divide(y, x, N):
    global white, blue
    paper_color = paper[y][x]
    for j in range(y, y+N):
        for i in range(x, x+N):
            if paper_color != paper[j][i]:
                divide(y, x, N//2)
                divide(y+N//2, x, N//2)
                divide(y, x+N//2, N//2)
                divide(y+N//2, x+N//2, N//2)
                return
    
    if paper_color == 1:
        blue += 1
    else:
        white += 1

divide(0, 0, N)
print(white, blue, sep="\n")