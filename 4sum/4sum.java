class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        HashSet<List<Integer>> res = new HashSet<>();
        for (int i = 0; i< nums.length - 3; i++)
        {
            int a = nums[i];
            for(int j = i+1; j < nums.length - 2; j++)
            {
                int b = nums[j];
                int start = j + 1;
                int end = nums.length - 1;
                while (start < end)
                {
                    int c = nums[start];
                    int d = nums[end];
                    if (a + b + c + d == target)
                    {
                        res.add(Arrays.asList(a, b, c, d));
                        start = start + 1;
                        end = end - 1;
                    }
                    else if (a + b + c + d > target)
                        end = end - 1;
                    else
                        start = start + 1;
                }
            }
        }
        List<List<Integer>> res1 = new ArrayList<>();
        for(List<Integer> l2: res)
            res1.add(l2);
        return res1;
    }
}
