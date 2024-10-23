# 그룹 단어 체커
# 실버 V

import sys; input = sys.stdin.readline

N = int(input()) # 단어의 개수
cnt = N # 그룹 단어 cnt

for _ in range(N):
    word = input() # 단어 입력
    for i in range(len(word)-1): # 단어의 길이만큼 for문 진행
        if word[i] == word[i+1]: # 문자가 연속해서 나타난다면
            pass # 그룹 단어이므로 pass
        elif word[i] in word[i+1:]: # 단어가 떨어져서 나오는 경우도 있다면
            cnt -= 1 # 전체 단어 개수에서 -1
            break # 반복문을 멈춘다

print(cnt) # 최종적인 그룹단어의 개수 출력