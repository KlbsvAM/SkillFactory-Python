
class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def get_area (self):
        return self.a*self.b
class Square:
    def __init__(self,a):
        self.a=a
    def get_area_square(self):
        return self.a*self.a
class Circle:
    def __init__(self,r):
        self.r=r
    def get_area_circle(self):
        return 3.14*self.r**2
class Treug:
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def __str__(self):
        return f"Treug : {self.b,self.h}"
    def get_area_treug(self):
        return 0.5*self.b*self.h
class Client:
    def __init__(self,name,last_name,city,balance):
        self.name=name
        self.last_name=last_name
        self.city=city
        self.balance=balance
    def __str__(self):
        return f"{self.name} {self.last_name}. {self.city}.Баланс:{self.balance} руб."
    def guests(self):
        return f"{self.name} {self.last_name}. {self.city}."
client_1=Client("Иван","Петров","Москва",100)
client_2=Client("Андрей","Иванов","Москва",50)
client_3=Client("Артем","Ким","Москва",75)
guests_corp=[client_1,client_2,client_3]
for guest in guests_corp:
    print(guest.guests())


