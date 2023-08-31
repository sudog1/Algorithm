def solution(id_list, report, k):
    report_state = {}
    for a, b in map(lambda x: x.split(), report):
        if b not in report_state:
            report_state[b] = {a}
        else:
            report_state[b].add(a)
    
    receive_mail = {i: 0 for i in id_list}
    for b in report_state:
        if len(report_state[b]) >= k:
            for a in report_state[b]:
                receive_mail[a] += 1
    
    return list(map(lambda x: receive_mail[x], id_list))