class Notebook:
    def __init__(self, brend, narxi, rangi, ssd, ram, yili, ekrani, avlode):
        self.brend = brend
        self.narxi = narxi
        self.rangi = rangi
        self.ssd = ssd
        self.ram = ram
        self.yili = yili
        self.ekrani = ekrani
        self.avlode = avlode

    def __str__(self):
        return f"{self.brend} {self.narxi} so'm"


brend = input("Brend = ")
n = Notebook(brend, "600$", "Silver", "512ssd", "16 DDR5",
             2022, "15.6", "12")
print(n)
print(Notebook)
