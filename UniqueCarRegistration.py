import random
import string


class UniqueCarRegistration:
    def __init__(self):
        self.used = list()

        twobytwo_combo = (26**2) * (10**2) * (26**2) * 9
        threebythree_combo = (26**3) * (10**3) * 9
        # Total possible combinations (26 alphabets and 10 digits and 9 provinces)
        self.possible_count = twobytwo_combo + threebythree_combo

    def generate(self):
        prov_list = ["GP", "NW", "FS", "MP", "NC", "EC", "ZN", "WC", "L"]

        # To avoid repeated combinations
        if len(self.used) >= self.possible_count:
            raise RuntimeError("All possible combinations have been exhausted.")

        while True:
            prov = "".join(random.choice(prov_list))
            sep = random.choice([" ", "-"])

            if random.choice([True, False]):
                two_part1 = "".join(random.choices(string.ascii_uppercase, k=2))
                two_part2 = "".join(random.choices(string.digits, k=2))
                two_part3 = "".join(random.choices(string.ascii_uppercase, k=2))
                candidate_reg = (
                    f"{two_part1}{sep}{two_part2}{sep}{two_part3}{sep}{prov}"
                )

            else:
                three_part1 = "".join(random.choices(string.ascii_uppercase, k=3))
                three_part2 = "".join(random.choices(string.digits, k=3))
                candidate_reg = f"{three_part1}{sep}{three_part2}{sep}{prov}"

            if candidate_reg not in self.used:
                self.used.append(candidate_reg)
                break

        print(candidate_reg)


if __name__ == "__main__":
    car_reg = UniqueCarRegistration()
    car_reg.generate()
    print()
