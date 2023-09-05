def solution(topping):
    l_num = []
    r_num = []
    l_temp = set()
    r_temp = set()
    for i in range(len(topping)-1):
        l_temp.add(topping[i])
        r_temp.add(topping[-i-1])
        l_num.append(len(l_temp))
        r_num.append(len(r_temp))
    count = 0
    for i in range(len(topping)-1):
        if l_num[i] == r_num[len(topping)-2-i]:
            count += 1
    return count