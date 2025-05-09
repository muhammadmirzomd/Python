class Phone:
    def __init__(self, rangi, camera, ekran, yili, model):
        self.rangi = rangi
        self.camera = camera
        self.ekran = ekran
        self.yili = yili
        self.model = model

    def nomi(self):
        return self.model

    def camerasi(self):
        return self.camera


phone = Phone("Qora", "12Mpx", "16.7", 2025,
              "Samsung S25 Ultra")
print(phone.nomi())
print(phone.camerasi())
