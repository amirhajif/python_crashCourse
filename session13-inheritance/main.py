# class A:#base
#     def f1(self):
#         print("in f1 method")
#     def f2(self):
#         print("in f2 method")

# class B(A):#derived
#     def f3(self):
#         print("in f3 method")
#     def f4(self):
#         print("in f4 method")

# a=A()
# #a.f2()

# b=B()
# b.f2()

class Person:
    def __init__(self,name,family):
        self.name=name
        self.family=family


class Worker(Person):
    def __init__(self, name, family,salary):
        super().__init__(name, family)
        self.salary=salary

worker = Worker("amir", "hajitabar", 20000)
print(worker.family)
