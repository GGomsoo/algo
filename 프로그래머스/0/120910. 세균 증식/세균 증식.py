def solution(n, t):
    answer = n
    for _ in range(t):
        answer *= 2
    return answer