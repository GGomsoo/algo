# 팔
# 실버 I
## L 보다 크거나 같고 R 보다 작거나 같은 자연수 중
## 8이 가장 적게 들어있는 수에 들어있는 8의 개수

L, R = map(str, input().split()) # 자연수 L, R 주어짐
len_L, len_R = len(L), len(R) 
cnt_8 = 0

# 서로 길이가 다르다 == 자리수가 다르다 == 8이 없는 숫자가 있다
if len_L != len_R: 
    print(0)

# 서로 길이가 같다
else:
    for i in range(len_L):
        # 서로의 자리수가 같은 숫자고
        if L[i] == R[i]:
            # L의 해당 자리수가 8이라면
            if L[i] == "8":
                # 8의 개수 추가
                cnt_8 += 1
        # 길이는 같은데, 서로 자리수가 다른 숫자라면
        # 굳이 비교할 필요가 없다.
        else:
            break
    
    print(cnt_8)