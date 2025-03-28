mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]


ceny = (150, 200, 120, 120, 100, 180)


slevy = ("Olomouc", "Svitavy", "Ostrava")


domeny = ("gmail.com", "seznam.cz", "email.cz")


dvojita_cara = "=" * 35
cara = "-" * 35


nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""


AKT_ROK = 2025

print("Vítejte v Aplikaci")
print(cara)
print(nabidka)
print(cara)

cislo_destinace = int(input("Zadejte číslo vybrané destinace: "))
if cislo_destinace > 6:
    print("číslo destinace neexistuje.")
print(f"Destinace: {mesta[cislo_destinace-1]}")

jmeno = input("vaše celé jméno: ")
jmeno_list = jmeno.split(" ")

jmeno = jmeno_list[0]
print(jmeno)

