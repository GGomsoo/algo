# 알파벳
# 골드 IV
import sys; input = sys.stdin.readline

def dfs(r, c, step):
    global cnt
    cnt = max(cnt, step)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 네방향 탐색
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        # 보드 범위 내에 있으면서
        if 0 <= nc < C and 0 <= nr < R:
            # 보드 내 새로운 위치의 알파벳이 이전에 지나온 적 없는 알파벳이라면
            if board[nr][nc] not in history:
                history.add(board[nr][nc]) # history에 추가하고
                dfs(nr, nc, step + 1) # dfs 다시 시작
                history.remove(board[nr][nc]) ## 백트래킹 활용. 지나온 알파벳의 흔적을 지운다.


R, C = map(int, input().split()) # 세로 R, 가로 C
board = [list(input()) for _ in range(R)] # 표 모양의 보드
history = set() # 지나온 알파벳들을 보관할 set함수 (겸사겸사 중복제거)
history.add(board[0][0]) # 좌측 상단에서 시작. 좌측 상단의 알파벳을 history에 넣어준다

cnt = 0 # 최대값 비교용 cnt
dfs(0, 0, 1)

print(cnt)