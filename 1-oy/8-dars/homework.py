# # 1-misol
# malumotlar = ["Ism: Ali", "Familiya: Karimov", "Yosh: 22", "Yo'nalish: Python dasturlash"]
# print("1-misol natijasi:")
# for malumot in malumotlar:
#     print(malumot)

# # 2-misol
# sozlar = "aziz, ilhom, kmdr"
# royxat = sozlar.split(", ")
# teskari = list(reversed(royxat))
# natija = ", ".join(teskari)
# print("2-misol natijasi:")
# print(natija)

# # 3-misol
# sozlar = "Bilol, ilhom, Aziz"
# royxat = sozlar.split(", ")
# alifbo = sorted(royxat)
# natija = ", ".join(alifbo)
# print("3-misol natijasi:")
# print(natija)
#
# 4-misol
# sozlar = "hello, nmadr, hello, nmadr, sadas, nmadr, hello"
# maqsad = "hello"
# royxat = sozlar.split(", ")
# takror_soni = royxat.count(maqsad)
# print("4-misol natijasi:")
# print(f"{maqsad} so'zi {takror_soni} marta takrorlangan")
#
# # 5-misol
# sozlar = "kmdr, nmadr, hello"
# topish = "nmadr"
# royxat = sozlar.split(", ")
# if topish in royxat:
#     indeks = royxat.index(topish)
#     print("5-misol natijasi:")
#     print(f"{topish} so'zi {indeks}-indeksda joylashgan")
# else:
#     print(f"{topish} ro'yxatda topilmadi.")
