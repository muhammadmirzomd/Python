class Animals:
    def __init__(self, name: str, years: int):
        self.name = name
        self.years = years

    def __str__(self):
        return f"{self.name} {self.years} yoshda"

    def yosh(self):
        return f"{self.name} {self.years} yoshda"


a = Animals("sher", 5)
print(a.yosh())
