def solution(storey):
    dp = {storey: 0}
    que = [[storey, 0]]
    min_consume = 80
    for sto, cnt in que:
        if sto == 0:
            min_consume = min(min_consume, cnt)
            continue
        q = sto // 10
        r = sto % 10
        if q in dp:
            if cnt+r < dp[q]:
                dp[q] = cnt+r
                que.append([q, cnt+r])
        else:
            dp[q] = cnt+r
            que.append([q, cnt+r])
        q += 1
        r = 10-r
        if q in dp:
            if cnt+r < dp[q]:
                dp[q] = cnt+r
                que.append([q, cnt+r])
        else:
            dp[q] = cnt+r
            que.append([q, cnt+r])
    return min_consume