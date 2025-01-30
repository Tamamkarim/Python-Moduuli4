import random

# Kysytään pisteiden määrä käyttäjältä
N = float(input("Syötä arvottavien pisteiden määrä: "))

n = 0

for _ in range(N):
    # Arvotaan pisteen koordinaatit neliön B sisältä
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Tarkistetaan onko piste yksikköympyrän sisällä
    if x ** 2 + y ** 2 < 1:
        n += 1

# Lasketaan
pi_approx = 4 * n / N

#  tulos
print(f"Piin likiarvo on {pi_approx}")

