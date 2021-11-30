import string
import random


def vytvor_hadane_cislo() -> str:
    cislice = string.digits
    prvni_cislice = random.choice(string.digits.strip("0"))
    cislice = cislice.replace(prvni_cislice, "")

    hadane_cislo = prvni_cislice

    pocet_cislic = 1
    while pocet_cislic < 4:
        unikatni_cislice = random.choice(cislice)
        cislice = cislice.replace(unikatni_cislice, "")
        hadane_cislo = hadane_cislo + unikatni_cislice
        pocet_cislic += 1
    return (hadane_cislo)

def isunique(zadane_cislo: str) -> bool:
    count_znak = 0
    for znak in zadane_cislo:
        if zadane_cislo.count(znak) > count_znak:
            count_znak = zadane_cislo.count(znak)
    if count_znak == 1:
        return(True)
    else:
        return(False)

def kontrola_vstupu(zadane_cislo: str) -> int:
    if not isunique(zadane_cislo):
        # print("You must enter a four digit number not starting with zero!")
        spravnost = 0
    elif zadane_cislo.startswith("0"):
        # print("You must enter a four digit number not starting with zero!")
        spravnost = 0
    elif len(zadane_cislo) != 4:
        # print("You must enter a four digit number not starting with zero!")
        spravnost = 0
    elif not zadane_cislo.isnumeric():
        # print("You must enter a four digit number not starting with zero!")
        spravnost = 0
    else:
        spravnost = 1
    return(spravnost)

def bulls_and_cows(hadane_cislo: str, zadane_cislo: str) -> list:
    bulls = 0
    cows = 0
    for znak in zadane_cislo:
        if znak in hadane_cislo and zadane_cislo.index(znak) == hadane_cislo.index(znak):
            bulls += 1
        elif znak in hadane_cislo:
            cows += 1
    return[bulls,cows]

# hadane_cislo = vytvor_hadane_cislo()
# print(hadane_cislo)
#
# zadane_cislo = input("Zadej cislo: ")
#
# unique_value = isunique(zadane_cislo)
# print(unique_value)
#
# startswith_value = zadane_cislo.startswith("0")
# len_value = len(zadane_cislo) != 4
# numeric_value = not(zadane_cislo.isnumeric())
#
# print(startswith_value)
# print(len_value)
# print(numeric_value)
#
# spravnost = kontrola_vstupu(zadane_cislo)
# print(spravnost)
