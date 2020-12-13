class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        m={}
        result=[]
        for i in names:
            if i not in m:
                result.append(i)
                m[i]=1
            
            else:
                
                val=i+'('+str(m[i])+')'
                while val in m:
                    m[i]+=1
                    val=i+'('+str(m[i])+')'
                result.append(val)
                m[val]=1
                        
        return result
                    
                
        
        
