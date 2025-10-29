import random
import string


class UniqueCarRegistration:
    def __init__(self):
        self.used = set()
        self.possible_count = (
            (26**2) * (10**2) * (26**2)
        )  # Total possible combinations (26 alphabets and 10 digits)

    def generate(self):
        print(
            "Choose your province by number: \n 1 for Gauteng\n 2 for North West\n3 for Free State\n 4 for Mpumalanga\n5 for Norther Cape\n6 for Eastern Cape\n7 for KwaZulu Natal\n8 for Western Cape\n9 for Limpopo\n"
        )
        choice_prov = input()
        prov = ""

        if choice_prov == "1":
            prov = "GP"
        elif choice_prov == "2":
            prov = "NW"
        elif choice_prov == "3":
            prov = "FS"
        elif choice_prov == "4":
            prov = "MP"
        elif choice_prov == "5":
            prov = "NC"
        elif choice_prov == "6":
            prov = "EC"
        elif choice_prov == "7":
            prov = "ZN"
        elif choice_prov == "8":
            prov = "WC"
        elif choice_prov == "9":
            prov = "L"
        else:
            print("Invalid choice")

        # To avoid repeated combinations
        if len(self.used) >= self.possible_count:
            raise RuntimeError("All possible combinations have been exhausted.")

        while True:
            part1 = "".join(random.choices(string.ascii_uppercase, k=2))
            part2 = "".join(random.choices(string.digits, k=2))
            part3 = "".join(random.choices(string.ascii_uppercase, k=2))
            sep = random.choice([" ", "-"])
            candidate_reg = f"{part1}{sep}{part2}{sep}{part3}+ ' '+{prov}"

            if candidate_reg not in self.used:
                self.used.add(candidate_reg)
                return candidate_reg


car_reg = UniqueCarRegistration()
car_reg.generate()
