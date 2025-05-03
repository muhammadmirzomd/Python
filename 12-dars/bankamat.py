def bankamat():
    print("Bankomatga xush kelibsiz!")
    print("1. Naqd pul yechish")
    print("2. Pul qo'shish")
    print("3. Hisobni tekshirish")


def pin_kod():
    sanoq = 0
    print("PIN kodni kiriting:")
    while sanoq < 3:
        pin = int(input("PIN kod: "))
        if pin == 1234:
            print("PIN kod to'g'ri")
            return bankamat()
        else:
            print("PIN kod noto'g'ri")
            sanoq += 1
    if sanoq < 3:
        print(f"Qolgan urinishlar: {3 - sanoq}")
        pin_kod()
    else:
        print("PIN kodni 3 marta noto'g'ri kiritdingiz. Bankomat bloklandi.")
        return pin_kod()


def hisobni_tekshirish():
    print("Hisobni tekshirish")
    hisob = 1000000
    print(f"Hisobingizdagi mablag': {hisob} so'm")
    return bankamat()


def pull_yechish():
    print("Naqd pul yechish")
    hisob = 1000000
    yechish = int(input("Yechmoqchi bo'lgan summangizni kiriting: "))
    if yechish > hisob:
        print("Hisobingizda yetarli mablag' yo'q!")
    else:
        hisob -= yechish
        print(f"Hisobingizdan {yechish} so'm yechildi. Qolgan mablag': {hisob} so'm")


def pull_qoshish():
    print("Pull qo'ish")
    hisob = 1000000
    qoshish = int(input("Qo'shmoqchi bo'lgan summangizni kiriting: "))
    if qoshish < 0:
        print("Salbiy summani qo'shish mumkin emas!")
    else:
        hisob += qoshish
        print(f"Hisobingizga {qoshish} so'm qo'shildi. Jami mablag': {hisob} so'm")
    raise bankamat()


if __name__ == "__main__":
    pin_kod()
    while True:
        tanlov = int(input("Tanlovingizni kiriting (1-4): "))
        if tanlov == 1:
            pull_yechish()
        elif tanlov == 2:
            pull_qoshish()
        elif tanlov == 3:
            hisobni_tekshirish()
        elif tanlov == 4:
            break
