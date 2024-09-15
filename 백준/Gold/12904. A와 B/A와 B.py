S = list(map(str, input()))
T = list(map(str, input()))

# S를 T로 만들어보니 메모리 초과 발생
# 반대로 T를 S로 만들기.. 구글 참조 ㅠ
while len(S) != len(T):
    if T[-1] == "A": # 문자열의 뒤에서 A를 추가 => 맨 마지막이 A이면 빼버린다
        T.pop()
    
    elif T[-1] == "B": # 뒤집고 뒤에 B를 추가
        T.pop()
        T.reverse()

if S == T:
    print(1)
else:
    print(0)