N1, N2, N12 = map(int, input().split())

N = abs(((N1 + 1) * (N2 + 1)) // (N12 + 1) - 1)
print(N)