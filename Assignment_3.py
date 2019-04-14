

print("---------------------------------------------------------Nested for loop example ---------------------------------------------------------------------")
a=33
b=300
c=200
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equalto b")
else:
    print("a is not greater than b")

for i in range(0,20):
    print(i,"-",end=" ")
    for j in range(0,10):
        if j%2==0:    
            print(j,end=" ")
    print("\n",end="")
print("\n---------------------------------------------------------Abstract class example ---------------------------------------------------------------------")
from abc import ABC,abstractmethod
class AbstractCurry(ABC):
    def __init__(self,name):
        self.name=name
        super().__init__()
    #@abstractmethod   
    def Ingredients(self):
        pass
    #@abstractmethod
    def smell(self):
        pass
class MushroomCurry(AbstractCurry):
    def __init__(self,curryname):
        super().__init__(curryname)
        print("The name of curry is %s"%self.name)
    def Ingredients(self):
        print("The main Ingredients of Mushroom curry are Mushrooms and Tomato")
    def smell(self):
        print("The smell of Mushroom is similar to chicken curry")
def main():
    print("Program execution starts")
main()    
mc=MushroomCurry("Mushroom masala")
mc.Ingredients()
mc.smell()               
c=AbstractCurry("Mushroom masala")
   
