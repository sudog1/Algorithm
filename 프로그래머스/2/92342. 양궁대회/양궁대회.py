def shoot(n, info, target, state, score):
    global max_score, final_state, is_win
    if target == len(info):
        if max_score < score:
            max_score = score
            for i in range(len(info)-1):
                final_state[i] = state[i]
            final_state[-1] = n
        elif max_score == score:
            flag = False
            state[-1] = n
            for i in range(1, len(info)):
                if state[-i] < final_state[-i]:
                    break
                elif state[-i] > final_state[-i]:
                    flag = True
                    break
            if flag:
                for i in range(len(info)):
                    final_state[i] = state[i]
            state[-1] = 0
        return
    
    shoot(n, info, target+1, state, score)
    if info[target]+1 <= n:
        n -= info[target]+1
        state[target] = info[target]+1
        score += (10-target) * (2 if info[target] else 1)
        shoot(n, info, target+1, state, score)
        state[target] = 0

        
def solution(n, info):
    global max_score, final_state
    max_score = sum(i-10 if info[i] else 0 for i in range(len(info)))
    final_state = [0]*11
    shoot(n, info, 0, [0]*11, max_score)
    return final_state if max_score > 0 else [-1]