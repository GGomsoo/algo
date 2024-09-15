def cutting_trees(start, end):
    while start <= end:
        mid = (start + end) // 2

        cut = 0 # 자른 나무의 길이
        for tree in trees:
            if tree >= mid: # 나무길이가 절단기 길이보다 크거나 같다면
                cut += (tree - mid) # 자른다
        
        if cut >= M: # 자른 나무들이 필요한 나무보다 많을 경우
            start = mid + 1 # 절단기 길이를 늘린다
        else:
            end = mid - 1
    
    return end # 절단기에 설정할 수 있는 높이의 최댓값

N, M = map(int, input().split()) # 나무의 수 N, 필요한 나무의 길이 M
trees = list(map(int, input().split())) # 나무들의 길이

print(cutting_trees(0, max(trees)))