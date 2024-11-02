# 큐 2
# 실버 IV
'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys; input = sys.stdin.readline
from collections import deque

N = int(input())
Q = deque()

for i in range(N):
    i = input().split()

    if i[0] == "push":
        Q.append(i[1])
    
    elif i[0] == "pop":
        if not Q:
            print(-1)
        else:
            print(Q.popleft())
    
    elif i[0] == "size":
        print(len(Q))

    elif i[0] == "empty":
        if not Q:
            print(1)
        else:
            print(0)
    
    elif i[0] == "front":
        if not Q:
            print(-1)
        else:
            print(Q[0])
    
    elif i[0] == "back":
        if not Q:
            print(-1)
        else:
            print(Q[-1])