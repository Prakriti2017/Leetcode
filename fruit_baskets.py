class Fruits:
    def max_fruit_count(self,arr):
        l=0
        max_count=float("-inf")
        basket={}
        for r in range(len(arr)):
            basket[arr[r]]=1+basket.get(arr[r],0)
            while len(basket)>2:
                left_tree=arr[l]
                basket[left_tree]-=1
                if basket[left_tree]==0:
                    del basket[left_tree]
                l+=1
            max_count=max(max_count,sum(basket.values()))
        return max_count

f=Fruits()
assert f.max_fruit_count(['A', 'B', 'C', 'A', 'C'])==3
assert f.max_fruit_count(['A', 'B', 'C', 'B', 'B', 'C'])==5
