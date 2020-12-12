class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic={0:-1}
        level=0
        maximum=0
        for i in range(len(nums)):
            if nums[i]==1:
                level+=1
            else:
                level-=1
            if level in dic:
                if i-dic[level]>maximum:
                    maximum=i-dic[level]
            else:
                dic[level]=i
        return maximum
                
        
