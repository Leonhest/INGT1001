print("\n")
print("Utregning av to tall")
print("\n")

def regnestykke():
    tall1 = int(input("Første tall"))
    print("\n")
    choice = input("Velg: +, -, *, /")
    print("\n")
    tall2 = int(input("Andre tall"))
    print("\n")
    if choice == "+":
        print(tall1 + tall2)
    elif choice == "-":
        print(tall1 - tall2)
    elif choice == "*":
        print(tall1 * tall2)
    elif choice == "/":
        print(tall1 / tall2)
    else:
        print("skriv +, -, * eller /")

regnestykke()

