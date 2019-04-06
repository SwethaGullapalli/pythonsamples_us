#wap to create ten real classes

class Curry(object):
    type="Eatable"
    def __init__(self,name,colour,taste,consistency):
        self.name=name
        self.colour=colour
        self.taste=taste
        self.consistency=consistency
    def description(self):
        return"the name of curry is %s and %s in colour and %s in taste"%(self.name,self.colour,self.taste)    
        
    def smelling(self,smell):
        return "%s smells very %s"%(self.name,smell)    
Dalcurry=Curry("dalcurry","yellow","spicy","semi solid")
print (Dalcurry.description())
print (Dalcurry.smelling("Aromatic"))
class Mangodal(Curry):
    def __init__(self,name,colour,taste,consistency,ingredient):
        Curry.__init__(self,name,colour,taste,consistency)
        self.ingredient=ingredient
    def Cookprocess(self): 
        return self.description
M= Mangodal("Mangodal","yellow","delicious","solid","Mango")
print (M.description())
print (M.smelling("Delicious"))
print (M.Cookprocess())



class Mother:
    type="Human"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def teach(self,storybook):
        return "%s reads the book %s to the kid "%(self.name,storybook)
    def cooking(self,dish):
        return "%s cooks %s to the kid"%(self.name,dish)
    def play(self,game):
        return "%s plays the game %s with the kid"%(self.name,game)
Swetha=Mother("Swetha",30)
print(Swetha.teach("llama llama"))
print(Swetha.cooking("Noodles"))
print(Swetha.play("Candy crush"))      

class Tv:
    type="Electronics"
    def __init__(self,name,yom,display,tvtype):
        self.name=name
        self.yom=yom
        self.display=display
        self.type=tvtype
    def Display(self,picturequality):
        return"The %s display picture is of %s quality which is %s type"%(self.name,picturequality,self.type)
LG=Tv("Lg",2017,"LED","Smart") 
print(LG.Display("HD"))

class Sofa:
    def __init__(self):
        print ("Calling Constructor")
        Sofa.name="Ikea"
        Sofa.color="Orange"

    def bed(self,model):
        print("The main use of %s Sofa is its convertibility %s Model and its wide range of %s"%(self.name,model,self.color))
IKEA=Sofa()
print(IKEA.bed("Pull")) 
#Sofa.name="Ikea"
#Sofa.color="Orange"
#yom="2018" 

class Wallclock:
    def __init__(self):
        Wallclock.name="Quartz"
        Wallclock.numbers="Roman"
        Wallclock.shape="Round"
        Wallclock.color="Black"
        Wallclock.smallhand="hours"
        Wallclock.bighand="minutes"
    def displaytime(self,hours,minutes):
        return"The  %s clock time is %s:%s pm"%(Wallclock.name,hours,minutes)
quartz=Wallclock()
print(quartz.displaytime(2,30))   


class Phone:
    def __init__(self,brand,width,height,OS,price):
        self.brand=brand
        self.width=width
        self.height=height
        self.OS=OS
        self.price=price
    def sendmessage(self):
        print ("hi,how are you")
    def call(self):
        print ("calling friend")
    def openbrowser(self):
        print ("opening browser")
    def share(self):
        print ("sharing files")
Iphone=Phone("iphone","23","45","Android","$3200")  
print(Iphone.sendmessage())
print(Iphone.call())
print(Iphone.openbrowser())
print(Iphone.share())      

class Pen():
    def __init__(self,color,name):
        self.color=color
        self.name=name
    def Writing(self,message):
        return"The %s pen message is %s"%(self.name,message)
Cello=Pen("RED","cello")
print (Cello.Writing("Hi I am cello"))   


class House:
    def __init__(self,name,floors,pillarsheight,rooflength):
        self.name=name
        self.floors=floors
        self.pillarsheight=pillarsheight
        self.rooflength=rooflength
    def playschool(self):
        return"Swetha's  house can function as a preschool"
    def office(self):  
        return"Swethas house can function as a office"
Swethahouse=House("Swetha",3,115,34)
print(Swethahouse.playschool())
print(Swethahouse.office())  

class Statue:
    def __init__(self,name,color,clay):
        self.name=name
        self.color=color
        self.clay=clay
    def Blessings(self,Energy):
        return"Goddess blessed us with %s"%(Energy)
Durga=Statue("durga","skincolor","mud")   
print(Durga.Blessings("Consciousness")) 

"""class TAASC_Throwball:
    TeamDhangal_Score=0
    TeamSpikers_Score=0
    Gamepoint=0
    bool netball,bool Serviceball,bool Underhand,bool doubletouch,bool doublehandsinrally
    def __init__(self,size):
        self.size=size
    def GameRules(self):
        if netball==True:
            Gamepoint+=1
        elif Serviceball==True:
            Gamepoint+=1    
        elif Underhand==True:
            Gamepoint+=1
        elif doubletouch==True:classmethod
            Gamepoint+=1
        elif doublehandsinrally==False:
            Gamepoint+=1
    def Team_Score(self):
        if(DhangalTeam.GameRules()==True):
            TeamDhangal_Score==Gamepoint
        else:    
            TeamSpikers_Score==Gamepoint
    def Winners(self):
        if(TeamDhangal_Score>TeamSpikers_Score):
            print("Team Dhangal are the Winners")
        elif:
            print("Team Spikers sre the Winners")    
DhangalTeam=Throwball(6)
SpikersTeam=Throwball(6)
print(DhangalTeam.GameRules())
print(SpikersTeam.GameRules())
print(DhangalTeam.Team_Score())
print(SpikersTeam.Team_Score())
print(DhangalTeam.Winners())
print(SpikersTeam.Winners())"""














