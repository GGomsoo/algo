N = int(input())

ans1 = ans2 = ans3 = 0

for i in range(1, N+1):
    ans1 += i

for j in range(1, N+1):
    ans2 += j

for k in range(1, N+1):
    ans3 += k ** 3

print(ans1)
print(ans2**2)
print(ans3)