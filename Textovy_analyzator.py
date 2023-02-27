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

while True:
    if registrated.get(user) != password:
        print(f"Username: {user}\nPassword: {password}")
        print(f"Incorrect username: \"{user}\" or password: \"{password}\". \nTerminating the program...")
        quit()
    else:
        print(f"Username: {user}\nPassword: {password}")
        print(oddelovac * 43)
        print(f"Welcome to the app, {user}.\nWe have 3 texts to be analyzed.")
        print(oddelovac * 43)        
        break

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

# počet slov začínajících velkým písmenem
pocet_prvnivelke = 0
for pocet in words_text_final:
    if pocet.istitle():
        pocet_prvnivelke += 1
print(f"There are {pocet_prvnivelke} titlecase words.")

# počet slov psaných velkými písmeny
vsechna_velka = 0
for velka in words_text_final:
    if velka.isupper() and velka.isalpha():
        vsechna_velka += 1
print(f"There are {vsechna_velka} uppercase words.")

# počet slov psaných malými písmeny
vsechna_mala = 0
for mala in words_text_final:
    if mala.islower() and mala.isalpha():
        vsechna_mala += 1
print(f"There are {vsechna_mala} lowercase words.")

# počet čísel (ne cifer)
pocet_cisel = 0
for pocet in words_text_final:
    if pocet.isdigit():
        pocet_cisel += 1
print(f"There are {pocet_cisel} numeric strings.")

# sumu všech čísel (ne cifer) v textu.
suma_cisel = []
for cisla in words_text_final:
    if cisla.isdigit():
        suma_cisel.append(int(cisla))
print("The sum of all the numbers:", sum(suma_cisel))
print(oddelovac * 43)

delka1 = []
delka2 = []
delka3 = []
delka4 = []
delka5 = []
delka6 = []
delka7 = []
delka8 = []
delka9 = []
delka10 = []
delka11 = []
delka12 = []
delka13 = []
delka14 = []

for graf in words_text_final:
        if len(graf) == 1:
            delka1.append(graf)
        elif len(graf) == 2:
            delka2.append(graf)
        elif len(graf) == 3:
            delka3.append(graf)
        elif len(graf) == 4:
            delka4.append(graf)
        elif len(graf) == 5:
            delka5.append(graf)
        elif len(graf) == 6:
            delka6.append(graf)
        elif len(graf) == 7:
            delka7.append(graf)
        elif len(graf) == 8:
            delka8.append(graf)
        elif len(graf) == 9:
            delka9.append(graf)
        elif len(graf) == 10:
            delka10.append(graf)
        elif len(graf) == 11:
            delka11.append(graf)
        elif len(graf) == 12:
            delka12.append(graf)
        elif len(graf) == 13:
            delka13.append(graf)
        else:
            delka14.append(graf)

sloupec1 = "*" * len(delka1)
sloupec2 = "*" * len(delka2)
sloupec3 = "*" * len(delka3)
sloupec4 = "*" * len(delka4)
sloupec5 = "*" * len(delka5)
sloupec6 = "*" * len(delka6)
sloupec7 = "*" * len(delka7)
sloupec8 = "*" * len(delka8)
sloupec9 = "*" * len(delka9)
sloupec10 = "*" * len(delka10)
sloupec11 = "*" * len(delka11)
sloupec12 = "*" * len(delka12)
sloupec13 = "*" * len(delka13)
sloupec14 = "*" * len(delka14)

nr_sloupec1 = len(sloupec1)
nr_sloupec2 = len(sloupec2)
nr_sloupec3 = len(sloupec3)
nr_sloupec4 = len(sloupec4)
nr_sloupec5 = len(sloupec5)
nr_sloupec6 = len(sloupec6)
nr_sloupec7 = len(sloupec7)
nr_sloupec8 = len(sloupec8)
nr_sloupec9 = len(sloupec9)
nr_sloupec10 = len(sloupec10)
nr_sloupec11 = len(sloupec11)
nr_sloupec12 = len(sloupec12)
nr_sloupec13 = len(sloupec13)
nr_sloupec14 = len(sloupec14)

lenght = "LEN|"
occurences = "   OCCURENCES   "
nr_ = "|NR."

print(f"{lenght}{occurences}{nr_}")
print(oddelovac * 43)

print(f"""  1|{sloupec1.ljust(1)} {nr_sloupec1} 
  2|{sloupec2.ljust(1)} {nr_sloupec2} 
  3|{sloupec3.ljust(1)} {nr_sloupec3} 
  4|{sloupec4.ljust(1)} {nr_sloupec4} 
  5|{sloupec5.ljust(1)} {nr_sloupec5} 
  6|{sloupec6.ljust(1)} {nr_sloupec6}
  7|{sloupec7.ljust(1)} {nr_sloupec7} 
  8|{sloupec8.ljust(1)} {nr_sloupec8}
  9|{sloupec9.ljust(1)} {nr_sloupec9} 
 10|{sloupec10.ljust(1)} {nr_sloupec10}
 11|{sloupec11.ljust(1)} {nr_sloupec11} 
 12|{sloupec12.ljust(1)} {nr_sloupec12}
 13|{sloupec13.ljust(1)} {nr_sloupec13} 
 14|{sloupec14.ljust(1)} {nr_sloupec14} 
"""
)