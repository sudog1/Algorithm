def solution(want, number, discount):
    dis_num = {i: 0 for i in want}
    count = 0
    for i in range(len(discount)):
        if i >= 10 and discount[i-10] in dis_num:
            dis_num[discount[i-10]] -= 1
        if discount[i] in dis_num:
            dis_num[discount[i]] += 1
        for j in range(len(want)):
            if dis_num[want[j]] < number[j]:
                break
        else:
            count += 1
    return count