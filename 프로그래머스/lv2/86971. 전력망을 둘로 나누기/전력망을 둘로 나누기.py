def divide_power(tree, visit, cur_node, count_arr):
    total = 1
    for child in tree[cur_node]:
        if visit[child]:
            continue
        visit[child] = 1
        result = divide_power(tree, visit, child, count_arr)
        total += result
        count_arr[1] = min(abs(2*result-count_arr[0]), count_arr[1])
    return total


def solution(n, wires):
    tree = [[] for _ in range(len(wires)+2)]
    node_count = 1
    visit = [0]*(len(wires)+2)
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)
        node_count += 1
    count_arr = [node_count, node_count]
    divide_power(tree, visit, 1, count_arr)
    return count_arr[1]