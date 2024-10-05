# 예산
# 실버 II

## 이분 탐색 활용

N = int(input()) # 지방의 수
budget = sorted(map(int, input().split())) # 각 지방의 예산 요청
S = int(input()) # 총 예산

def solution(start, end, target):
    ans = 0 # 최종 상한액
    while start <= end:
        temp = 0 # 임의의 총 예산
        mid = (start + end) // 2

        for b in budget:
            if b > mid: # 요청한 예산이 상한액보다 큰 경우
                b = mid # 상한액만큼만 배정한다
            temp += b # 이 값들을 더한다
        
        if target >= temp: # 임의의 총 예산이 총액보다 작거나 같은 경우
            start = mid + 1 # 상한액 증가를 위한 조정
            ans = mid # 현재 상한액을 최종 상한액으로 배정
        else:
            end = mid - 1 # 상한액 감소를 위한 조정
    
    return ans # 최종적인 상한액을 return 한다

print(solution(1, budget[-1], S))