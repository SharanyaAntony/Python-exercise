#1.day5
warehouse = [0]
count = 0


def details(index=0):
    if index < len(warehouse):
        print(warehouse[index])
        index += 1;
        details(index)
    else:
        return


def insert(index=0, end=5, count=0):
    if index < end:
        wish = input("Tell what you wish to do")
        if wish == "give":
            amt = int(input("Tell us the Amount"))
            warehouse.append(warehouse[index] + amt)

        elif wish == "take":
            amt = int(input("Tell us the Amount"))
            warehouse.append(warehouse[index] - amt)

            count += 1

            if count >= 2:
                warehouse.append(warehouse[index] - (amt+20))
            else:
                warehouse.append(warehouse[index] - amt)
        index += 1;insert(index, end, count)


# print(warehouse)
insert(0, 5);
details()
