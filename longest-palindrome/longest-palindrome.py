class Solution:
    def longestPalindrome(self, s: str) -> int:
        pair=set()
        count=0
        for i in s:
            if i not in pair:
                pair.add(i)
            else:
                pair.remove(i)
                count+=2
        if len(pair)!=0:
            count+=1
        return count
                
        
