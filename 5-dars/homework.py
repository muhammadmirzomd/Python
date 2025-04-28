#   1-misol
# yosh = int(input("Yoshnigizni yozing; "))
# if yosh >= 18:
#     print("Siz voyaga yetgansiz !")
# elif yosh <= 18:
#     print("Siz hali voyaga yetmagansiz!")
from logging import LogRecord

#   2-misol
# baho = int(input("Bahoni kiriting; "))
# if baho == 5:
#     print("A")
# elif baho == 4:
#     print("B")
# elif baho == 3:
#     print("C")
# elif baho == 2:
#     print("D")
# else:
#     print("F")

#   3-misol
# raqam = int(input("Raqamni kiriting; "))
# if raqam > 0:
#     print("Musbat")
# elif raqam < 0:
#     print("Manfiy")
# else:
#     print("Bu son nol !")

#   4-misol
# son1 = int(input("1-Sonni kriting;"))
# son2 = int(input("2-Sonni kriting;"))
# if son1 > son2:
#     katta = son1
# else:
#     katta = son2
# print(f"Kattasi: {katta}")

#5-misol
# son1 = int(input("1-Sonni kriting;"))
# son2 = int(input("2-Sonni kriting;"))
# son3 = int(input("3-Sonni kriting;"))
# katta = son1
# if son2 > katta:
#     katta = son2
# elif son3 > katta:
#     katta = son3
# print(f"Kattasi:{katta}")

#6-misol
# son = int(input("Sonni kiriting: "))
# if son % 2 == 0:
#     print(f"{son} juft son.")
# else:
#     print(f"{son} toq son.")

#7-misol
# ism = str(input("Ismingizni yozing; "))
# yosh = int(input("Yoshnigizni yozing; "))
# if yosh >= 18:
#     print(f"Hurmatli {ism} kirishingiz mumkin!")
# elif yosh <= 18:
#     print(f"Hurmatli {ism} kirishingiz mumkin emas!")

#   8-misol
# a = int(input("Hafta raqamini kiriting; "))
# hafta = a % 7
# if hafta == 1:
#     print("Dushanba")
# elif hafta == 2:
#     print("Seshanba")
# elif hafta == 3:
#     print("Chorshanba")
# elif hafta == 4:
#     print("Payshanba")
# elif hafta == 5:
#     print("Juma")
# elif hafta == 6:
#     print("Shanba")
# elif hafta == 0:
#     print("Yakshanba")

# 9-misol
# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# yigindi = son1 + son2
# if yigindi > 100:
#     print("Yig'indi 100 dan katta.")
# elif yigindi < 100:
#     print("Yig'indi 100 dan kichik.")
# else:
#     print("Yig'indi aynan 100 ga teng.")

# 10-misol
# ball = int(input("Ballingizni kiriting:"))
# if 50 <= ball <= 100:
#     print("Imtihondan o'tingiz!")
# elif 0 <= ball <= 49:
#     print("Imtihondan o'tolmadingiz!")
# else:
#     print("Bunday ball mavjud emas")

#14-misol
# t = int(input("Temperatura: "))
# if t < 20:
#     print("Sovuq")
# elif t > 30:
#     print("Issiq")
# else:
#     print("O‘rtacha")

#15-misol
# oy = int(input("Oy raqami (1-12): "))
# if oy == 2:
#     print("28 yoki 29 kun")
# elif oy in [4, 6, 9, 11]:
#     print("30 kun")
# else:
#     print("31 kun")

#17-misol
# soat = int(input("Soatni kiriting (0-23): "))
# if 5 <= soat < 12:
#     print("Ertalab")
# elif 12 <= soat < 18:
#     print("Kunduz")
# else:
#     print("Kech")

#18-misol
# harorat = int(input("Haroratni kiriting: "))
# if harorat >= 25:
#     print("Yoz")
# elif 10 <= harorat < 25:
#     print("Bahor")
# else:
#     print("Qish")


#19-misol
# login = input("Login: ")
# parol = input("Parol: ")
# if login == "admin" and parol == "1234":
#     print("Kirish muvaffaqiyatli")
# else:
#     print("Login yoki parol xato")

# 20-misol
# a = int(input("a: "))
# b = int(input("b: "))
# if a == b:
#     print("Kvadrat")
# else:
#     print("To'rtburchak")

#21-misol
# son = int(input("Son kiriting: "))
# if -10 < son < 10:
#     print("Bir xonali")
# elif -100 < son < 100:
#     print("Ikki xonali")
# else:
#     print("Uch xonali yoki undan katta")

#23-misol
# daromad = int(input("Daromad: "))
# if daromad < 5000:
#     print("Kam daromad – past stavka")
# elif daromad <= 10000:
#     print("O‘rtacha daromad – o‘rtacha stavka")
# else:
#     print("Yuqori daromad – yuqori stavka")

#24-misol
# soat = int(input("Soatni kiriting: "))
# if 6 <= soat < 12:
#     print("Ertalab")
# elif 12 <= soat < 18:
#     print("Kunduz")
# else:
#     print("Kech")

#26-misol
# baho = int(input("Baho (1-5): "))+
# if baho >= 4:
#     print("O‘tgan")
# else:
#     print("Qolgan")

#30-misol
db = int(input("Tovush darajasi (dB): "))
if db < 30:
    print("Zaif")
elif db <= 70:
    print("O‘rtacha")
else:
    print("Kuchli")

'''
11-misol
12-misol
13-misol
16-misol
22-misol
26-misol
27-misol
28-misol
29-misol
'''
