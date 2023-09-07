def solution(k, dungeons):
    dp = {0: 0}
    for a, b in sorted(dungeons, key=lambda x: x[0]-x[1]):
        for cur_fati in list(dp):
            next_fati = max(a, cur_fati + b)
            if next_fati > k:
                continue
            if next_fati in dp:
                dp[next_fati] = max(dp[next_fati], dp[cur_fati]+1)
            else:
                dp[next_fati] = dp[cur_fati]+1
    return max(dp.values())