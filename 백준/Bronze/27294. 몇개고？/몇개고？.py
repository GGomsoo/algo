'''
술 + 초밥 or not 점심식사 == 밥알 280
점식식사 and not 술 == 밥알 320

T <= 11 : 아침
12 <= T <= 16 : 점심
나머지 : 저녁

S == 1 : 술
S == 0 : 술 X
'''

T, S = map(int, input().split())

if S == 1 or (T <= 11 or T > 16):
    print(280)

elif (12 <= T <= 16) and (S == 0):
    print(320)