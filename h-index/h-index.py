class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        
        low=0
        high=len(citations)-1
        result=0
        while low<=high:
            mid=(low+high)//2
            diff=len(citations)-mid
            if citations[mid]<diff:
                low=mid+1
            else:
                result=diff
                high=mid-1
        return result
                
            
​
​
​
        
