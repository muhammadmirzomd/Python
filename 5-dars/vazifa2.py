# 8
# son= int(input("Hafta kunini kiriting = "))
# hafta = son % 7
# if hafta == 0:
#     print()

# 11
# yil = int(input("Yil = "))
# if yil % 4 == 0 and yil % 400 !=0:
#     print("Kabisa yili")
#

# 12
# 123/ 10 = 12 % 10 == 2
# son = 123
# y = son / 100
# o = (son // 10)% 10
# b = son % 10
# print(o)


"""
uchburchak

"""

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
#
# if a+b>c and a+c>b and b+c>a:
#     print("Bu uchbirchak bo'la oladi")
# else:
#     print("Bola olmaydi")

# 20 0123485
# 94 732 0406

a = int(input("a = "))
b = int(input("b = "))
k = a * b
ayirma = a - b
if k > ayirma:
    print(f"Kopaytmasi katta = {k}")
else:
    print(f"Ayirmasi katta = {ayirma}")
