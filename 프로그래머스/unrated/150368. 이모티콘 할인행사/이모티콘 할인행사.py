max_members = 0
max_sales = 0
dc_ratio = [10, 20, 30, 40]

def discount(users, emoticons, cnt_members, cnt_sales, n):
    global max_members, max_sales
    if n >= len(emoticons):
        if max_members < cnt_members:
            max_members = cnt_members
            max_sales = cnt_sales
        elif max_members == cnt_members:
            max_sales = max(max_sales, cnt_sales)
        return
    for i in range(len(dc_ratio)):
        price = emoticons[n] * (100-dc_ratio[i]) // 100
        for user in users:
            if user[0] > dc_ratio[i]:
                break
            flag = False
            if user[1] <= user[2]:
                flag = True
            else:
                cnt_sales += price
            user[2] += price
            if not flag and user[1] <= user[2]:
                cnt_members += 1
                cnt_sales -= user[2]
        discount(users, emoticons, cnt_members, cnt_sales, n+1)
        for user in users:
            if user[0] > dc_ratio[i]:
                break
            flag = False
            if user[1] > user[2]:
                flag = True
                cnt_sales -= price
            user[2] -= price
            if not flag and user[1] > user[2]:
                cnt_members -= 1
                cnt_sales += user[2]


def solution(users, emoticons):
    users = sorted(user+[0] for user in users)
    answer = []
    discount(users, emoticons, 0, 0, 0)
    return [max_members, max_sales]