l=[1,2,3,4,5,6]
max=min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print("max:",max)
print("min:",min)



l=[1,2,3,9,4,5,9,4,6,2,6,6]
print("occurrence of 9:",l.count(9))
print("occurrence of 4:",l.count(4))
print("occurrence of 6:",l.count(6))



l=[1,2,3,4,5,6]
l.sort()
print("ascending:",l)
l.sort(reverse="true")
print("descending:",l)
