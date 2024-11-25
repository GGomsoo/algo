# 마법사 상어와 파이어볼
# 골드 IV

from collections import deque

# 격자의 크기, 파이어볼의 갯수, 이동명령의 수
N, M, K = map(int, input().split())

# 2중 리스트로 구현한 격자
boards = [[[] for _ in range(N)] for _ in range(N)]

# 파이어볼을 담을 deque
fireballs = deque()

# 파이어볼에 대한 정보를 입력
for _ in range(M):
    # 행, 열, 질량, 속도, 방향
    r, c, m, s, d = map(int, input().split())
    # 인덱스값으로 사용할 행, 열은 -1씩 계산 후 추가
    fireballs.append([r-1, c-1, m, s, d])

# 이동명령의 수 만큼 반복문 실행
for _ in range(K):

    # 파이어볼에 대한 정보를 격자에 입력
    while fireballs:
        row, col, mass, speed, direction = fireballs.popleft()

        # 파이어볼의 방향에 대한 정보
        # 12시부터 시계방향으로 진행
        d_row = [-1, -1, 0, 1, 1, 1, 0, -1]
        d_col = [0, 1, 1, 1, 0, -1, -1, -1]

        n_row = (row + d_row[direction] * speed) % N
        n_col = (col + d_col[direction] * speed) % N
        boards[n_row][n_col].append([mass, speed, direction])
    
    # 격자 전체를 조사
    for row in range(N):
        for col in range(N):
            # 같은 위치에 파이어볼이 2개 이상 있다면 파이어볼은 모두 하나로 합쳐진다.
            if len(boards[row][col]) >= 2:
                temp_mass, temp_speed, check_odd, check_even, cnt = 0, 0, 0, 0, len(boards[row][col])

                # 같은 위치의 파이어볼에 대한 정보들을 합치는 중
                while boards[row][col]:
                    mass, speed, direction = boards[row][col].pop(0)

                    temp_mass += mass
                    temp_speed += speed

                    # 해당 파이어볼의 방향이 홀수/짝수인지 확인하는 과정
                    if direction % 2 == 0:
                        check_even += 1
                    else:
                        check_odd += 1
                
                # 합쳐지는 파이어볼의 방향이 모두 홀수/짝수라면
                # 4개로 나눠지는 파이어볼의 방향 [0, 2, 4, 6]
                if check_odd == cnt or check_even == cnt:
                    n_direction_4 = [0, 2, 4, 6]

                # 그게 아니라면 방향은 [1, 3, 5, 7]
                else:
                    n_direction_4 = [1, 3, 5, 7]
                
                # 질량 = 합쳐진 파이어볼의 질량 합 / 5
                # 속력 = 합쳐진 파이어볼의 속력 합 / 합쳐진 파이어볼의 갯수
                total_mass, total_speed = temp_mass // 5, temp_speed // cnt

                # 파이어볼의 질량이 0이 아니라면
                # 4개의 파이어볼로 나눈다
                if total_mass:
                    for direction_4 in n_direction_4:
                        fireballs.append([row, col, total_mass, total_speed, direction_4])
            
            # 격자의 해당 위치에 파이어볼이 1개만 있는 경우
            if len(boards[row][col]) == 1:
                mass, speed, direction = boards[row][col].pop(0)
                fireballs.append([row, col, mass, speed, direction])

# 남아있는 파이어볼의 질량 구하기
total_fireball_mass = sum([fireball[2] for fireball in fireballs])
print(total_fireball_mass)