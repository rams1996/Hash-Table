class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        i=0
        j=0
        count=0
        m=-float('inf')
        while j<len(s):
            if count==0:
                if s[j] not in freq:
                    freq[s[j]]=1
                    m=max(m,j-i+1)
                else:
                    freq[s[j]]+=1
                    count+=1
                j+=1
            else:
                
                if freq[s[i]]>1:
                    freq[s[i]]-=1
                    count-=1
                    
                elif freq[s[i]]==1:
                    del freq[s[i]]
                
                i+=1
        while count>=1:
            if freq[s[i]]>1:
                    freq[s[i]]-=1
                    count-=1
                    
            elif freq[s[i]]==1:
                del freq[s[i]]
            i+=1
            
        m=max(m,j-i)
        if m==-float('inf'):
            return 0
        return m
            
        
        
            
            
        
