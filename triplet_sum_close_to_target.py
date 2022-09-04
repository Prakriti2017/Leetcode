class TwoPointers:
    def find_triplet(self,arr,target):
        min_diff=float("inf")
        arr=sorted(arr)
        for i in range(len(arr)-2):
            l=i+1
            r=len(arr)-1
            while l<r:
                triplet_sum=arr[i]+arr[l]+arr[r]
                diff=target-triplet_sum
                if diff==0:
                    return triplet_sum
                if abs(diff)<abs(min_diff):
                    min_diff=diff
                if min_diff>0:
                    l+=1
                else:
                    r-=1
        return target-min_diff

t=TwoPointers()
assert t.find_triplet([-2, 0, 1, 2],2)==1
assert t.find_triplet([-3, -1, 1, 2],1)==0