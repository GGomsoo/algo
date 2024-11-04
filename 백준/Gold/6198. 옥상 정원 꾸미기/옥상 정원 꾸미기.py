# 옥상 정원 꾸미기
# 골드 V
# 스택

'''
모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다.
자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 다음 빌딩을 볼 수 없다.
'''

### 시간초과
N = int(input()) # 빌딩의 수
buildings = [] # 빌딩을 담을 스택
stack = []
cnt = 0 # 벤치마킹한 빌딩의 수

for _ in range(N):
    buildings.append(int(input())) # 빌딩의 정보를 스택에 추가

for building in buildings: # 빌딩들에 대해서
    # 스택이 있고, 스택의 마지막값이 빌딩의 값보다 낮거나 같다면
    # == 해당 빌딩을 관찰할 수 없다
    # 스택에서 제외
    while stack and stack[-1] <= building:
        stack.pop()
    
    # 스택에 빌딩을 추가한다
    stack.append(building)

    # 벤치마킹한 빌딩의 수를 추가하는데
    # 마지막 빌딩의 옥상을 볼 수 있는 건물이 없기 때문에 스택의 길이에서 -1
    cnt += len(stack) - 1

print(cnt)