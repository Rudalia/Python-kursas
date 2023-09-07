# This is a sample Python script.
import string

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


# 2023 - 09 -05 uzduotys ir ju sprendimai
    #
    # skaicius = 42
    #
    # if skaicius:
    #     print("daugiau uz ")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# sarasas = [1,2,3,4,5]
# for elementas in sarasas:
#     print("Elementas:", elementas)

    # for i in range(5,0,-1):
    #     print (i)

# skaiciai = [24.11.72.34.7.84]
#
# didziausias_skaicius = skaiciai[0]
#
# for skaicius in skaiciai:
#     if skaicius > didziausias_skaicius:
#         didziausias_skaicius = skaicius
# print("Didziausias skaicius yra: ", didziausias_skaicius)


# skaicius = int(input("iveskite skaiciu: "))
# suma = 0
#
# for i in range(1, skaicius + 1):
#     suma += i
# print ("Skaiciu suma nuo 1 iki", skaicius, "yra", suma)

# Is saraso isfiltruoti lyginius skaicius

# sarasas = [2,5,11,25,9]
# lyginiai_skaiciai = []
#
# for skaicius in sarasas:
#     if skaicius %2 == 0:
#         lyginiai_skaiciai.append(skaicius)
# print("lyginiai_skaiciai", lyginiai_skaiciai)



# eiluciu_sk = int(input("iveskite sveika skaiciu"))
# for eilute in range(1,eiluciu_sk+1):
#     tarpas = eiluciu_sk - eilute
#     zvaigzd = 2 * eilute -1
    # print(" " * tarpas + " * " * zvaigzd)

    # surasti pirminius skaicius is intervalo [10;50] pirminiai skaiciai

# pradzia = 10
# # pabaiga = 50
# #
# # print(f"pirminiai_skaiciai tarp {pradzia} ir {pabaiga} yra: ")
# # for skaicius in range(pradzia, pabaiga + 1):
# #     if skaicius > 1:
# #         for daliklis in range(2,skaicius):
# #             if (skaicius % daliklis)==0:
# #                break
# #         else:
# #             print(skaicius)

# Rasti zodzius, kurie prasideda is a.

# zodziai_is_a = ["as", "tu", "jis", "asta", "marius"]
#
# raide = "a"
# for zodis in zodziai_is_a:
#     if zodis[0].lower()==raide.lower:
#         print("zodis")

# 5. Sudaryti ir isvesti daugybos lentele.

# print("daugybos lentele nuo 1 iki 10")
# for i in range(1,11):
#     for j in range(1,11):
#         rezultatas = i*j
#         print(f"{i} x {j} = {rezultatas}")
#         print()


# 6. Patikrinti ar ivestas vartotojas sk yra teig ar neig arba nulis

# skaicius = int(input("iveskite skaiciu_>"))
#
# if skaicius > 0:
#     print("ivestas skaicius yra teigiamas")
# elif skaicius > 0:
#     print("ivestas skaicius yra neigiamas")
# else:
#     print("ivestas skaicius = nulis")


# 7. isvesti fizz skaiciams, kurie dalijasi is 3, buzz skaiciams, kurie dalijasi ie 5, fizzbuzz skaiciai, kurie
# dalijasi is 3 ir 5 intervale nuo 1 iki 100.


# for skaicius  in range(1,101):
#     if skaicius % 3 ==0 and skaicius %5 ==0:
#         print("fizzbuzz")
#     elif skaicius % 3 ==0:
#         print("fizz")
#     elif skaicius % 5 ==0:
#         print("buzz")
#     else:
#         print("skaicius")


# 8. Sukurkite skaiciu atspejimo zaidima
#
# ...
# import random
#
# ...
# pasleptas_skaicius = random.randint( a: 1, b: 100)
# bandymai = 0
# maksimalus_bandymu_skaicius = 10
# while bandymai < maksimalus_bandymu_skaicius:
#     Spejimas = int(input("atspekite paslepta skaiciu nuo 1 iki 100:"))
#     bandymai += 1
#     if spejimas == pasleptas_skaicius:
#         print(f"Valio! Atspejote skaiciu per {bandymai} bandymus")
#         break
#     elif spejimas < pasleptas_skaicius:
#         print("Bandykite didesni skaiciu")
#     else:
#         print("Bandykite mazesni skaiciu")
# if bandymai >= maksimalus_bandymu_skaicius:
#     print(f"Jus pasiekete maksimalu bandymu skaiciu. pasleptas skaicius buvo {pasleptas_skaicius}") pasitikrinti dar

# 9. Sukurti zodziu sarasa, kur saugomi zodziai ir ju ilgiai, reikia isvesti zodzius kuriu ilgiai ilgesni
# nei 6 simboliai

# zodziai = ["kaimas", "miestas", "savivaldybe", "miestelis", "gyvenviete", "mama", "tetis"]
# zodynas = {}
# for zodis in zodziai:
#     zodynas[zodis] = len(zodis)
# for zodis, ilgis in zodynas.items():
#     if ilgis > 6:
#         print(f"{zodis}: {ilgis} simboliai")


# 1. Sukurkite žodyną ir trumpą tekstą. Atspasudinkite žodžius,
# # kurie pasikartojo daugiau nei 3 kartus.
#
# # zodynas = []
# # tekstas = Metuose yra dvylika mnesiu. Kiekvienas menuo turi 30 arba 31 dienas. Vienas menuo metuose turi maziau
# nei 30 dienas. Tai Vasario menuo, kuris turi 28 dienas. Kas ketveri metai Vasaris turi 29 dienas. Tai visi menesiai
# turi arba 30, arba 31 dienas.

# tekstas = """Metuose yra dvylika menesiu. Kiekvienas menuo turi 30 arba 31 dienas.
#  Vienas menuo metuose turi maziau nei 30 dienas. Tai Vasario menuo, kuris turi 28 dienas.
#  Kas ketveri metai Vasaris turi 29 dienas. Tai visi menesiai turi arba 30, arba 31 dienas."""
#
# # Skaidome tekstą į žodžius
# zodziai = tekstas.lower().split()
#
# # Kuriamas žodynas žodžių pasikartojimams sekti
# zodynas = {}
#
# for zodis in zodziai:
#     zodynas[zodis] = zodynas.get(zodis, 0) + 1
#
# # Išvedame žodžius, kurie pasikartojo daugiau nei 3 kartus
# print("Žodžiai, kurie pasikartojo daugiau nei 3 kartus:")
# for zodis, kartai in zodynas.items():
#     if kartai > 3:
#         print(zodis)


# 2 .Sukurti sąrašą žodžių ir išvesti unikalius žodžius bei jų pasikartojimo dažnumą;

# zodziai = ["lova", "spinta", "palapine", "lagaminas", "spintele", "kuprine", "kelnes", "batai", "bateliai",
#            "kaliosai", "pizama", "laikrodis"]
# unikalus_zodziai = prasideda "l" ir "b"
# for unikalus_zodziai in zodziai


#
# zodziai = ["lova", "spinta", "palapine", "lagaminas", "spintele", "kelnes", "kuprine", "kelnes", "batai", "bateliai",
#            "kaliosai", "pizama", "lova", "laikrodis"]
#
# # Kuriamas žodynas žodžių pasikartojimams sekti
# zodynas = {}
#
# for zodis in zodziai:
#     zodynas[zodis] = zodynas.get(zodis, 0) + 1
#
# # Išvedame unikalius žodžius bei jų pasikartojimo dažnumą
# for zodis, kartai in zodynas.items():
#     print(f"'{zodis}': {kartai} kartus")
#
# # Sukurkite žodyną ir trumpą tekstą. Atspasudinkite žodžius, kurie pasikartojo daugiau nei 3 kartus.
#
# trumpas_tekstas = "visi visi visi norėjo alaus, bet buvo tik tuščios alaus bačkos ir rarūgusio vyno alaus buteliuose"
# žodynas = {}
# zodziai = trumpas_tekstas.split()
# for zodis in zodziai:
#     zodis = zodis.strip(",.")
#     žodynas[zodis] = žodynas.get(zodis, 0) + 1
# for zodis, pasikartojimai in žodynas.items():
#     if pasikartojimai >=3:
#         print(f"pasikartojantis(-ys) Žodis(-iai) yra: {zodis}, pasikartojo {pasikartojimai} kartų")
#
# pasižiūrėti strip

# 3. Sukurkite žodyną su studentų duomenimis ir atspausdinkite studentus, kurių vidurkis yra aukščiau 8.0;


...
# import string

...

# ilgis = 7
# simboliai = string.ascij_letters + string.digits + string.punctuation
# random_string = '' . join(random.choise(simboliai) for _ in range(ilgis))
# print('random_string', random_string)

# ilgis = 7
# simboliai = string.ascii_letters + string.digits + string.punctuation
# random_string = ''.join(random.choice(simboliai) for _ in range(ilgis))
# print("random_string", random_string)


# 3. Sukurkite žodyną su studentų duomenimis ir atspausdinkite studentus, kurių
# vidurkis yra aukščiau 8.0;

# Žodynas su studentų vardais ir jų vidurkiais
# studentai = {
#     "Jonas": 8.5,
#     "Petras": 7.9,
#     "Ona": 8.1,
#     "Eglė": 9.0,
#     "Marius": 6.5
# }
#
# # Tikriname kiekvieno studento vidurkį ir išspausdiname, jei vidurkis aukščiau 8.0
# print("Studentai, kurių vidurkis yra aukščiau 8.0:")
# for vardas, vidurkis in studentai.items():
#     if vidurkis > 8.0:
#         print(vardas)

# 4. Sukurti žodyną su knygų informacija ir surikiuoti
# knygas pagal metus ir pavadinimus.

# Knygų informacija
# knygos = [
#     {"pavadinimas": "Haris Poteris", "autorius": "J.K. Rowling", "metai": 2000},
#     {"pavadinimas": "Dangaus tiltas", "autorius": "Ruta Sepetys", "metai": 2011},
#     {"pavadinimas": "Bėgikė", "autorius": "Stephen King", "metai": 1982},
#     {"pavadinimas": "Mėnulio šviesa", "autorius": "J.K. Rowling", "metai": 2000},
# ]
#
# # Rikiuojame knygas pagal metus, tada pagal pavadinimus
# rikiuotos_knygos = sorted(knygos, key=lambda x: (x['metai'], x['pavadinimas']))
#
# # Išspausdiname surikiuotą sąrašą
# for knyga in rikiuotos_knygos:
#     print(knyga["pavadinimas"], "-", knyga["autorius"], "-", knyga["metai"])




# Parašykite programą, kuri suskaičiuoja visų sveikujų skaičių nuo 1 iki n ėjimo sumą, kur n yra vartotojo įvestas
# skaičius. Panaudokite "for" ciklą ir "if" sąlygos sakinį, kad tikrintumėte, ar įvestas skaičius yra sveikasis;


# n = int(input("iveskite skaiciu:"))
# if n <= 0:
#     print("ivestas skaicius turi buti sveikasis, bandykite dar")
# else:
#     suma = 0
#     for skaicius in range(1,n + 1):
#         suma += skaicius
#     print(f'suuma nuo1 iki {n} yra {suma}')


# 2. Sukurkite programą, kurioje vartotojas gali įvesti mokinio pažymį (nuo 1 iki 10). Programa turi grąžinti
# mokinio vertinimą (pvz., "Neužtektinai", "Silpnai", "Vidutiniškai", "Gerai", "Puikiai").
# Naudokite "if" sąlygos sakinį;

# # Vartotojas įveda pažymį
# pazymys = int(input("Įveskite mokinio pažymį nuo 1 iki 10: "))
#
# # Tikriname pažymio vertinimą
# if pazymys >= 9 and pazymys <= 10:
#     vertinimas = "Puikiai"
# elif pazymys >= 7 and pazymys < 9:
#     vertinimas = "Gerai"
# elif pazymys >= 5 and pazymys < 7:
#     vertinimas = "Vidutiniškai"
# elif pazymys >= 4 and pazymys < 5:
#     vertinimas = "Silpnai"
# elif pazymys >= 1 and pazymys < 4:
#     vertinimas = "Neužtektinai"
# else:
#     vertinimas = "Netinkamas pažymys, įveskite pažymį nuo 1 iki 10."
#     print(f"Mokinio vertinimas: {vertinimas}")

# 4. Turite žodyną, kuriame yra vardai ir amžius. Parašykite programą,
# peržiūri žodyną ir išrenka tik tas poras,
# kuriose amžius yra didesnis arba lygus 18.
# Rezultatus patalpinkite naujame žodyne;


# Zodynas su zmoniu vadrais ir  metais
# zmones = {"Jonas": 23, "Mantas": 45, "Ona": 44, "Kotryna": 37, "Lina": 14, "Marius": 7}
# print("Zmones, kuriu amzius >= 18")
# for vardas, amzius in zmones.items():
#     if amzius >= 18:
#         print(vardas, amzius)



# 3. Sukurkite programą, kuri leidžia vartotojui įvesti metus.
# # Programa turi patikrinti, ar įvesti metai
# # yra keliamieji (dalijasi iš 4) ir atspausdinti atitinkamą pranešimą;

# vartotojas iveda metus
# metai = int(input("iveskite metus:"))
# if metai % 4 ==0:
#     print(f"keliamieji metai")
# else:
#     print(f" nekeliamieji metai")

# 5. Leiskite vartotojui įvesti kelias prekes ir jų kainas. Sukurkite sąrašą,
# kuriame prekės yra žodynai, kuriuose yra prekės pavadinimas ir kaina.
# Taip pat paskaičiuokite bendrą visų prekių kainą;

# prekiu_krepselis = []
# while True:
#     preke = input("Nurodyte prekę arba įrašykite žodį baigti")
#     if not preke:
#         break
#     kaina = float(input("Įveskite prekės kainą: "))
#     prekes_info = {'pavadinimas': preke, 'kaina': kaina}
#     prekiu_krepselis.append(prekes_info)
#
# Krepselio_suma = sum((prekes_info['kaina'] for prekes_info in prekiu_krepselis))
# print("prekiu sarasas: ")
# for prekes_info in prekiu_krepselis:
#     print(f"Pavadinimas: {prekes_info['pavadinimas']}, Kaina: {prekes_info['kaina']}")
# print(f"Bendra kaina: {Krepselio_suma}")


# 6. Turite sąrašą žmonių vardų. Sukurkite programą, kuri leidžia
# vartotojui įvesti vardą ir patikrina, ar jis yra sąraše.
# Jei vardas yra sąraše, programa turi išvesti
# pranešimą "Vardas yra sąraše," kitu atveju -"Vardo nėra sąraše."

# zmones = {
#     'Vanda'
#     'Jonas'
#     'Karina'
#     'Jole'
#     'Petras'
#     'Martynas'
#     'Mindaugas'
#
# }
# ivestas_vardas = input("Iveskite varda kuri norite patikrinti:")
# if ivestas_vardas in zmones:
#     print('Vardas yra sarase')
# else:
#     print('Vardo nera sarase')


