def solution(a, b):
    month = [31 if i%7%2 else 30 for i in range(13)]
    month[2] = 29
    month[7] = 31
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    count = 0
    for i in range(1, a):
        count += month[i]
    count += b-1
    return day[count%7]