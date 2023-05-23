class Pojistenci:
    def __init__(self):
        self.pojistenci = []

    @staticmethod
    def is_valid_name(name):
        return all(ch.isalpha() or ch.isspace() for ch in name)

    def pridej_pojisteneho(self):
        jmeno_pojistence = input("Zadejte jméno: ")
        jmeno_pojistence = jmeno_pojistence.strip()
        if not self.is_valid_name(jmeno_pojistence):
            print("Jmeno musí být ze znaků abecedy")
            return
        prijmeni_pojisteneho = input("Zadejte příjmení: ")
        prijmeni_pojisteneho = prijmeni_pojisteneho.strip()
        if not self.is_valid_name(prijmeni_pojisteneho):
            print("Příjmení musí být ze znaků abecedy")
            return

        telefonni_cislo = input("Zadejte telefonní číslo: ")
        telefonni_cislo = telefonni_cislo.replace(" ", " ")
        if not telefonni_cislo.isdigit():
            print("Telfonní číslo musí být zadané jako číslo.")
            return
        vek = input("Zadejte věk: ")
        vek = vek.replace(" ", " ")
        if not vek.isdigit():
            print("Věk musí být zadané jako číslo.")
            return

        pojistenec = {
            "jmeno": jmeno_pojistence,
            "prijmeni": prijmeni_pojisteneho,
            "telefonni_cislo": telefonni_cislo,
            "vek": vek
        }
        self.pojistenci.append(pojistenec)

    def vypis_pojistene(self):
        print("Pojisteni klienti:")
        for pojistenec in self.pojistenci:
            print("Jméno:", pojistenec["jmeno"])
            print("Příjmení:", pojistenec["prijmeni"])
            print("Telefonní číslo:", pojistenec["telefonni_cislo"])
            print("Věk:", pojistenec["vek"])
            print()

    def vyhledej_pojisteneho(self):
        jmeno_pojistence = input("Zadejte jméno pojistence: ")
        found = False
        for pojistenec in self.pojistenci:
            if pojistenec["jmeno"] == jmeno_pojistence:
                print("Jméno:", pojistenec["jmeno"])
                print("Příjmení:", pojistenec["prijmeni"])
                print("Telefonní číslo:", pojistenec["telefonni_cislo"])
                print("Věk:", pojistenec["vek"])
                found = True
                break
        if not found:
            print("Pojistenec nenalezen")

    def spustit(self):
        while True:
            print("Vyberte si akci:")
            print("1 - Přidat nového pojistěného")
            print("2 - Vypsat všechny pojistěné")
            print("3 - Vyhledat pojistěného")
            print("4 - Konec")
            volba = input()

            if volba == '1':
                self.pridej_pojisteneho()
            elif volba == '2':
                self.vypis_pojistene()
            elif volba == '3':
                self.vyhledej_pojisteneho()
            elif volba == '4':
                print("Konec")
                break
            else:
                print("Nezadali jste číslo v požadovaném rozmezí.")


pojistenci = Pojistenci()
pojistenci.spustit()
