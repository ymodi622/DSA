mat = [[1,1,1],
       [1,0,1],
       [1,1,1]]
matRow = [0]*len(mat)
matCol = [0]*len(mat[0])
for i in range(len(mat)):
  
    for j in range(len(mat[i])):
        if mat[i][j] == 0:
            matRow[i] = 1
            matCol[j] = 1

# print(matRow)
# print(matCol)

for i in range(len(matRow)):
    if matRow[i] == 1:
        mat[i] = [0]*len(mat)
    for j in range(len(mat[i])):
        if matCol[j] == 1:
            mat[i][j] = 0

# print(mat)
    