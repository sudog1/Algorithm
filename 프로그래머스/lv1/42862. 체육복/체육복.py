def solution(n, lost, reserve):
    student_state = [0]*(n+2)
    for idx in lost:
        student_state[idx] -= 1
    for idx in reserve:
        student_state[idx] += 1
    
    for i, state in enumerate(student_state):
        if state == -1:
            if student_state[i-1] == 1:
                student_state[i] = 0
            elif student_state[i+1] == 1:
                student_state[i] = 0
                student_state[i+1] = 0
    
    return n + sum(filter(lambda x: x<0, student_state))