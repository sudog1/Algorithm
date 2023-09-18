from collections import defaultdict

def solution(rows, columns, queries):
    answer = []
    matrix = defaultdict(dict)
    number = 1
    for row in range(1, rows+1):
        for col in range(1, columns+1):
            matrix[row][col] = number
            number += 1
    for query in queries:
        row = query[0]
        col = query[1]
        col_move = query[3] - query[1]
        row_move = query[2] - query[0]
        index = []
        value = []
        for _ in range(col_move):
            value.append(matrix[row][col])
            col += 1
            index.append([row, col])
        for _ in range(row_move):
            value.append(matrix[row][col])
            row += 1
            index.append([row, col])
        for _ in range(col_move):
            value.append(matrix[row][col])
            col -= 1
            index.append([row, col])
        for _ in range(row_move):
            value.append(matrix[row][col])
            row -= 1
            index.append([row, col])
        answer.append(min(value))
        for index, value in zip(index, value):
            row, col = index
            matrix[row][col] = value
            
    return answer