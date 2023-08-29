from itertools import combinations

def make_pn(n):
    pn = [2]
    for x in range(3, n+1, 2):
        for y in pn:
            if not x % y:
                break
        else:
            pn.append(x)
    return pn

def solution(nums):
    answer = 0
    nums.sort()
    max_sum = sum(nums[-3:])
    pn = make_pn(max_sum)
    for s in combinations(nums, 3):
        if sum(s) in pn:
            answer += 1
    return answer