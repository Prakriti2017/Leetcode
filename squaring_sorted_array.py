class TwoPointers:
    def square_sorted_array(self,arr):
        output=[]
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i]**2>arr[j]**2:
                output.append(arr[i]**2)
                i+=1
            else:
                output.append(arr[j]**2)
                j-=1
        output.append(arr[i]**2)
        return output[::-1]

t=TwoPointers()
assert t.square_sorted_array([-2, -1, 0, 2, 3])==[0, 1, 4, 4, 9]
assert t.square_sorted_array([-3, -1, 0, 1, 2])==[0 ,1,1, 4, 9]