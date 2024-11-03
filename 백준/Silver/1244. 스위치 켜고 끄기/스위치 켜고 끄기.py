# 스위치 켜고 끄기
# 실버 IV
# 남학생 1 / 여학생 2

def change_switch(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0

N = int(input()) # 스위치의 갯수
switch = [-1] + list(map(int, input().split())) # 스위치 정보, 1번부터 사용하기 위해 0번 인덱스 값에 임의의 숫자 설정
S = int(input()) # 학생의 숫자

for _ in range(S):
    gender, switch_num = map(int, input().split()) # 성별, 학생이 받은 숫자

    # 남학생
    if gender == 1:
        for i in range(switch_num, N+1, switch_num): # 스위치 번호가 자기가 받은 수의 배수이면, 상태를 변경
            change_switch(i)
    
    # 여학생
    else:
        change_switch(switch_num) # 자기가 받은 번호의 스위치를 중심으로
        for j in range(N//2):
            if switch_num - j < 1 or switch_num + j > N: # 스위치 범위를 넘어서면 중단
                break
            if switch[switch_num - j] == switch[switch_num + j]: # 좌우 대칭인 경우라면, 상태를 변경
                change_switch(switch_num - j)
                change_switch(switch_num + j)
            else:
                break

for k in range(1, N+1):
    print(switch[k], end=" ") # 최종적인 스위치 상태를 출력

    if k % 20 == 0: # 스위치 갯수가 20개가 넘어간다면
        print() # 줄바꿈