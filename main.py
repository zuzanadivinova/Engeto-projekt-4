# Seznam pro ukládání úkolů
ukoly = []

# Funkce hlavní menu
def hlavni_menu():
    while True:
        print("\n--- HLAVNÍ MENU ---")
        menu_text = (
            "1. Přidat nový úkol\n"
            "2. Zobrazit všechny úkoly\n"
            "3. Odstranit úkol\n"
            "4. Konec programu"
        )
        print(menu_text)

        volba = input("Vyber možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Program byl ukončen.")
            break
        else:
            print("Neplatná volba. Zkuste to znovu.")

# Funkce pro přidání úkolu
def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný.")
            continue
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný.")
            continue
        ukoly.append({"nazev": nazev, "popis": popis})
        print("Úkol byl přidán.")
        break

# Funkce pro zobrazení úkolů
def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("\n--- SEZNAM ÚKOLŮ ---")
        for index, ukol in enumerate(ukoly, 1):
            print(f"{index}. {ukol['nazev']} - {ukol['popis']}")

# Funkce pro odstranění úkolu
def odstranit_ukol():
    if not ukoly:
        print("Seznam úkolů je prázdný. Není co odstraňovat.")
        return

    zobrazit_ukoly()
    while True:
        try:
            cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= cislo <= len(ukoly):
                odstraneny = ukoly.pop(cislo - 1)
                print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
                break
            else:
                print("Neplatné číslo úkolu. Zkuste to znovu.")
        except ValueError:
            print("Zadejte prosím platné číslo.")

# Spuštění programu
if __name__ == '__main__':
    hlavni_menu()
