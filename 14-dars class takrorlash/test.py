class Register:
    def __init__(self, ism, familiya, t_yil, nomeri, email,
                 jinsi, parol, seriasi, manzil):
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.nomeri = nomeri
        self.email = email
        self.jinsi = jinsi
        self.parol = parol
        self.seriasi = seriasi
        self.manzil = manzil

    def ism_familiya(self):
        return self.ism + " " + self.familiya
    def full_name(self):
        return f"mening ismim {self.ism}  familiyam {self.familiya} "
    def nmadrla(self):
        return f"Mening pasport id seriyam {self.seriasi} mening jinsiim {self.jinsi}"

    def __str__(self):
        return self.ism

    def manzill(self):
        return self.manzil
    def famillya(self):

        return self.familiya
    def seriass(self):
        return self.seriasi
    def  emaill(self):
        return self.email
    def raqamm(self):
        return self.nomeri
    def yosh(self):
        return self.t_yil
a = Register("Diyor", "Axmadjonov",
             2004, 200123485,
             "diyorbekaxmadjonov98@gmail.com", "Erkak",
             "uy5678ui", "Ac2833339", "Olmazor tuman")
print(a.famillya())
print(a.seriass())
print(a.emaill())
print(a.raqamm())
print(a.yosh())
print(a.full_name())
print(a.nmadrla())