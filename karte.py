line = input()
cards = []
p_count = 13
k_count = 13
h_count = 13
t_count = 13
i = 0
while i < len(line):
    cards.append(line[i:i + 3])
    i += 3
i = 0
check = 0
while i < len(cards):
    j = i + 1
    while j < len(cards):
        if cards[i] == cards[j]:
            check = 1
        j += 1
    i += 1

if check == 1:
    print("GRESKA")
else:
    i = 0
    while i < len(cards):
        if cards[i][0] == "P":
            p_count -= 1
        elif cards[i][0] == "K":
            k_count -= 1
        elif cards[i][0] == "H":
            h_count -= 1
        elif cards[i][0] == "T":
            t_count -= 1
        i += 1
    print(p_count, k_count, h_count, t_count)