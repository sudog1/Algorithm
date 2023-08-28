def solution(number):
    number.sort()
    count = 0
    for i in range(len(number)):
        if number[i] > 0:
            break
        for j in range(i+1, len(number)):
            temp = number[i]+number[j]
            if temp > 0:
                break
            for k in range(j+1, len(number)):
                res = number[i]+number[j]+number[k]
                if res == 0:
                    count += 1
                elif res > 0:
                    break
    return count