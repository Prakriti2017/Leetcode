class TwoPointers:
    def sort_objects(self,arr):
        low=0
        high=len(arr)-1
        i=0
        while(i<=high):
            if arr[i]==0:
                arr[low],arr[i]=arr[i],arr[low]
                i+=1
                low+=1
            elif arr[i]==1:
                i+=1
            else:
               arr[high],arr[i]=arr[i],arr[high]
               high-=1
        return arr

t=TwoPointers()
assert t.sort_objects([1, 0, 2, 1, 0])==[0,0,1,1,2]
