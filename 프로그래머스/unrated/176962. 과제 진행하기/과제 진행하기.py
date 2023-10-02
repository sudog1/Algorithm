def conv(x):
    h, m = map(int, x[1].split(':'))
    x[1] = h*60 + m
    x[2] = int(x[2])
    return x

def solution(plans):
    completed = []
    plans = sorted(map(conv, plans), key=lambda x: x[1])
    paused = []
    for i in range(len(plans)-1):
        cur_plan = plans[i]
        next_plan = plans[i+1]
        spare_time = next_plan[1] - (cur_plan[1] + cur_plan[2])
        if spare_time >= 0:
            completed.append(cur_plan[0])
            while paused and paused[-1][2] <= spare_time:
                spare_time -= paused[-1][2]
                completed.append(paused.pop()[0])
            if paused:
                paused[-1][2] -= spare_time
        else:
            cur_plan[2] = -spare_time
            paused.append(cur_plan)
    completed.append(plans[-1][0])
    while paused:
        completed.append(paused.pop()[0])
    return completed