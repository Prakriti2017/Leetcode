from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        for i in range(target+1):
            if i in nums:
                dp[i]=1
        for i in range(1,target+1):
            for num in nums:
                if i-num>=0:
                    dp[i]+=dp[i-num]
        return dp[-1]



so=Solution()
assert so.combinationSum4([1],1)==1
assert so.combinationSum4([1,2,3],1)==1
assert so.combinationSum4([1,2,3],4)==7