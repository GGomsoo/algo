N = int(input())
A_list = set(map(int, input().split()))
M = int(input())
B_list = list(map(int, input().split()))

for i in B_list:
    print(1) if i in A_list else print(0)