A = int(input())
W, V = map(int, input().split())

calc_A = W // V

if calc_A >= A:
    print(1)
else:
    print(0)