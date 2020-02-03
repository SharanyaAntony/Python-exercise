
#day 5 Binary Representation
num=int(input("Enter the Number"))
def bin(i):
    if i>1:
        bin(i//2)
    print(i%2,end=" ")
bin(num)
print()
