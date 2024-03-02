class Samochod:
    def __init__(self, marka, model, rocznik):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik

    def __str__(self):
        return f"Marka: {self.marka}, Model: {self.model}, Rocznik: {self.rocznik}"

    def pokaz_informacje(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Rocznik: {self.rocznik}")
    


# Utworzenie obiektu klasy Samochod
moj_samochod = Samochod('Toyota', 'Corolla', 2020)

# Drukowanie obiektu
print(moj_samochod)
moj_samochod.pokaz_informacje()