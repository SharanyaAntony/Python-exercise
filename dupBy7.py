#4.day 5
from array import *
ar =array('i',[12, 90, 34, 78, 11, 90])
for yet in ar:print(yet)
num=int(input("enter the num"))
def findDup(start=0,end=len(ar)):
    if start<=end:
        if ar[start] == ar[start+1]:
            print(ar[start]," is duplicate")
            if ar[start]%num:
                print(ar[start])
    start += 1;
    findDup(start, end)
findDup()
print()
