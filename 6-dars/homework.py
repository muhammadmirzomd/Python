# 14
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     birlik = son % 10
#     qolgan = son // 10
#     yangi_son = birlik * 100 + qolgan
#     print("Natija:", yangi_son)
# else:
#     print("Iltimos, uch xonali son kiriting.")

# 15
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     yuz = son // 100
#     on = (son // 10) % 10
#     bir = son % 10
#     yangi_son = on * 100 + yuz * 10 + bir
#     print("Natija:", yangi_son)
# else:
#     print("Uch xonali son kiriting.")

# 16
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     yuz = son // 100
#     on = (son // 10) % 10
#     bir = son % 10
#     yangi_son = yuz * 100 + bir * 10 + on
#     print("Natija:", yangi_son)
# else:
#     print("Uch xonali son kiriting.")

# 17
# son = int(input("1000 dan katta son kiriting: "))
# if son > 999:
#     yuzlik = (son // 100) % 10
#     print("Yuzliklar xonasidagi raqam:", yuzlik)
# else:
#     print("999 dan katta son kiriting.")

# 18
# son = int(input("1000 dan katta son kiriting: "))
# if son > 999:
#     minglik = (son // 1000) % 10
#     print("Mingliklar xonasidagi raqam:", minglik)
# else:
#     print("999 dan katta son kiriting.")

# 19
# N = int(input("N sekundni kiriting: "))
# if N >= 0:
#     minut = N // 60
#     print("To‘la minutlar:", minut)
# else:
#     print("Musbat son kiriting.")

# 20
# N = int(input("N sekundni kiriting: "))
# if N >= 0:
#     soat = N // 3600
#     print("To‘la soatlar:", soat)
# else:
#     print("Musbat son kiriting.")

# 21
# N = int(input("N sekundni kiriting: "))
# if N >= 0:
#     minut = N // 60
#     sekund = N % 60
#     print(f"{minut} minut {sekund} sekund o‘tgan.")
# else:
#     print("Musbat son kiriting.")

# 21
# N = int(input("N sekundni kiriting: "))
# if N >= 0:
#     soat = N // 3600
#     sekund = N % 3600
#     print(f"{soat} soat {sekund} sekund o‘tgan.")
# else:
#     print("Musbat son kiriting.")

# 23
# N = int(input("N sekundni kiriting: "))
# if N >= 0:
#     soat = N // 3600
#     minut = (N % 3600) // 60
#     sekund = N % 60
#     print(f"{soat} soat {minut} minut {sekund} sekund o‘tgan.")
# else:
#     print("Musbat son kiriting.")

# 1
# L = int(input("Uzunlikni santimetrda kiriting: "))
# if L >= 0:
#     metr = L // 100
#     print("To‘liq metr:", metr)
# else:
#     print("Manfiy bo‘lmasligi kerak.")
# 2
# M = int(input("Og‘irlikni kilogramda kiriting: "))
# if M >= 0:
#     tonna = M // 1000
#     print("To‘liq tonna:", tonna)
# else:
#     print("Manfiy bo‘lmasligi kerak.")

# 3
# bayt = int(input("Fayl hajmini baytda kiriting: "))
# if bayt >= 0:
#     kb = bayt // 1024
#     print("Kilobaytda:", kb)
# else:
#     print("Manfiy bo‘lmasin.")

# 4
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
# if A > 0 and B > 0 and A > B:
#     joylashish = A // B
#     print("Joylashishlar soni:", joylashish)
# else:
#     print("A > B va musbat sonlar bo‘lishi kerak.")

# 5
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
# if A > 0 and B > 0 and A > B:
#     qoldiq = A % B
#     print("Qoldiq uzunlik:", qoldiq)
# else:
#     print("A > B va musbat sonlar bo‘lishi kerak.")

# 6
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     onlik = (son // 10) % 10
#     print("O‘nliklar xonasidagi raqam:", onlik)
# else:
#     print("Iltimos, uch xonali son kiriting.")

# 7
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     yuz = son // 100
#     on = (son // 10) % 10
#     bir = son % 10
#     yigindi = yuz + on + bir
#     print("Raqamlar yig‘indisi:", yigindi)
# else:
#     print("Uch xonali son kiriting.")

# 8
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     yuz = son // 100
#     on = (son // 10) % 10
#     bir = son % 10
#     yangi_son = bir * 100 + on * 10 + yuz
#     print("Teskari son:", yangi_son)
# else:
#     print("Uch xonali son kiriting.")

# 9
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     on = (son // 10) % 10
#     bir = son % 10
#     yangi_son = on * 10 + bir
#     print("Natija:", yangi_son)
# else:
#     print("Uch xonali son kiriting.")

# 10
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     yuz = son // 100
#     on = (son // 10) % 10
#     bir = son % 10
#     print("Natija:", yuz * 100 + on * 10 + bir)
# else:
#     print("Uch xonali son kiriting.")

# 11
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     yuz = son // 100
#     on = (son // 10) % 10
#     bir = son % 10
#     yangi_son = yuz * 100 + bir * 10 + on
#     print("Natija:", yangi_son)
# else:
#     print("Uch xonali son kiriting.")

# 12
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     yuz = son // 100
#     on = (son // 10) % 10
#     bir = son % 10
#     teskari = bir * 100 + on * 10 + yuz
#     print("Teskari tartib:", teskari)
# else:
#     print("Uch xonali son kiriting.")

# 13
# son = int(input("Uch xonali son kiriting: "))
# if 100 <= son <= 999:
#     yuz = son // 100
#     qolgan = son % 100
#     yangi_son = qolgan * 10 + yuz
#     print("Natija:", yangi_son)
# else:
#     print("Uch xonali son kiriting.")

#
# a = 1234
# print(a / 1000)
