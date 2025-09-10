d={"eno":666,"ename":"xyz"}
print(d)
print(d["eno"])
print(d.get("ename"))
d["eno"]=126
print(d)
d["age"]=20
print(d)
for key in d:
    print(key)
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,":",value)
d.pop("eno")
print(d)
d.popitem()
print(d)
d.clear()
print(d)
