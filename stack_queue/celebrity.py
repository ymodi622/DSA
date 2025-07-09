def celebrity(mat):
    n = len(mat)
    top = 0
    bot = n - 1

    while top < bot:
        if mat[top][bot] == 1:
            top += 1
        else:
            bot -= 1

    # Verify if the candidate is a celebrity
    for i in range(n):
        if i == top:
            continue
        if mat[top][i] != 0 or mat[i][top] != 1:
            return -1

    return top


print(celebrity([[1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1]]))
