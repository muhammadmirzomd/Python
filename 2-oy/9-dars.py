class Yoz:
    def __init__(self, matn, file_nomi):
        self.matn = matn
        self.file_nomi = file_nomi

    def yoz(self):
        with open(self.file_nomi, 'a', encoding='utf-8') as file:
            file.write(self.matn + '\n')
        print("Faylga yozildi")
matn = input("Matnni kiriting: ")

obj = Yoz(matn,  'namuna.txt')
obj.yoz()

class Test:
    def __init__(self, savollar):
        self.savollar = savollar
    def chiqar(self):
        print(self.savollar.strip())

for i in open('namuna.txt', encoding='utf-8'):
        a = Test(i)
        a.chiqar()