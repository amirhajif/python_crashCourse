class Product:
    def __init__(self,name,price,count):
        #Constructor
        self.name=name
        self.price=price
        self.count=count

    def calculateValue(self):
        return self.count*self.price

    #set&get for name
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name

    #set&get for price
    def setPrice(self,price): 
        self.price=price

    def getPrice(self):
        return self.price

    #set&get for count
    def setCount(self,count):
        self.count=count

    def getCount(self):
        return self.count


product1=Product("phooe",200,6)

product1.setName("phone")

print(product1.getName())