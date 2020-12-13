class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newArr=[0]*len(nums)
        count=0
        for i in nums:
            for j in nums:
                if j<i:
                    newArr[count]+=1
            count+=1
        return newArr
                    
            
        
