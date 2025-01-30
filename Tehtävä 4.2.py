
while True:
    tuumat = float(input("Syötä tuumat (negatiivinen lopettaa): "))
    if tuumat < 0:
        print("Ohjelma suljetaan.")
        break
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa = {senttimetrit:.2f} cm\n")