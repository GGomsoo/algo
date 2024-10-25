# 알고리즘 수업 - 버블 정렬 2 - 마라톤 문제
# 브론즈 I

def bubble_sort(lst, count):
    global cnt
    for j in range(len(lst)-1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                cnt += 1

                if cnt == count:
                    print(*lst)
                    break
    
    if cnt < count:
        print(-1)

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

bubble_sort(A, K)