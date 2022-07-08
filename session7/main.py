#key:value
car = {
    "company" : "benz" ,
    "model" : "c200",
    "price" : 2000,
}

# print(car.values())
# if "color" in car:
#     print("exist")
# else:
#     print("not exist")

# car["company"]="bmw"

# car.update({"company":"saipa"})

# car["color"]="red"

# car.update({"color": "red"})

# car.pop("company")


# print(car)


# for item in car:
#     print(car[item])

# for value in car.values():
#     print(value)

# for key in car.keys():
#     print(key)

for key,value in car.items():
    print(key,value)