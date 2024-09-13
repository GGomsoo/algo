# 뒤집힌 덧셈
# 브론즈 1

X, Y = input().split() # 문자열로 입력 받음

revX = revY = "" # reverseX, Y들

# 기존의 X, Y 길이부터 처음까지 뒤집어서 for문 진행
# revX, revY에 해당 값들을 문자열로 추가
for i in range(len(X)-1, -1, -1):
    revX += X[i]

for j in range(len(Y)-1, -1, -1):
    revY += Y[j]

# revX, revY를 자연수화 하여 덧셈 -> 다시 문자화
temp = str(int(revX) + int(revY))

result = "" # 최종 정답
for k in range(len(temp)-1, -1, -1): # 임시 숫자의 문자 길이만큼 for문을 뒤에서 진행
    result += temp[k]

print(int(result)) # 결과물은 정수(자연수)로 출력