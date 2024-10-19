# 점프왕 쩰리 (Large)
# 실버 I

def jump_king(j, i):
    global result
    visited[j][i] = 1

    if (j, i) == (N-1, N-1):
        result = "HaruHaru"
    
    dj = [1, 0]
    di = [0, 1]

    for k in range(2):
        nj = j + dj[k] * game_board[j][i]
        ni = i + di[k] * game_board[j][i]

        if 0 <= nj < N and 0 <= ni < N:
            if not visited[nj][ni]:
                jump_king(nj, ni)

N = int(input())
game_board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = "Hing"

jump_king(0, 0)
print(result)