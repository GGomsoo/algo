# 중복 빼고 정렬하기
# 실버 V

N = int(input())
nums = sorted(set(map(int, input().split())))
print(*nums)