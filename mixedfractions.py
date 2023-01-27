import sys
inputs = sys.stdin.readlines()
for i in range(len(inputs)):
    position = inputs[i].strip().split()
    if len(position) > 1:
        num = int(position[0])
        den = int(position[1])
        if num == 0 and den == 0:
            break
        else:
            remainder = (num // den)
            mod = (num % den)
            print(remainder, mod, "/", position[1])