from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap=defaultdict(list)
        columnMap=defaultdict(list)
        boxMap=defaultdict(list)
        
        def recursion(row,index):
            nonlocal flag
            if not flag:
                return -1
            if index==len(board[0]):
                return board[row][index-1]
            value=recursion(row,index+1)
            if value!='.':
                if value in rowMap[row]:
                    flag=False
                    return -1
                else:
                    rowMap[row].append(value)
                if value in columnMap[index]:
                    flag=False
                    return -1
                else:
                    columnMap[index].append(value)
                if value in boxMap[(row//3,index//3)]:
                    flag= False
                    return -1
                else:
                    boxMap[(row//3,index//3)].append(value)
            return board[row][index-1]
        globalFlag=True
        flag=True
        def recursion2(row):
            nonlocal flag
            nonlocal globalFlag
            if globalFlag==False:
                return -1
            if row==len(board):
                return row-1
            temp=recursion2(row+1)
            flag=True
            if globalFlag==False:
                return -1
            recursion(temp,0)
            if flag==False:
                globalFlag= False
            return temp-1
        recursion2(0)
        return globalFlag
​
                
        
