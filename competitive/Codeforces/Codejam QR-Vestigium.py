for t in range(int(input())):
    n = int(input())
    matrix = [[int(i) for i in input().split()] for j in range(0, n)]
    # print(matrix)

    trace = 0
    col_count = 0
    row_count = 0

    for i in range(n):
        col_bool = 0
        row_bool = 0
        col = {}
        row = {}
        for j in range(n):
            if i == j:
                trace += matrix[i][j]

            if matrix[j][i] in col:
                if not col_bool:
                    col_count += 1
                col_bool = 1
            else:
                col[matrix[j][i]] = 1

            if matrix[i][j] in row:
                if not row_bool:
                    row_count +=1
                row_bool = 1
            else:
                row[matrix[i][j]] = 1
    
    print("Case #{}:".format(t+1), end=" ")
    print(trace, row_count, col_count)
