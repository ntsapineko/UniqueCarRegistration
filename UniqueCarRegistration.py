import random
import string


class UniqueCarRegistration:
    def __init__(self):
        self.used = list()
        self.possible_count = (
            (26**2) * (10**2) * (26**2)
        )  # Total possible combinations (26 alphabets and 10 digits)

    def generate(self):
        prov_list = ["GP", "NW", "FS", "MP", "NC", "EC", "ZN", "WC", "L"]

        prov = "".join(random.choices(prov_list))
        part1 = "".join(random.choices(string.ascii_uppercase, k=2))
        part2 = "".join(random.choices(string.digits, k=2))
        part3 = "".join(random.choices(string.ascii_uppercase, k=2))
        sep = random.choice([" ", "-"])

        candidate_reg = f"{part1}{sep}{part2}{sep}{part3}{sep}{prov}"

        # To avoid repeated combinations
        if len(self.used) >= self.possible_count:
            raise RuntimeError("All possible combinations have been exhausted.")

        while True:
            if candidate_reg not in self.used:
                self.used.append(candidate_reg)
                break

        print(candidate_reg)


if __name__ == "__main__":
    car_reg = UniqueCarRegistration()
    car_reg.generate()
    print()
