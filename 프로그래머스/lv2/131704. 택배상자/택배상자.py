def solution(order):
    boxes = list(reversed([i for i in range(1, len(order)+1)]))
    sub_container = []
    r_order = list(reversed(order))
    while r_order:
        if boxes:
            if boxes[-1] == r_order[-1]:
                boxes.pop()
                r_order.pop()
                continue
            elif boxes[-1] < r_order[-1]:
                sub_container.append(boxes.pop())
                continue
        if sub_container and sub_container[-1] == r_order[-1]:
            sub_container.pop()
            r_order.pop()
        else:
            return len(order) - len(r_order)
    return len(order)