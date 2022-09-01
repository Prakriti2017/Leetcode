class Solution:
    def sums(self,nums,s):
        nums=sorted(nums)
        i=0
        j=len(nums)-1
        while i<len(nums):
            if(nums[i]+nums[j])>s:
                j-=1
            elif(nums[i]+nums[j])<s:
                i+=1
            else:
                print(nums[i],nums[j])
                return True
        return  False

so=Solution()
assert so.sums([5,7,1,2,8,4,3],12)==True