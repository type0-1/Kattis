from datetime import datetime
line = input() 
d, m = line.split(" ") 
result = datetime(2009, int(m), int(d))
print(result.strftime('%A'))