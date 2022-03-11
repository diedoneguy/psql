# class Cars:
#     mark = "lexus"
#     year = "2004"
# bmw = Cars()
# bmw.mark = "bmw"
# bmw.year = "2004"
# print(bmw.mark,bmw.year)

# tesla = Cars()
# tesla.mark = "tesla"
# tesla.year = "2201"
# print(tesla.mark,tesla.year)

# masserati = Cars()
# masserati.mark = "masserati"
# masserati.year = "2012"
# print(masserati.car,masserati.year)


# import random
# succe = random.randint(1,10)
# print(succe)
# i = 0
# while i > 3:
# sa = int(input("введите число"))
# if succe != sa:
#     print('LOOSER')
# else:
#     print('winner')

# class Person:
#     name = "vlad"
#     age = "25"

#     def dicplay_person(self):
#         return f'hello {self.name}, your age {self.age}'
# a = Person().dicplay_person()
# b = Person()
# b.name = 'Glent'
# b.age = '25'
# print(b.dicplay_person()) 
#     # phone = 'iphone'
# #     year = '2012'
# # iphone7 = telephone
# # iphone7.name = 'iphone7'
# # def__init__(self,iphone.name) 
# class People:
#     name = 'serega'
#     age = '25'
# names = People



# from curses import keyname
# from dataclasses import dataclass
# from types import MemberDescriptorType
# from typing import KeysView
# from typing_extensions import Self
# from unicodedata import name
# from defer import return_value

# from paramiko import Agent


from shutil import SpecialFileError


class Dog:
    name = 'Rex'
    noise = 'woof'
    def say(self):
        return f'my dog {self.name},{self.noise*18}'
d = Dog().say()
print(d)

# class Employee:
#     emplCount = 0
#     def __init__(self,name,age,salary)->None:
#         self.a = age
#         self.n = name
#         self.s = salary
#         Employee.emplCount()
#     def display
# 
''' 
class Notebook:
    #  def __init__(self,cpu,ozu,videocard,hdd,motherboard,displaysize) -> None:
        name = 'PackardBell'
        cpu  = '4 ядерный'
        memory = '6гб'
        videocard = 'intelgraphics'
        hdd = '240гб'
        motherboard = 'packardbell'
        displaysize = '1900*1200'
        def fredde(self):
            # return f'your cpu {self.cpu},memoru {self.memory},videocard {self.videocard},'
            return{'name': self.name,'cpu':self.cpu,'memory': self.memory,'videocard': self.videocard,}
c = Notebook().fredde()
print(c)

class DANNUE:
    def __str__(self):
        return('colors')
colors = {
"black": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,255,255,1],
"hex": "#000"
}
},
"white": {
"category": "value",
"code": {
"rgba": [0,0,0,1],
"hex": "#FFF"
}
},
"red": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,0,0,1],
"hex": "#FF0"
}
},
"blue": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [0,0,255,1],
"hex": "#00F"
}
},
"yellow": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,255,0,1],
"hex": "#FF0"
}
},
"green": {
"category": "hue",
"type": "secondary",
"code": {
"rgba": [0,255,0,1],
"hex": "#0F0"
}
}
}

def get__init__(self,name_dictionary):
    return{'colors': self.keys}
def get_values_set(self):
    values1 = []
    def get_values_in_set(c):
        for i in c.values():
            if type(i) is dict:
                get_values_in_set(i)
            else:
                values1.append(i)
    get_values_in_set(self.color)
    return values1
'''

# class Hostel:
#     def __str__(self):
#         return f'hello {self.name}, your age {self.posititon}'
    
#     data = {
#     "markers": [
#     {
#     "name": "Rixos The Palm Dubai",
#     "position": [25.1212, 55.1535],
#     },
#     {
#     "name": "Shangri-La Hotel",
#     "location": [25.2084, 55.2719]
#     },
#     {
#     "name": "Grand Hyatt",
#     "location": [25.2285, 55.3273]
#     }
#     ]
#     }
#     erem = {}
    # def __str__(self):
    #     return f'hell {self.markers},{self.position}'
    # b = data(name).position()
    # print(b)
    # for lop in data:
    #     lop == set
    #     print(lop)
    #     if dict in data:
    #         dict.append(erem)
    #     erem = erem.get.dict ( [])
    #     print(erem)










    # def brawlstars(self):
    #     return{name: self.data,}
    # for i in data:
    #     if i in data.name():
    #         print(data)
    # def __init__ (self,markers):
    #     return{'data': self.keys}
    # def get_values_set(self):
    #     values1 = []
    #     def get_values_in_set(c):
    #         for i in c.values():
    #             if type(i) is dict:
    #                 get_values_in_set(i)
    #             else:
    #                 values1.append(i)
    #     get_values_in_set(self.color)
    #     return_value
    #     print(values1)


# a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
# big = {}
# for i in a:
#     if i > 5:
#         print(i)
#     for i in a:
#         if i < 5:
#             print(i)    

'''
def random():
    for i in str(range(1,10)):
        a = int(input('введите число'))
        if a in i:
            print('это число есть в списке')
random() 
# '''
# class Python:
#     def __init__ (self) -> None:
#         self.word = "fuck you"
#         def {self.word}:
#             return "i am ", self.word
# p = Python
# # print(p)
# class Cars:
#     def drive(self):
#         print('power')
# class Mersedes(Cars):
#     def speed(self):
#         pass

# class Power():
#     def __init__ (self, engine,matel,mark):
#         self.e = engine
#         self.m = matel
# class Zoo:
#     def __init__(self) -> None:
#         self.animals_1 = 'tiger'
#         self.animals_4 = 'panda'
#         self.animals_3 = 'snake'
#         self.animals_2 = 'girafe'
#     def main(self):
#         return self.animals_1,self.animals_4,self.animals_3,self.animals_2
        
# p = Zoo()
# print(p.main())
# p.animals_1 = 'lion'
# print(p.main())
# p.animals_4 = 'varane'
# print(p.main())
# p.animals_3 = 'bear'
# print(p.main())
# p.animals_2 = 'elephent'
# class Park(Zoo):
#     def __init__(self) -> None:
#         self.amimals_3 = 'girafe'
#     def main(self):
#         return self.amimals_3
# ass = Park()
# print(ass.main())
# ass.amimals_3 = 'snake'
# print(ass.main())

# print()
'''
class Cars:
        def __init__ (self) -> None:
                self.model1 = 'Touota Supra'
                self.model2 = 'Lexus Lx 570'
                self.model3 = 'Paganu Haura'
        def main(self):
                return self.model1,self.model2,self.model3
speed = Cars()
print(speed.main())
speed.model1 = 'Mersedes Gtr63'
speed.model2 = 'Bmw M4'
speed.model3 = 'Audi R8'
print(speed.main()) 
'''
# class Car:
#     def __init__ (self)->None:
#         self.make = 'Japan'
#         self.model = 'Fit'
#         self.year = '2001'
#         self.odometer = 0
#         self.fuel = 70
#         self.drive = 50
#     def main(self):
#             return self.make,self.model,self.year,self.odometer,self.fuel,self.drive
# optic = Car()
# print(optic.main())
# class Dist(Car):
#     def __add_distance__ (drive): 
#         def main(self):
#             return self.distance

class House:
    def __init__(self)-> None:
        self.hometype = 'Моналитный дом '
        self.area = 30 
        self.furniture = 0
    def main(self):
            return f"Тип дома:{self.hometype}Участок:{self.area} Мебели:{self.furniture}"
home = House()
print(home.main())
home.furniture = ('Шкаф[2]'),('Стол[1.5]'),('Кровать[4]')
print(home.main())
bed = 4
cupboard = 2
table = 1,5

