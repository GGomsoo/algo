def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                if stack[-1] == "(":
                    stack.pop(-1)
            else:
                stack.append(i)
    
    if stack:
        answer = False
    
    # # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer