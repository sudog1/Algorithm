from collections import defaultdict
from math import ceil

def solution(fees, records):
    acc_time = defaultdict(int)
    parking = defaultdict(lambda: -1)
    last_time = 23*60+59
    for record in records:
        time, car_num, state = record.split()
        m, s = map(int, time.split(':'))
        time_sec = m*60 + s
        if parking[car_num] >= 0:
            acc_time[car_num] += time_sec - parking[car_num]
            parking[car_num] = -1
        else:
            parking[car_num] = time_sec
    for car_num, time in filter(lambda x: x[1] >= 0, parking.items()):
        acc_time[car_num] += last_time - time
    total_fees = []
    for car_num in sorted(acc_time.keys()):
        result = acc_time[car_num] - fees[0]
        if result >= 0:
            total_fees.append(fees[1] + ceil(result/fees[2])*fees[3])
        else:
            total_fees.append(fees[1])
    return total_fees