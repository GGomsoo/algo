# 킹
# 실버 III
## A(65) ~ H(72)

king, stone, N = input().split()
N = int(N)

king_col, king_row = int(ord(king[0])-ord("A")+1), int(king[1])
stone_col, stone_row = int(ord(stone[0])-ord("A")+1), int(stone[1])

# 이동관련 주문 dict 처리
move = {"R": [0, 1], "L": [0, -1], "B": [-1, 0], "T": [1, 0],
        "RT": [1, 1], "LT": [1, -1], "RB": [-1, 1], "LB": [-1, -1]}

for _ in range(N):
    # 어떻게 움직일지에 대한 요청
    order = input()

    # 킹을 요청에 따라 움직인다
    new_king_col = king_col + move[order][1]
    new_king_row = king_row + move[order][0]

    # 요청에 따라 움직인 킹이 체스판 범위 내에 있다면
    if 1 <= new_king_col <= 8 and 1 <= new_king_row <= 8:
        # 움직인 좌표가 돌멩이와 겹친다면
        if new_king_col == stone_col and new_king_row == stone_row:
            # 돌도 새로운 좌표를 구한다
            new_stone_col = stone_col + move[order][1]
            new_stone_row = stone_row + move[order][0]
            # 그 좌표가 체스판 범위 내에 있다면
            if 1 <= new_stone_col <= 8 and 1 <= new_stone_row <= 8:
                # 킹과 돌을 같은 방향으로 이동시킨다
                king_col += move[order][1]
                king_row += move[order][0]
                stone_col += move[order][1]
                stone_row += move[order][0]
            # 범위 밖이면 그 이동은 건너뛴다
            else:
                continue
        # 돌과 겹치지 않는다면
        else:
            king_col += move[order][1]
            king_row += move[order][0]
    # 킹이 범위 밖이라면 그 요청은 건너뛴다
    else:
        continue

print(chr(king_col + 64) + f"{king_row}")
print(chr(stone_col + 64) + f"{stone_row}")