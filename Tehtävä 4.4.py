import random

while True:
    target = random.randint(1, 10)
    arvaukset = 0

    while True:
        guess = int(input("Arvaa luku (1-10): "))
        arvaukset += 1

        if guess < target:
            print("Liian pieni arvaus")
        elif guess > target:
            print("Liian suuri arvaus")
        else:
            print(f"Oikein! Arvasit {arvaukset} kerrolla.")
            break

    uudestaan = input("Haluatko pelata uudestaan? (k/e): ").lower()
    if not uudestaan.startswith('k'):
        break

print("Kiitos pelistä!")



