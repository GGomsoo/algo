# 두 숫자의 곱이 n인 자연수의 순서쌍
# n의 약수의 갯수를 구하면 된다

def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer