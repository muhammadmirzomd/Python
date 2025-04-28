"""
chiqmagan misollar uchun
"""


# 1
# def musbat_manfiy_sonlar(a):
#     if a > 0:
#         return "Musbat"
#     elif a < 0:
#         return "Manfiy"
#     else:
#         return "Nol"
# print(musbat_manfiy_sonlar(-10))

# 8
# def raqamlar_yigindisi(a):
#     a = str(a)
#     yigindi = 0
#     for i in a:
#         print(i)
#         yigindi += int(i)
#     return yigindi
#
#
# print(raqamlar_yigindisi(123))

# 9
# def son_teskarisi(a):
#     a = str(a)
#     return int(a[::-1])
# print(son_teskarisi(1234))
# 13
# def unli_harflar(soz):
#     unli = "aeiou"
#     unli_harflar = []
#     for i in soz:
#         # print(i)
#         if i in unli:
#             unli_harflar.append(i)
#     return unli_harflar
# print(unli_harflar("asdfjhggdfgdjhdgzfastyuiukjlkjn"))

# 30
def parol(parol):
    if len(parol) < 8:
        return "Parol kamida 8 ta belgidan iborat bo'lishi kerak"
    elif parol.isalpha():
        return "Parolda raqam bo'lishi kerak"
    elif parol.isdigit():
        return "Parolda harf bo'lishi kerak"
    elif parol.isalnum():
        return "Parolda maxsus belgilar bo'lishi kerak"
    elif parol.islower():
        return "Parolda katta harf bo'lishi kerak"
    else:
        return "Parol to'g'ri"

print(parol("A12345@678"))

