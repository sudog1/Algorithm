def solution(numbers):
    result = [-1]*len(numbers)
    numbers_with_idx = list(enumerate(numbers))
    stack = []
    for e in numbers_with_idx:
        while stack:
            if stack[-1][1] < e[1]:
                result[stack[-1][0]] = e[1]
                stack.pop()
            else:
                break
        stack.append(e)
    return result