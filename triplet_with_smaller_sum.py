class TwoPointers:
    def searchTriplets(self,arr,target):
        num_triplets=0
        arr=sorted(arr)
        for i in range(len(arr)-2):
            l=i+1
            r=len(arr)-1
            while(l<r):
                target_sum=arr[i]+arr[l]+arr[r]
                if target_sum<target:
                    num_triplets+=r-l
                    print(num_triplets)
                    l+=1
                else:
                    r-=1
        return num_triplets
t=TwoPointers()
assert t.searchTriplets([-1, 0, 2, 3],3)==2
