#First N prime numbers

num=int(input("Enter the value of N"))
for pno in range(1,num+1):
    if pno%2!=0:
        num+=1
        print(pno)
    if pno==2:
        print(pno)
        
    
