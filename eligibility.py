n = int(input())
i = 0

while i < n:
    line = input()
    line = line.split(" ")
    name = line[0]
    pdate = int(line[1][0:4])
    dob = int(line[2][0:4])
    amt = int(line[3])
    list = []
    list.append(name)
    list.append(pdate)
    list.append(dob)
    list.append(amt)
    if pdate >= 2010 or dob >= 1991:
        print(name, "eligible")
    elif pdate < 2010 and dob < 1991 and amt > 40:
        print(name, "ineligible")
    else:
        print(name, "coach petitions")
    i += 1