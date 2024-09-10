from collections import deque

N, Q = map(int, input().split())

front = deque()
back = deque()
current_page = 0
access_cnt = False

for _ in range(Q):
    order = input().split()
    
    if "A" in order: # 접속의 경우
        if not access_cnt: # 처음 웹페이지 접속하는 경우
            current_page = int(order[1]) # 현재 페이지를 뒤로 가기 공간에 추가 X
            access_cnt = True
        else:
            back.append(current_page) # 현재 페이지를 뒤로 가기 공간에 추가
            current_page = int(order[1]) # 다음 접속 페이지가 현재 페이지로 갱신
        front.clear() # 앞으로 가기 공간에 저장된 페이지 모두 삭제
    
    elif "B" in order: # 뒤로가기의 경우
        if back: # 뒤로가기 공간에 1개 이상의 페이지가 저장되어 있을 때
            front.append(current_page) # 현재 보던 웹페이지를 앞으로 가기 공간에 저장
            current_page = back.pop() # 뒤로 가기 공간에서 방문한지 가장 최근의 페이지에 접속. 해당 페이지는 뒤로 가기 공간에서 삭제
    
    elif "F" in order: # 앞으로가기의 경우
        if front: # 앞으로 가기 공간에 1개 이상의 페이지가 저장되어 있을 때
            back.append(current_page) # 현재 보던 웹페이지를 뒤로 가기 공간에 저장
            current_page = front.pop() # 앞으로 가기 공간에서 방문한지 가장 최근의 페이지에 접속. 해당 페이지는 앞으로 가기 공간에서 삭제
    
    elif "C" in order: # 압축의 경우
        temp = deque() # 중복 제거에 사용할 임시 deque
        now = 0 # 페이지 중복 확인용
        while back:
            page = back.popleft()
            if now != page:
                temp.append(page)
                now = page
        back = temp # 중복 제거한 back으로 갱신

# 현재 페이지 출력
print(current_page)

# 가장 최근에 방문한 순서대로 == 뒤에서부터 출력
if back:
    print(" ".join(map(str, reversed(back)))) 
else:
    print(-1)

if front:
    print(" ".join(map(str, reversed(front))))
else:
    print(-1)