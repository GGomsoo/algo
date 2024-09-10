from collections import deque

# 입력 처리
N, Q = map(int, input().split())

# 스택 초기화
back = deque()   # 뒤로가기 스택
front = deque()  # 앞으로가기 스택
current_page = -1  # 현재 페이지 (-1은 초기 상태, 아무 페이지도 열지 않은 상태)

for _ in range(Q):
    command = input().split()
    
    if command[0] == 'A':  # 접속 명령
        new_page = int(command[1])
        if current_page != -1:  # 이미 페이지가 있을 경우
            back.append(current_page)  # 현재 페이지를 back에 저장
        current_page = new_page  # 새 페이지 접속
        front.clear()  # 새로운 페이지를 접속하면 앞으로 가기 목록은 초기화
    
    elif command[0] == 'B':  # 뒤로 가기 명령
        if back:  # 뒤로 갈 페이지가 있을 경우
            front.append(current_page)  # 현재 페이지를 앞으로 가기 스택에 저장
            current_page = back.pop()  # 뒤로가기 스택에서 가장 최근 페이지로 이동
    
    elif command[0] == 'F':  # 앞으로 가기 명령
        if front:  # 앞으로 갈 페이지가 있을 경우
            back.append(current_page)  # 현재 페이지를 뒤로 가기 스택에 저장
            current_page = front.pop()  # 앞으로 가기 스택에서 가장 최근 페이지로 이동
    
    elif command[0] == 'C':  # 중복 제거 명령
        temp = deque()
        prev = None
        while back:
            page = back.pop()
            if page != prev:
                temp.appendleft(page)
                prev = page
        back = temp  # 중복 제거 후 back 갱신

# 출력 처리
print(current_page)  # 현재 페이지 출력

# 뒤로 가기 스택 출력 (역순으로)
if back:
    print(" ".join(map(str, reversed(back))))
else:
    print(-1)

# 앞으로 가기 스택 출력 (역순으로)
if front:
    print(" ".join(map(str, reversed(front))))
else:
    print(-1)
