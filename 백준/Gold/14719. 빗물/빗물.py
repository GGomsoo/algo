# 빗물
# 골드 V

H, W = map(int, input().split())
block = list(map(int, input().split()))

start = 1
rain = 0

# for i in range(1, W-1):
#     left_block = max(block[:i])
#     right_block = max(block[i+1:])

#     min_block_height = min(left_block, right_block)

#     if block[i] < min_block_height:
#         rain += min_block_height - block[i]

while start != W-1:
    left = max(block[:start])
    right = max(block[start+1:])

    min_height = min(left, right)

    if block[start] < min_height:
        rain += min_height - block[start]
    
    start += 1

print(rain)