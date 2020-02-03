#2.day5
from array import *
ar =array('i',[12, 90, 34, 78, 11, 90])
def findDup(start=0,end=len(ar)):
    if start<=end:
        if ar[start] == ar[start+1]:
            print(ar[start]," is duplicate")
        start+=1;findDup(start,end)
    else:
        return
findDup()
print()

