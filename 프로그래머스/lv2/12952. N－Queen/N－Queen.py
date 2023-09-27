def is_occupied(c, m_d, s_d):
    return col_occ[c] or main_diag_occ[m_d] or skew_diag_occ[s_d]

def toggle_occupy(c, m_d, s_d):
    col_occ[c] = 1-col_occ[c]
    main_diag_occ[m_d] = 1 - main_diag_occ[m_d]
    skew_diag_occ[s_d] = 1 - skew_diag_occ[s_d]
    
def bt(n, r):
    if r >= n:
        return 1
    count = 0
    for c in range(n):
        m_d = r-c
        s_d = r+c
        if is_occupied(c, m_d, s_d):
            continue
        toggle_occupy(c, m_d, s_d)
        count += bt(n, r+1)
        toggle_occupy(c, m_d, s_d)
    return count


def solution(n):
    global col_occ, main_diag_occ, skew_diag_occ
    col_occ = [0]*n
    main_diag_occ = [0]*(2*n-1)
    skew_diag_occ = [0]*(2*n-1)
    return bt(n, 0)