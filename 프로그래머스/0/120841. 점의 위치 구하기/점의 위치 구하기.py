def solution(dot):
    answer = 0
    x = dot[0]
    y = dot[1]
    
    for _ in dot:
        if x > 0 and y > 0:
            answer = 1
        elif x < 0 and y > 0:
            answer = 2
        elif x < 0 and y < 0:
            answer = 3
        else:
            answer = 4
    return answer