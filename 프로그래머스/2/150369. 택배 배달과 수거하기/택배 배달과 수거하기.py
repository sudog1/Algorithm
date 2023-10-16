def deliver(arr, cap):
    result = []
    while arr:
        cur_cap = cap
        if arr[-1] == 0:
            arr.pop()
        else:
            result.append(len(arr))
            while arr and cur_cap:
                if cur_cap >= arr[-1]:
                    cur_cap -= arr[-1]
                    arr.pop()
                else:
                    arr[-1] -= cur_cap
                    break
    return result
                

def solution(cap, n, deliveries, pickups):
    del_arr = deliver(deliveries, cap)
    pic_arr = deliver(pickups, cap)
    del_len = len(del_arr)
    pic_len = len(pic_arr)
    if del_len >= pic_len:
        arr = del_arr[:]
        comp_len = pic_len
    else:
        arr = pic_arr[:]
        comp_len = del_len
    for i in range(comp_len):
        arr[i] = max(del_arr[i], pic_arr[i])
    return sum(arr)*2