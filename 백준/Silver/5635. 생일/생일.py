# 생일
# 실버 V

N = int(input())
students = []
for _ in range(N):
    student = list(input().split())
    students.append(student)

students.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

# 가장 나이가 적은 사람
print(students[-1][0])

# 가장 나이가 많은 사람
print(students[0][0])