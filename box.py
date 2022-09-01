class Box:
    def numBoxingWays(self, weight_range, max_weight):
        weight_list=[i for i in range(1,weight_range+1)]
        result=[]
        def dfs(i, cur,total):
            if total==max_weight:
                result.append(cur.copy())
                return
            if i>=len(weight_list) or total>max_weight:
                return
            cur.append(weight_list[i])
            dfs(i,cur,total+weight_list[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return len(result)


b1=Box()
assert b1.numBoxingWays(2,7)==4
