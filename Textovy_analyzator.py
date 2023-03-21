# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Václav Kryštof
# email: v.krystof@seznam.cz
# discord: Vašek K.#0340

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registrated = {                                               # key = user, value = password
    "bob": "123",                                             # číselné heslo použiju jako string
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}     

oddelovac = "="
user = input("Please login with your username: ")
password = input("Please enter your password: ")

print("python projekt1.py")

if registrated.get(user) != password:
    print(f"Username: {user}\nPassword: {password}")
    print(f"Incorrect username: \"{user}\" or password: \"{password}\". \nTerminating the program...")
    quit()
else:
    print(f"Username: {user}\nPassword: {password}")
    print(oddelovac * 43)
    print(f"Welcome to the app, {user}.\nWe have 3 texts to be analyzed.")
    print(oddelovac * 43)

selected_text = input("Enter a number. Only 1-3 to be selected: ")

if not selected_text.isdigit():
    print(f"Number must be ONLY digit in range 1-3! Not a string, symbol, etc.")
    print(f"Incorrect number: {selected_text} \nTerminating the programm...")
    quit()

if selected_text in "123":
    print(f"Entered number: {selected_text}")
    print(oddelovac * 43)
else:
    print(f"Number must be ONLY digit in range 1-3! Not a string, symbol, etc.")
    print(f"Incorrect number: {selected_text} \nTerminating the programm...")
    quit()

words_text_cleared = TEXTS[int(selected_text) -1].replace(".", "").replace(",", "").replace("-", "")
words_text_final = words_text_cleared.split()

#počet slov
pocet_slov = len(words_text_final)
print(f"There are {pocet_slov} words in the selected text.")

pocet_prvnivelke = 0  # počet slov začínajících velkým písmenem
vsechna_velka = 0     # počet slov psaných velkými písmeny
vsechna_mala = 0      # počet slov psaných malými písmeny
pocet_cisel = 0       # počet čísel (ne cifer)
suma_cisel = []       # sumu všech čísel (ne cifer) v textu.

for pocet in words_text_final:
    if pocet.istitle():
        pocet_prvnivelke += 1
    elif pocet.isupper() and pocet.isalpha():
        vsechna_velka += 1
    elif pocet.islower() and pocet.isalpha():
        vsechna_mala += 1
    elif pocet.isdigit():
        pocet_cisel += 1
        suma_cisel.append(int(pocet))

print(f"There are {pocet_prvnivelke} titlecase words.")
print(f"There are {vsechna_velka} uppercase words.")
print(f"There are {vsechna_mala} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.")
print("The sum of all the numbers:", sum(suma_cisel))
print(oddelovac * 43)

lenght = "LEN|"
occurences = "       OCCURENCES       "
nr_ = "|NR."

print(f"{lenght}{occurences}{nr_}")
print(oddelovac * 43)

slovnik = {}

for delka_slova in words_text_final:
    if len(delka_slova) not in slovnik:
        slovnik[len(delka_slova)] = 1
    else:
        slovnik[len(delka_slova)] += 1

for j, i in sorted(slovnik.items()):
    print("{:3}|".format(j), "{:23}|".format("*" * i), "{}".format(i))
