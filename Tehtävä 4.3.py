luvut = []

while True:
    syote = input("Syötä luku (tyhjä lopettaa): ")

    if syote == "":
        break  # Lopeta silmukka jos syöte on tyhjä

    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte! Syötä numero tai tyhjä.")

if luvut:  # Tarkista onko listassa lukuja
    print(f"\nPienin syötetty luku: {min(luvut)}")
    print(f"Suurin syötetty luku: {max(luvut)}")
else:
    print("\nEt syöttänyt yhtään lukua.")