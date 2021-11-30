import BullsAndCows_pomocne_funkce as bcpom

ODDELOVAC = 50*"-"
HADANE_CISLO = bcpom.vytvor_hadane_cislo()

### Uvitani uzivatele

print("""
Hi there!
--------------------------------------------------
I've generated a random 4 digit number for you
(NOT starting with 0, unique cyphers).
Let's play Bulls and Cows game.
--------------------------------------------------""")
zadane_cislo = input("Enter a 4 digit number: ")
guesses = 1
print(ODDELOVAC)

while zadane_cislo != HADANE_CISLO:
    spravnost = bcpom.kontrola_vstupu(zadane_cislo)
    if spravnost == 0:
        print("""You must enter:
            - four digit number
            - unique cyphers
            - not starting with zero!""")
        print(ODDELOVAC)
        zadane_cislo = input("Enter a 4 digit number: ")
        print(ODDELOVAC)
    else:
        bulls_and_cows = bcpom.bulls_and_cows(HADANE_CISLO, zadane_cislo)
        if bulls_and_cows[0] == 1:
            bulls = "bull"
        else:
            bulls = "bulls"
        if bulls_and_cows[1] == 1:
            cows = "cow"
        else:
            cows = "cows"
        print(f"{bulls_and_cows[0]} {bulls}, {bulls_and_cows[1]} {cows}")

        guesses += 1
        print(ODDELOVAC)
        zadane_cislo = input("Enter a 4 digit number: ")
        print(ODDELOVAC)

print(f"Well done! You have guessed the right number {zadane_cislo} in {guesses} guesses!")
