class Solution {
    // O(nlog(n)), sort trick
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}