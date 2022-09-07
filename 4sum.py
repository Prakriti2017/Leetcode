class TwoPointers:
    def find_quadruplets(self,arr,target):
        result=[]
        for i in range(len(arr)-3):
            for j in range(i+1,len(arr)-2):
                l=j+1
                r=len(arr)-1
                while l<r:
                    our_sum=arr[i]+arr[j]+arr[l]+arr[r]
                    if our_sum<target:
                        l+=1
                    elif our_sum>target:
                        r-=1
                    else:
                        result.append([arr[i],arr[j],arr[l],arr[r]])
                        l+=1
                        while arr[l]==arr[l-1] and l<r:
                            l+=1
        print(result)
        return result

t=TwoPointers()
assert t.find_quadruplets([4, 1, 2, -1, 1, -3],1)==[[-3, -1, 1, 4], [-3, 1, 1, 2]]
