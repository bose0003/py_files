'''
Python file for python refresher section 
Contains code from lecture 3, 4, 5, 6, 7, 8, 9
'''

class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self, year):
        return(2018 - self.year)

age = 25

name = "Subhasis Bose"

print("Hello my name is {} and I am {} years old.".format(name, age))

if age > 18:
    print("You are older than 18.")

def hello():
    print("hello world!")

hello()
hello()
hello()

dognames = ["Frodo", "Sean", "Sally", "Mark"]

for dogname in dognames:
    print(dogname)

for i in range(1,10):
    print(i)

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"] 

cooldictionary = {}
for i in range(len(words)):
    cooldictionary[words[i]] = definitions[i]

print(cooldictionary)

car = Car(2000, "Honda", "Civic")
age = car.age(2000)
print(age)