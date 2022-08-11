class Solution:
    def summ(self, nums, k):
        d=dict()
        for i in range(len(nums)):
            if (k-nums[i]) in d.values():
                return True
            else:
                d[i]=nums[i]
        return False

so=Solution()
assert so.summ([1,2,3,4,5],7)==True