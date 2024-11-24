# 컨베이어 벨트 위의 로봇
# 골드 V
## 힌트: deque의 rotate 활용하기

from collections import deque

def moving_robot():
    result = 0 # 단계수
    robot_location = deque([0 for _ in range(N)]) # 로봇의 위치

    while True:
        result += 1

        # 순서1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        conveyor_belt.rotate(1)
        robot_location.rotate(1)

        # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
        robot_location[N-1] = 0

        # 순서2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로
        # 한 칸 이동할 수 있다면 이동한다. 이동할 수 없다면 가만히 있는다.
        # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        # 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.
        for i in range(N-2, -1, -1):
            if robot_location[i] and not robot_location[i+1] and conveyor_belt[i+1] >= 1:
                robot_location[i], robot_location[i+1] = 0, 1
                conveyor_belt[i+1] -= 1
        
        # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
        robot_location[N-1] = 0

        # 순서3. 올리는 위치에 있는 칸의 내구도가 0이 아니면
        # 올리는 위치에 로봇을 올린다.
        if conveyor_belt[0]:
            robot_location[0] = 1
            conveyor_belt[0] -= 1
        
        # 순서4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
        # 그렇지 않다면 1번으로 돌아간다.
        if conveyor_belt.count(0) >= K:
            break
    
    return result

N, K = map(int, input().split()) # 컨베이어 벨트의 길이, 내구도 0인 칸의 개수
conveyor_belt = deque(list(map(int, input().split()))) # 컨베이어 벨트의 정보
print(moving_robot())