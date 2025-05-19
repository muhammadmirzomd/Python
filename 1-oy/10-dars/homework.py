# 1
def musbat_yoki_manfiy(son):
    if son > 0:
        return "Musbat"
    elif son < 0:
        return "Manfiy"
    else:
        return "Nol"

print(musbat_yoki_manfiy(10))

# 2
def juft_yoki_toq(son):
    if son % 2 == 0:
        return "Juft"
    else:
        return "Toq"

print(juft_yoki_toq(7))

# 3
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

print(faktorial(5))

# 4
def eng_kichik_son(a, b):
    return a if a < b else b

print(eng_kichik_son(3, 7))

# 5
def eng_katta_son(a, b, c):
    return max(a, b, c)

print(eng_katta_son(4, 9, 2))

# 6
def tubmi(son):
    if son < 2:
        return False
    for i in range(2, int(son**0.5)+1):
        if son % i == 0:
            return False
    return True

print(tubmi(13))

# 7
def tub_sonlar(n):
    return [i for i in range(2, n+1) if tubmi(i)]

print(tub_sonlar(20))

# 8
def raqamlar_yigindisi(son):
    yigindi = 0
    for i in str(abs(son)):
        yigindi += int(i)
    return yigindi

print(raqamlar_yigindisi(1234))


# 9
def teskari_son(son):
    teskari = 0
    son = abs(son)
    while son > 0:
        teskari = teskari * 10 + son % 10
        son //= 10
    return teskari * (-1 if son < 0 else 1)

print(teskari_son(123))

# 10
def palindrommi(son):
    s = str(son)
    return s == s[::-1]

print(palindrommi(121))

# 11
def kabisa_yilmi(yil):
    return yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0)

print(kabisa_yilmi(2024))

# 12
def teskari_soz(matn):
    return matn[::-1]

print(teskari_soz("hello"))

# 13
def unlilar_soni(matn):
    unli = "aeiouAEIOU"
    return sum(1 for harf in matn if harf in unli)

print(unlilar_soni("Salom dunyo"))

# 14
def sozlar_soni(matn):
    return len(matn.split())

print(sozlar_soni("Bugun havo yaxshi"))

# 15
def anagrammami(matn1, matn2):
    return sorted(matn1) == sorted(matn2)

print(anagrammami("listen", "silent"))

# 16
def fibonacci(n):
    a, b = 0, 1
    natija = []
    for _ in range(n):
        natija.append(a)
        a, b = b, a + b
    return natija

print(fibonacci(7))

# 17
def juft_yigindi(n):
    return sum(i for i in range(n+1) if i % 2 == 0)

print(juft_yigindi(10))

# 18
def faqat_juft_raqamli(son):
    for raqam in str(abs(son)):
        if int(raqam) % 2 != 0:
            return False
    return True

print(faqat_juft_raqamli(2486))


# 19
def eng_katta_element(lst):
    eng_katta = lst[0]
    for son in lst:
        if son > eng_katta:
            eng_katta = son
    return eng_katta

print(eng_katta_element([4, 7, 2, 9, 1]))

# 20
def ortacha_qiymat(lst):
    return sum(lst) / len(lst)

print(ortacha_qiymat([5, 10, 15]))

# 21
def musbat_sonlar(lst):
    return [i for i in lst if i > 0]

print(musbat_sonlar([-3, 5, 0, 8, -1]))

# 22
def takroriy_olib_tashla(lst):
    return list(set(lst))

print(takroriy_olib_tashla([1, 2, 2, 3, 4, 4]))

# 23
def tartibla(matn):
    return ''.join(sorted(matn))

print(tartibla("python"))

# 24
def yosh_toifasi(yosh):
    if yosh < 13:
        return "Bola"
    elif yosh < 18:
        return "O‘smir"
    else:
        return "Katta"

print(yosh_toifasi(16))

# 25
def salomlashuv(soat):
    if 5 <= soat < 12:
        return "Ertalab"
    elif 12 <= soat < 18:
        return "Tushda"
    else:
        return "Kechqurun"

print(salomlashuv(14))

# 26
def kvadratlash(lst):
    return [i**2 for i in lst]

print(kvadratlash([1, 2, 3, 4]))

# 27
def juft_indeksdagilar(lst):
    return [lst[i] for i in range(0, len(lst), 2)]

print(juft_indeksdagilar([10, 20, 30, 40, 50]))

# 28
def katta_harflar(matn):
    return matn.upper()

print(katta_harflar("salom"))

# 29
def umumiy_elementlar(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(umumiy_elementlar([1, 2, 3], [2, 3, 4]))

# 30
def kuchli_parol(parol):
    uzun = False
    raqam_bor = False
    harf_bor = False

    if len(parol) >= 8:
        uzun = True

    for belgi in parol:
        if '0' <= belgi <= '9':
            raqam_bor = True
        if ('a' <= belgi <= 'z') or ('A' <= belgi <= 'Z'):
            harf_bor = True

    if uzun and raqam_bor and harf_bor:
        return "Kuchli parol"
    else:
        return "Kuchsiz parol"

print(kuchli_parol("parol123"))
