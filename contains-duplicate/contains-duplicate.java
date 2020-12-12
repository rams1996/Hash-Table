class Solution {
    public boolean containsDuplicate(int[] nums) {
        int f=0;
        Arrays.sort(nums);
        for(int i=0;i<nums.length-1;i++)
        {
            if(nums[i]==nums[i+1])
            {
                f=1;
                break;
            }
        }
        if(f==1)
            return true;
        else return false;
    }
}
