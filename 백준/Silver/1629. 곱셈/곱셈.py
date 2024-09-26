# 곱셈
# 실버 I

## 분할정복을 이용한 거듭제곱
## 자연수 A를 B번 곱한 수를 C로 나눈 나머지를 알고싶다.
A, B, C = map(int, input().split())

def power(a, b, c):
    if b == 1: # B가 1인 경우
        return a % c
    
    else: # 1이 아닌 경우
        temp = power(a, b//2, c) # temp의 값은 return 되어오는 '(A ** B) % C' 의 값이다.
        if b % 2 == 0: # 제곱수가 짝수인 경우
            return (temp * temp) % c
        else: # 제곱수가 홀수인 경우
            return (temp * temp * a) % c

print(power(A, B, C))