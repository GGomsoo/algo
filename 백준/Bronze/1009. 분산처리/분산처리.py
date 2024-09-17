# 분산처리
# 브론즈 II
# 1, 5, 6은 몇번을 제곱해도 마지막 숫자가 1, 5, 6
# 나머지 숫자는 (ex: 3의 경우 3, 9, 27, 81, 243, 729, 2187, ...) 그냥 3이랑 3**5랑 뒷자리수가 같다 ( 제곱수 % 4) 
# 제곱수 % 4 == 0 인 경우 -> 4제곱
import sys; input = sys.stdin.readline

N = int(input())
same = [1, 5, 6]
other = [2, 3, 4, 7, 8, 9]

for _ in range(N):
    A, B = map(int, input().split())
    A %= 10

    if A == 0:
        print(10)
    
    elif A in same:
        print(A)
    
    elif A in other:
        B = B % 4
        temp = 0
        if B == 0:
            temp = str(A ** 4)
            print(temp[-1])
        
        else:
            temp = str(A ** B)
            print(temp[-1])