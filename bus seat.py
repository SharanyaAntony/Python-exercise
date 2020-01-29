#bus seat arrangement

chart=""
for row in range(1,2):
    for seat in range (1,5):
        amt=int(input("amount you have: "))
        if amt>=200:
            print("Ur seat no: ",row,seat)
            chart+="$"
            if seat%2==0:
                chart+="    "
        else:
            chart+="#"
        
    chart+="\n"
print(chart)
