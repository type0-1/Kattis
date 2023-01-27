view1 = 10
view2 = 30
view3 = 10
n = int(input())
option2 = 100 - n
win1 = ((view1 / n) * 100 / 1)
win2 = ((view2 / n) * 100 / 1)
win3 = ((view3 / option2) * 100 / 1)
amount = win1 + win2
print(amount / (view1 + view2))
print(win3 / view3)
