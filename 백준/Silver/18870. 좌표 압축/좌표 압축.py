# 좌표 압축
# 실버 II

N = int(input()) # 좌표 갯수 N
X = list(map(int, input().split())) # 좌표 list
set_X = sorted(set(X)) # 입력받은 좌표들에 대한 중복제거, 오름차순으로 정렬

D = dict() # 좌표들을 dict에 {좌표 : 인덱스} 형식으로 저장
for i in range(len(set_X)):
    D[set_X[i]] = i

for i in X:
    print(D[i], end=" ")