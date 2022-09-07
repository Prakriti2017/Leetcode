class TwoPointers:
    def findTriplets(self, arr):
        result=set()
        arr=sorted(arr)
        for i in range(len(arr)-2):
            j=i+1
            k=len(arr)-1
            while j<k:
                if arr[i]+arr[j]+arr[k]>0:
                    k-=1
                elif arr[i]+arr[j]+arr[k]<0:
                    j+=1
                else:
                    result.add((arr[i],arr[j],arr[k]))
                    k-=1
                    j+=1
        return result

t=TwoPointers()
assert t.findTriplets([-3, 0, 1, 2, -1, 1, -2])==((-3, 1, 2), (-2, 0, 2), (-2, 1, 1), (-1, 0, 1))