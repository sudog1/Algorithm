from functools import cmp_to_key

def comp(a, b):
    a_gap = a[0]-a[1]
    b_gap = b[0]-b[1]
    if a_gap == b_gap:
        return b[0]-a[0]
    else:
        return a_gap-b_gap

    
def solution(k, dungeons):
    dp = {0: 0}
    for a, b in sorted(dungeons, key=cmp_to_key(comp)):
        for cur_fati in list(dp):
            next_fati = max(a, cur_fati + b)
            if next_fati > k:
                continue
            if next_fati in dp:
                dp[next_fati] = max(dp[next_fati], dp[cur_fati]+1)
            else:
                dp[next_fati] = dp[cur_fati]+1
    return max(dp.values())