# 도시와 비트코인
# 실버 III
## 진우의 위치 (0, 0) / 거래소 위치 (N-1, M-1)

from collections import deque

def finish_exchange(j, i):
    visited[j][i] = 1 # 현재위치 방문처리
    q = deque([(j, i)]) # 현재좌표 Q에 삽입

    while q:
        j, i = q.popleft() # Q에서 좌표를 추출
        if (j, i) == (M-1, N-1): # 해당 좌표가 거래소 좌표라면 Yes 문구를 return
            return "Yes"
        
        # 진우는 최대한 빨리 가야한다
        # 동쪽(오른쪽), 남쪽(아래쪽)으로만 이동한다
        dj = [0, 1] 
        di = [1, 0]

        # 2방향 탐색
        for k in range(2):
            nj = j + dj[k]
            ni = i + di[k]
            
            # 신규 좌표가 도시 범위 내에 있으면서
            if 0 <= nj < M and 0 <= ni < N:
                # 방문한 적 없고, 갈 수 있는 길(1) 이라면
                if not visited[nj][ni] and city[nj][ni] == 1:
                    # 해당 좌표를 방문처리
                    visited[nj][ni] = 1
                    # Q에 신규 좌표를 삽입한다
                    q.append((nj, ni))
    
    return "No"

N, M = map(int, input().split()) # 가로 N, 세로 M
city = [list(map(int, input().split())) for _ in range(M)] # 도시
visited = [[0] * N for _ in range(M)] # 방문체크

print(finish_exchange(0, 0))