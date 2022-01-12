class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i=0
        j=len(nums)-1
        sortedNums=sorted(nums)
        sums=set()
        for k in range(len(nums)):
            i=0
            j=len(nums)-1
            while(i<j):
                if( i==k):
                    i+=1
                if(j==k):
                    j-=1                   
                if((sortedNums[i]+sortedNums[j]+sortedNums[k])<0):
                    i+=1
                elif((sortedNums[i]+sortedNums[j]+sortedNums[k])>0):
                    j-=1
                else:
                    l=sorted([sortedNums[i],sortedNums[j],sortedNums[k]])
                    sums.add(tuple(l))
                    break
        result=[]
        for i in sums:
            result.append(list(i))

        return list(result)

s=Solution()
assert s.threeSum([-1,0,1,2,-1,-4])==[[-1,0,1],[-1,-1,2]]
                    
                
                
           