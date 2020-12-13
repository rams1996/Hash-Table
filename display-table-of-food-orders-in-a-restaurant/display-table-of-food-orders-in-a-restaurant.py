class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        from collections import deque
        menuSet=set()
        header=[]
        for i in orders:
            if i[-1] not in menuSet:
                menuSet.add(i[-1])
                header.append(i[-1])
        nahMap={}
        header.sort()
        for k in range(len(header)):
            nahMap[header[k]]=k+1
        header.insert(0,"Table")
        tableSet={}
        finalOutput=[]
        finalOutput.append(header)
        for i in orders:
            if i[1] not in tableSet:
                tableSet[i[1]]=[0]*len(header)
                tableSet[i[1]][0]=int(i[1])
            tableSet[i[1]][nahMap[i[-1]]]+=1
        
        abcd=list(tableSet.values())
        abcd.sort()
        for i in range(len(abcd)):
            for j in range(len(abcd[0])):
                abcd[i][j]=str(abcd[i][j])
        for m in abcd:
            finalOutput.append(m)
        return finalOutput
                
            
            
             
        
