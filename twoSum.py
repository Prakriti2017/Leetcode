class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(nums)-1
        sortedNum=sorted(nums)
        result=[]
        while(i<j):
            if(i==j):
                continue
            if((sortedNum[i]+sortedNum[j])>target):
                j-=1
            elif((sortedNum[i]+sortedNum[j])<target):
                i+=1
            else:
                result.append(sortedNum[i])
                result.append(sortedNum[j])
                break
        return nums.index(result[0]),nums.index(result[1])
    
s= Solution()
assert s.twoSum([3,3],6)== [0,1]