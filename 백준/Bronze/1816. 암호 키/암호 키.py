T = int(input())

for _ in range(T):
    number = int(input())

    for i in range(2, 1_000_001):
        if number % i == 0:
            print("NO")
            break

        if i == 1_000_000:
            print("YES")