# 방 배정
# 브론즈 II

N, K = map(int, input().split()) # 학생 수, 배정 최대 인원 수
students = [[0] * (6+1) for _ in range(2)] # 학생 1학년부터 6학년까지 남녀
room = 0 # 방 갯수

for _ in range(N):
    gender, grade = map(int, input().split()) # 성별과 학년
    students[gender][grade] += 1 # 해당 인원수 추가

for j in range(2):
    for i in range(1, 7):
        if 1 <= students[j][i] <= K: # 배정 최대 인원 넘지 않는다면
            room += 1 # 방 1개 추가
        else: # 넘는 경우
            if students[j][i] % K == 0: # 최대 인원의 배수인 경우
                room += students[j][i] // K
            else: # 최대 인원의 배수가 아닌 경우
                room += students[j][i] // K + 1

print(room)