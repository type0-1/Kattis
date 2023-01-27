line = input()
line = line.split(" ")
end = (line[0][len(line[0]) - 1])
end2 =(line[0][len(line[0]) - 2:])
check = (line[0][:len(line[0]) - 1])

if end == "e":
    print(line[0] + "x" + line[1])
elif end2 == "ex":
    print(line[0] + line[1])
else:
    if end == "a":
        print(check + "ex" + line[1])
    elif end == "i":
        print(check + "ex" + line[1])
    elif end == "o":
        print(check + "ex" + line[1])
    elif end == "u":
        print(check + "ex" + line[1])
    elif end2 != "ex":
        print(line[0] + "ex" + line[1])