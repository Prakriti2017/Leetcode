from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        diction={}
        def dp(target,nums):
            if len(nums)==0 and target==0:
                return 1
            if len(nums)==0 and target!=0:
                return 0
            if (target,str(nums)) in diction:
                return diction[(target,str(nums))]
            last=nums[-1]
            add=dp(target+last, nums[0:-1])
            sub=dp(target-last, nums[0:-1])
            sums=add+sub
            diction[(target,str(nums))]=sums
            return sums
        return dp(target,nums)

so=Solution()
assert so.findTargetSumWays([],0)== 1
assert so.findTargetSumWays([],1)== 0
assert so.findTargetSumWays([],-1)== 0
assert so.findTargetSumWays([],-5)== 0
print("Passed base cases")

assert so.findTargetSumWays([1,1,1],1)== 3
assert so.findTargetSumWays([1,1,1,1,1],3)== 5