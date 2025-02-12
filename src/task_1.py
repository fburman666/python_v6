#Skriv ner vad du tror kommer skrivas ut.
# Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?


# Vad gör följande kod?
class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)



# 2a, 2b Vad gör följande kod? Fixa eventuella fel.
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(self):
       # super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(self):
      #  super().make_noise()
        print("kuckeliku!")

class Goldfish(Animal):
    def make_noise(self):
        super().make_noise()
       # print("blubb!")

def sound_off(animal):
    for pet in animal:
        pet.make_noise()


c = Cat()
d = Dog()
h = Rooster()
g = Goldfish()
sound_off([c, d, h, g])


