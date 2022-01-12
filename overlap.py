class Solution:
    def mergeIntervals(self,intervals):
        starts=sorted([interval[0] for interval in intervals ])
        ends=sorted([interval[1] for interval in intervals ])      
        merged=[]
        newStart=0
        j=0
        for i in range(len(starts)):
            if(starts[i]<ends[j]):
                continue
            else:
                j+=1
                print(starts[i],ends[j])
                if(i==(len(starts)-1)):
                    merged.append([starts[newStart],ends[len(ends)-1]])
                else:
                    merged.append([starts[newStart],ends[j]])
                newStart=i

            
        print(merged)
        return merged

s=Solution()
s.mergeIntervals([[2,4], [5,7], [1,3], [6,8],[15,17]])
