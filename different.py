import sys
inputs = sys.stdin.readlines()
i = 0

while i < len(inputs):
    result = inputs[i].strip("\n")
    new_result = result.split(" ")
    if len(new_result) <= 1:
        pass
    else:
        a = new_result[0]
        b = new_result[1]
        if int(a) > int(b):
            print(int(a) - int(b))
        else:
            print(int(b) - int(a))
    i += 1