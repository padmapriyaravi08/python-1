class student:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c
    def display(self):
        print("student no:",self.sno)
        print("student name:",self.sname)
        print("student age:",self.sage)


x=int(input("enter your roll no:"))
y=input("enter your name")
z=int(input("enter your age:"))

ob=student(x,y,z)
ob.display()



class student:
    def __init__(self,m1,m2,m3):
        self.m1=x
        self.m2=y
        self.m3=z
    def display(self):
        print("mark in the first sub:",self.m1)
        print("mark in the second sub:",self.m2)
        print("mark in the third sub:",self.m3)


x=int(input("enter m1:"))
y=int(input("enter m2:"))
z=int(input("enter m2:"))

ob=student(x,y,z)
ob.display()
