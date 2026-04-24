class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        all=[[] for i in range(27)]
        index=0
        for i in board:
            bucket=all[index]
            for j in i:
                bucket.append(j)
            index+=1
        for i in range(0,9):
            bucket=all[index]
            index+=1
            for j in range(0,9):
                bucket.append(board[j][i])
        for i in range(0,3):
            start=i*3
            for j in range(0,3):
                end=j*3
                bucket=all[index]
                index+=1
                for k in range(start,start+3):
                    for v in range(end,end+3):
                        bucket.append(board[k][v])
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!=".":
                    if (all[i].count(board[i][j]))>1:
                        return (False)
                    if (all[i+9].count(board[i][j])>1):
                        return (False)
                    val1=(i)//3
                    val2=(j)//3
                    check=(val1*3)+val2
                    if (all[check+18].count(board[i][j])>1):
                        return (False)                
        return (True)