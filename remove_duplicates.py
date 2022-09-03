class TwoPointers:
    def remove_duplicates(self, arr):
        j=1
        for i in range(1,len(arr)):
            if arr[i]!=arr[i-1]:
                arr[j]=arr[i]
                j+=1
        return j

t=TwoPointers()
assert t.remove_duplicates([2, 3, 3, 3, 6, 9, 9])==4
assert t.remove_duplicates([2, 2, 2, 11])==2