#2.1.a
class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__language_list = []
    def print_info(self):
        print(f"I {self.__name} bor det {self.__population} miljoner invånare")
        if self.__area is not None:
            print(f"Arean är {self.__area} kvadratkilometer")
        for language in self.__language_list:
            print(language)
    def add_language(self, lang):
        self.__language_list.append(lang)


se = Country("Sverige", 10.5, 10)
no = Country("Norge", 5.5)
isl = Country("Island", 0.383)
dan = Country("Danmark", 5.96)

#2.1.b
se.print_info()

#2.1.c
dan.print_info()

#2.1.f:
se.add_language("svenska")
se.add_language("romani")
se.print_info()
dan.print_info()