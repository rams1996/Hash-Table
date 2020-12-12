class Solution:
    def isHappy(self, n: int) -> bool:
        add=n
        for i in range(1000):
            num=add
            add=0
            for j in str(num):
                add= add+ (int(j)**2)
            if add==1:
                return True
            
        return False
                
                
            
        
