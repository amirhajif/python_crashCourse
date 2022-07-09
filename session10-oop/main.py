#store
#oop object oriented programming
# product1_name="phone"
# product1_price=2000
# product1_count=6

# product2_name="laptop"
# product2_price=3000
# product2_count=16

# product3_name="tablet"
# product3_price=2500
# product3_count=4

class Product:
    def calculateValue(self,price,count):
        return price*count

product1=Product()

product1.name="phone"
product1.price=2000
product1.count=6



print(product1.calculateValue(product1.price,product1.count))

# word="amir"
# print(word.capitalize())

product2=Product()
