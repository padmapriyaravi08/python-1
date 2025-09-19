class ebill:
    def __init__(self,a,b,c,d,e,f):
        self.cno=a
        self.cname=b
        self.caddr=c
        self.curr_unit=d
        self.pre_unit=e
        self.amount=f


    def calculate(self):
        self.unit=self.curr_unit-self.pre_unit
        self.amount=self.curr_unit*self.pre_unit


    def display(self):
        print("consumer no:",self.cno)
        print("consumer name:",self.cname)
        print("consumer address:",self.caddr)
        print("current unit:",self.curr_unit)
        print("previous unit:",self.pre_unit)
        print("amount:",self.amount)


x=int(input("enter consumer no:"))
y=input("enter consumer name:")
z=input("enter consumer address:")
p=int(input("current unit:"))
r=int(input("previous unit:"))
s=int(input("amount:"))


obj=ebill(x,y,z,p,r,s)
obj.calculate()
obj.display()
            
