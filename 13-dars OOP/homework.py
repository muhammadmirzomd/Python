"""
1-misol
"""
# class Talaba:
#     def __init__(self, ism, yosh, kurs, institut, yonalish):
#         self.ism = ism
#         self.yosh = yosh
#         self.kurs = kurs
#         self.institut = institut
#         self.yonalish = yonalish
#
#     def tanishtir(self):
#         print(f"Men {self.ism}, {self.yosh} yoshdaman.")
#         print(f"{self.institut} institutida {self.kurs}-kursda o‘qiyman.")
#         print(f"Yo‘nalishim: {self.yonalish}")
#
# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# kurs = int(input("Kursingizni kiriting: "))
# institut = input("Institut nomini kiriting: ")
# yonalish = input("Yo‘nalishingizni kiriting: ")
#
# talaba1 = Talaba(ism, yosh, kurs, institut, yonalish)
# talaba1.tanishtir()

"""
2-misol
"""
# class Kitob:
#     def __init__(self, nomi, muallif, janr, sahifa_soni, yil):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.janr = janr
#         self.sahifa = sahifa_soni
#         self.yil = yil
#
#     def info(self):
#         print(f"Kitob: {self.nomi}, Muallif: {self.muallif}")
#         print(f"Janr: {self.janr}, Sahifa: {self.sahifa}, Yili: {self.yil}")
#
# nomi = input("Kitob nomi: ")
# muallif = input("Muallif: ")
# janr = input("Janr: ")
# sahifa = int(input("Sahifa soni: "))
# yil = int(input("Chop etilgan yil: "))
#
# k = Kitob(nomi, muallif, janr, sahifa, yil)
# k.info()

"""
3-misol
"""

# class Qabul:
#     def __init__(self, bemor, shifokor, yonalish, sana, vaqti):
#         self.bemor = bemor
#         self.shifokor = shifokor
#         self.yonalish = yonalish
#         self.sana = sana
#         self.vaqti = vaqti
#
#     def info(self):
#         print(f"Bemor: {self.bemor}")
#         print(f"Qabul: {self.shifokor} ({self.yonalish})")
#         print(f"Sana: {self.sana}, Soat: {self.vaqti}")
#
# bemor = input("Bemor ismi: ")
# shifokor = input("Shifokor ismi: ")
# yonalish = input("Yo‘nalish (masalan, kardiolog): ")
# sana = input("Qabul kuni: ")
# vaqti = input("Soat: ")
#
# q = Qabul(bemor, shifokor, yonalish, sana, vaqti)
# q.info()

'''
4-misol
'''

# class Dostavka:
#     def __init__(self, ism, manzil, mahsulot, masofa, narx):
#         self.ism = ism
#         self.manzil = manzil
#         self.mahsulot = mahsulot
#         self.masofa = masofa
#         self.narx = narx
#
#     def info(self):
#         print(f"Buyurtmachi: {self.ism}")
#         print(f"Manzil: {self.manzil}, Mahsulot: {self.mahsulot}")
#         print(f"Masofa: {self.masofa} km, Narx: {self.narx} so‘m")
#
# ism = input("Ismingiz: ")
# manzil = input("Manzilingiz: ")
# mahsulot = input("Buyurtma qilgan mahsulot: ")
# masofa = float(input("Masofa (km): "))
# narx = int(input("Dostavka narxi: "))
#
# d = Dostavka(ism, manzil, mahsulot, masofa, narx)
# d.info()

"""
5-misol
"""

# class OnlineDars:
#     def __init__(self, fan, oqituvchi, boshlanish_vaqti, davomiylik, platforma):
#         self.fan = fan
#         self.oqituvchi = oqituvchi
#         self.boshlanish = boshlanish_vaqti
#         self.davomiylik = davomiylik
#         self.platforma = platforma
#
#     def info(self):
#         print(f"Fan: {self.fan}")
#         print(f"O‘qituvchi: {self.oqituvchi}")
#         print(f"Boshlanish: {self.boshlanish} | Davomiylik: {self.davomiylik} daqiqa")
#         print(f"Dars platformasi: {self.platforma}")
#
# fan = input("Fan nomi: ")
# oqituvchi = input("O‘qituvchi ismi: ")
# boshlanish = input("Boshlanish vaqti: ")
# davomiylik = int(input("Davomiylik (daqiqa): "))
# platforma = input("Platforma: ")
#
# d1 = OnlineDars(fan, oqituvchi, boshlanish, davomiylik, platforma)
# d1.info()