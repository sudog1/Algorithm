def solution(ingredient):
    count = 0
    stack = []
    for e in ingredient:
        if len(stack) >= 3 and e == 1:
            for i in range(1, 4):
                if stack[-i]+i != 4:
                    stack.append(e)
                    break
            else:
                count += 1
                for _ in range(3):
                    stack.pop()
        else:
            stack.append(e)
            
    return count