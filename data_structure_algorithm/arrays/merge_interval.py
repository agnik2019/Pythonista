# Given a list of intervals, merge all the overlapping intervals 
# to produce a list that has only mutually exclusive intervals.

'''

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("["+str(self.start)+", "+str(self.end)+"]",end='')

def merge(intervals):
    merged = []
    if len(intervals)<2:
        return intervals
    intervals.sort(key= lambda x: x.start)
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1,len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(end,interval.end)
        else:
            merged.append(Interval(start,end))
            start = interval.start
            end = interval.end

    merged.append(Interval(start,end))

    return merged

def main():
    print("Merged intervals: ",end='')
    for i in merge([Interval(1,4), Interval(2,5),Interval(7,9)]):
        i.print_interval()

main()

'''

def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if len(intervals) < 2:
        return intervals
    merged = []
    
    intervals.sort(key = lambda x : x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1,len(intervals)):
        interval = intervals[i]
        if interval[0] <= end:
            end = max(interval[1],end)
        else:
            merged.append([start,end])
            start = interval[0]
            end = interval[1]
    merged.append([start,end])     
    
    return merged

intervals = [[1,4],[0,4]]
print(merge(intervals))