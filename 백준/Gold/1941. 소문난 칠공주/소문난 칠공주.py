### GPT CODE

from collections import deque

# 입력을 받는다
grid = [input().strip() for _ in range(5)]

# 5x5에서 각 좌표의 번호를 0부터 24까지 매핑
coords = [(i, j) for i in range(5) for j in range(5)]

# 방향 벡터 (상, 하, 좌, 우)
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_connected(selected):
    """선택된 7명의 좌표가 서로 연결되어 있는지 확인"""
    visited = set()
    q = deque([selected[0]])
    visited.add(selected[0])
    
    while q:
        curr = q.popleft()
        x, y = curr // 5, curr % 5
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            nxt = nx * 5 + ny
            if 0 <= nx < 5 and 0 <= ny < 5 and nxt in selected and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    
    return len(visited) == 7

def dfs(idx, cnt, dasom, selected):
    """조합을 만들어 조건을 만족하는지 탐색"""
    global answer
    # 7명을 선택한 경우
    if cnt == 7:
        if dasom >= 4 and is_connected(selected):
            answer += 1
        return
    
    # 선택 가능 범위를 넘어선 경우
    if idx >= 25:
        return

    # 현재 좌표를 선택하는 경우
    dfs(idx + 1, cnt + 1, dasom + (grid[idx // 5][idx % 5] == 'S'), selected + [idx])
    # 현재 좌표를 선택하지 않는 경우
    dfs(idx + 1, cnt, dasom, selected)

# 가능한 경우의 수를 세는 변수
answer = 0
dfs(0, 0, 0, [])

# 결과 출력
print(answer)
