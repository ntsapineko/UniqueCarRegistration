import random
import string

class UniqueCarRegistration:
    def __init__(self):
        self.used = set()
        self.possible_count = (26**2) * (10**2) * (26**2)  # Total possible combinations (26 alphabets and 10 digits)

    def generate(self):
        if len(self.used) >= self.possible_count:
            raise RuntimeError("All possible combinations have been exhausted.") #To avoid repeated combinations

        while True:
            part1 = ''.join(random.choices(string.ascii_uppercase, k=2))
            part2 = ''.join(random.choices(string.digits, k=2))
            part3 = ''.join(random.choices(string.ascii_uppercase, k=2))
            sep = random.choice([' ', '-'])
            candidate = f"{part1}{sep}{part2}{sep}{part3}"

            if candidate_reg not in self.used:
                self.used.add(candidate_reg)
                return candidate_reg

gen = UniqueCarRegistration()
for _ in range(5):
    print(gen.generate())