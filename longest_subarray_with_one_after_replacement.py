from unittest.util import _MAX_LENGTH


class Subarray:
    def one_replacement(self,arr,k):
        l=0
        max_length=0
        frequency_of_1=0
        for r in range(len(arr)):
            if arr[r]==1:
                frequency_of_1+=1
            while (r-l+1)-frequency_of_1>k:
                if arr[l]==1:
                    frequency_of_1-=1
                l+=1
            max_length=max(max_length,r-l+1)
        return max_length
s=Subarray()
assert s.one_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],2)==6
assert s.one_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],3)==9
assert s.one_replacement([],0)==0
                
