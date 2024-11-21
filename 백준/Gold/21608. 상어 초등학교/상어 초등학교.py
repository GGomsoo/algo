# 상어 초등학교
# 골드 V

N = int(input())
students_info = dict() # 학생들의 정보
classroom = [[0] * N for _ in range(N)] # 교실의 크기 N * N

d_row = [0, 1, 0, -1]
d_col = [-1, 0, 1, 0]

for _ in range(N**2): # 학생들의 정보를 dict에 관리
    student = list(map(int, input().split()))
    students_info[student[0]] = student[1:]

for student in students_info:
    classroom_info = [] # 교실 정보
    for row in range(N):
        for col in range(N):
            if classroom[row][col] == 0: # 해당 자리가 빈 자리라면
                favorites = blank = 0 # 좋아하는 학생의 수, 빈자리 수

                for k in range(4): # 네방향 탐색
                    n_row = row + d_row[k]
                    n_col = col + d_col[k]

                    if 0 <= n_row < N and 0 <= n_col < N: # 교실 내에 있으면서
                        if classroom[n_row][n_col] in students_info[student]: # 주변에 좋아하는 번호가 있는 경우
                            favorites += 1
                        
                        elif classroom[n_row][n_col] == 0: # 주변에 빈자리가 있는 경우
                            blank += 1
    
                classroom_info.append((row, col, favorites, blank)) # 자리 선정에 대한 교실 정보를 추가
    classroom_info.sort(key=lambda x: (-x[2], -x[3], x[0], x[1])) # 좋아하는 학생 수(내림차순), 빈자리 수(내림차순), 행(오름차순), 열(오름차순) 순으로 정렬
    classroom[classroom_info[0][0]][classroom_info[0][1]] = student # 정렬한 값 중 첫번째 값에 대한 내용을 교실에 반영

result = 0
score = [0, 1, 10, 100, 1000]
classroom_info.sort()

for row in range(N):
    for col in range(N):
        idx = 0

        for k in range(4):
            n_row = row + d_row[k]
            n_col = col + d_col[k]

            if 0 <= n_row < N and 0 <= n_col < N:
                if classroom[n_row][n_col] in students_info[classroom[row][col]]: # 주변에 좋아하는 학생이 있으면 + 1
                    idx += 1
        
        result += score[idx]

print(result)