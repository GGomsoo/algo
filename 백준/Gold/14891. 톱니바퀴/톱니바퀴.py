# 톱니바퀴
# 골드 V

from collections import deque

def left_saw(num, d):
    if num < 0:
        return
    
    if sawtooth[num][2] != sawtooth[num + 1][6]:
        left_saw(num -1, -d)
        sawtooth[num].rotate(d)


def right_saw(num, d):
    if num > N-1:
        return
    
    if sawtooth[num][6] != sawtooth[num - 1][2]:
        right_saw(num + 1, -d)
        sawtooth[num].rotate(d)

# 톱니바퀴 갯수 및 톱니바퀴에 대한 정보
N = 4
sawtooth = [deque(list(map(int, input()))) for _ in range(N)]

# 회전 횟수 및 관련 정보
K = int(input())
for _ in range(K):
    saw_num, direction = map(int, input().split())
    saw_num -= 1

    # 주변 톱니의 회전 가능여부 확인
    left_saw(saw_num - 1, -direction)
    right_saw(saw_num + 1, -direction)

    # 회전시킬 톱니바퀴와 방향을 결정
    sawtooth[saw_num].rotate(direction)


# # 톱니바퀴 회전 디버깅
# print()
# for saw in sawtooth:
#     print(*saw)
# print()

# 톱니바퀴의 12시 방향이 N극(0)이면 0점
# S극(1)이면 1번은 1, 2번은 2, 3번은 4, 4번은 8점
result = 0
for i in range(N):
    if sawtooth[i][0] == 1:
        result += 2 ** i

print(result)
