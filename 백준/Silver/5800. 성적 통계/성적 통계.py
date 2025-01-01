# 성적 통계
# 실버 V

K = int(input())

for i in range(1, K+1):
    class_info = list(map(int, input().split()))
    students = class_info[0]
    math_score = sorted(class_info[1:], reverse=True)

    max_score = math_score[0]
    min_score = math_score[-1]

    gap = 0
    for j in range(len(math_score)-1):
        gap = max(gap, math_score[j] - math_score[j+1])
    
    print(f"Class {i}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {gap}")