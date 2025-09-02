class Solution
{
    public int removeDuplicates(int[] nums)
    {
        int tail = 1;
        for (int i=1; i<nums.length; i++)
        {
            if (nums[i-1] != nums[i])
            {
                nums[tail++] = nums[i];
            }
        }
        return tail;
    }
}