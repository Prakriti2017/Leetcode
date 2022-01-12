"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        starts=sorted([interval.start for interval in intervals])
        ends=sorted([interval.end for interval in intervals])
        j=0
        count=0
        i=0               
        minCount=0
        while i<(len(intervals)):
            if(starts[i]<ends[j]):
                i+=1
                count+=1
            else:
                count-=1
                j+=1
            minCount=max(minCount,count)
        return minCount

