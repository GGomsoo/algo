# 맥주 마시면서 걸어가기
# 골드 V

from collections import deque

T = int(input()) # test case의 개수
for _ in range(T):
    def walk_beer():
        visited = [0] * N
        position = deque([(sang_home_x, sang_home_y)]) # 상근이의 집 위치를 Q에 담음

        while position:
            home_x, home_y = position.popleft()
            
            # 맥주가 다 떨어지기전에 페스티벌에 도착할 수 있다면
            if abs(home_x - festival_x) + abs(home_y - festival_y) <= 1000:
                return ("happy") # 행복해요
            
            # 편의점 갯수만큼 반복
            for i in range(N):
                if not visited[i]:
                    # 편의점의 좌표를 추출
                    cur_conv_x, cur_conv_y = convenience[i]

                    # 맥주 다 떨어지기전에 편의점에 도착할 수 있다면
                    if abs(home_x - cur_conv_x) + abs(home_y - cur_conv_y) <= 1000:
                        # 해당 편의점 방문 처리
                        visited[i] = 1
                        # 해당 위치를 Q에 다시 담음
                        position.append((cur_conv_x, cur_conv_y))
        
        # 도착전에 맥주가 떨어지면 슬퍼요
        return "sad"

    N = int(input()) # 맥주를 파는 편의점의 개수
    sang_home_x, sang_home_y = map(int, input().split()) # 상근이의 집 위치

    convenience = [] # 편의점 목록
    for _ in range(N):
        conv_x, conv_y = map(int, input().split())
        convenience.append((conv_x, conv_y))
    
    festival_x, festival_y = map(int, input().split()) # 페스티벌의 좌표
    print(walk_beer()) # 맥주 마시면서 걸어가기