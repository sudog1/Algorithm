def solution(numbers, target):
    dp = {0: 1}
    for num in numbers:
        items = dp.items()
        dp = {}
        for acc, cnt in items:
            if acc+num in dp:
                dp[acc+num] += cnt
            else:
                dp[acc+num] = cnt
            if acc-num in dp:
                dp[acc-num] += cnt
            else:
                dp[acc-num] = cnt
    return dp[target] if target in dp else 0