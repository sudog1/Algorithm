def time_to_min(time):
    start, end = time
    s_h, s_m = map(int, start.split(':'))
    e_h, e_m = map(int, end.split(':'))
    return [s_h*60+s_m, e_h*60+e_m]

def solution(book_time):
    acc_client = [0]*(24*60+10)
    book_min = list(map(time_to_min, book_time))
    for start_min, end_min in book_min:
        acc_client[start_min] += 1
        acc_client[end_min+10] -= 1
    for i in range(0, len(acc_client)-1):
        acc_client[i+1] += acc_client[i]
    return max(acc_client)