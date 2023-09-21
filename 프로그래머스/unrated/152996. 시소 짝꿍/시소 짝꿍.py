def solution(weights):
    people = {}
    torque = {}
    count = 0
    for weight in weights:
        if weight in people:
            count += people[weight]
            people[weight] += 1
        else:
            people[weight] = 1
    for weight in set(weights):
        for arm in range(2, 5):
            t = weight*arm
            if t in torque:
                count += torque[t]*people[weight]
                torque[t] += people[weight]
            else:
                torque[t] = people[weight]
    return count