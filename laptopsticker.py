line = input()
wc, hc, ws, hs = line.split(" ")
wc = int(wc)
hc = int(hc)
ws = int(ws)
hs = int(hs)

if wc - 1 <= ws or hc - 1 <= hs:
    print("0")
else:
    print("1")
    
    
