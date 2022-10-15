a = []
b = []

for i in range(3):
    a.append(str(input()))
    b.append(len(a[i]))

maxs = max(b)
mins = min(b)

for i in a:
    if len(i) == maxs:
        maxc = i
    elif len(i) == mins:
        minc = i

print(minc + maxc)