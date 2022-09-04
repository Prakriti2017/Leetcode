from collections import deque
class TwoPointers:
    def find_products(self,arr,target):
        product=1
        result=[]
        l=0
        for r in range(len(arr)):
            product*=arr[r]
            while product>=target and l<len(arr):
                product/=arr[l]
                l+=1
            store_list=deque()
            for i in range(r,l-1,-1):
                store_list.appendleft(arr[i])
                result.append(list(store_list))
        return result

t=TwoPointers()
assert t.find_products([2, 5, 3, 10],30)==[[2], [5], [2, 5], [3], [5, 3], [10]]
assert t.find_products([8, 2, 6, 5],50)==[[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]