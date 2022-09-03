class Two_Pointers:
    def target_sum(self,arr,target):
        i=0
        j=len(arr)-1
        while i<j:
            our_sum=arr[i]+arr[j]
            if our_sum<target:
                i+=1
            elif our_sum>target:
                j-=1
            else:
                return [i,j]
            
t=Two_Pointers()
assert t.target_sum([1, 2, 3, 4, 6],6)==[1,3]
assert t.target_sum([2, 5, 9, 11],11)==[0,2]