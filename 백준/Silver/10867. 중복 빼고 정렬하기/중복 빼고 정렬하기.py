# 중복 빼고 정렬하기
# 실버 V

N = int(input())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()
print(*nums)

