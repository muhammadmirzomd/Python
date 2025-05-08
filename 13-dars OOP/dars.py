"""
class yaratish
"""


class Person:
    def __init__(self, ism, yosh, familiya, yili, nomeri):
        self.ism = ism
        self.yosh = yosh
        self.familiya = familiya
        self.yili = yili
        self.nomeri = nomeri

    def __str__(self):
        return self.ism

    def ismm(self):
        return self.ism

    def yoshm(self):
        return self.yosh

    def ism_familiya(self):
        return self.ism + " " + self.familiya


person = Person("Diyor", 21,
                "Axamdjonov", 2004, 1234)
print(person.ismm())
print(person.yoshm())
print(person.ism_familiya())
print(person)