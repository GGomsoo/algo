# 카드1
# 실버 V

from collections import deque

N = int(input())
cards = deque(list(range(1, N+1)))

# 카드가 1장 남을 때 까지 반복한다
while len(cards) > 1:
    # 제일 위 카드를 바닥에 버린다
    print(cards.popleft(), end=" ")
    # 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
    cards.append(cards.popleft())
# 마지막 남은 카드를 출력한다
print(cards[0])