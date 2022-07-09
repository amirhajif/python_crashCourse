class Product:

    discount = 0.8 #class Attribute

    def __init__(self,name:str,price,count=6):
        #Constructor
        self.name=name
        self.price=price
        self.count=count

    def calculateValue(self):
        return self.count*self.price*self.discount

product1=Product("phone",200)

# print(product1.count)


# product2=Product()



product1.discount=0.5
print(product1.calculateValue())

# print(Product.discount)
# print(product1.discount)