# 회의실 배정
# 실버 I

import sys; input = sys.stdin.readline

N = int(input())
meeting_times = [list(map(int, input().split())) for _ in range(N)]
meeting_times.sort(key=lambda x: (x[1], x[0])) # 회의 종료시간 기준으로 오름차순 정렬

end_time = cnt = 0
for i in range(N):
    if end_time <= meeting_times[i][0]: # 회의 종료시간이 다음 회의 시작시간보다 작다면
        end_time = meeting_times[i][1] # 회의 시작, 종료 시간을 해당 회의의 종료 시간으로 변경
        cnt += 1 # 회의 횟수 증가

print(cnt)