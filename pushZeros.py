class Solution:
    def pushZero(self,nums):
        count=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]!=0):
                nums[count]=nums[i]
                count-=1
        while count>=0:
            nums[count]=0
            count-=1
        print(nums)
        return nums
so=Solution()
assert so.pushZero([1,10,20,0,59,63,0,88,0])==[0,0,0,1,10,20,59,63,88]
