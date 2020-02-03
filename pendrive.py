#pendrive#pendrive

pen={500:"hp",300:"sandisk",1000:"sony",350:"toshiba"}
amt=0
amt=int(input("Enter the pendrive you wish to remove"))
def dlt(key=0):

    if pen.get(amt):
        del pen[amt]
        print(pen)
        key += 1
        if key>len(pen)-1:
            return
        dlt()
    else:
        return
dlt()
        
            
