import time 
import sys

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

required = ("\n Gebruik alleen A, B of C \n")

def begin():
    print("Je bent wakker geworden, wat ga je als eerste doen?")
    print("A | Douchen")
    print("B | Tanden Poetsen")
    print("C | Ontbijten")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_douchen()
    if choice in answer_B:
        option_tandenpoetsen()
    if choice in answer_C:
        option_ontbijten()
    else:
        print(required)
        begin()


def option_douchen():
    print("Je hebt er voor gekozen om te douchen, wacht nu 10 seconden...")
    time.sleep(10)
    print("Je bent klaar met doucen! Wat wil je nu gaan doen?")
    print("A | Tanden poetsen")
    print("B | Ontbijten")
    print("C | Spullen Pakken")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_tandenpoetsen()
    if choice in answer_B:
        option_ontbijten()
    if choice in answer_C:
        option_spullen()
    else:
        print(required)
        begin()


def option_tandenpoetsen():
    print("Je hebt er voor gekozen om tanden te poetsen, wacht nu 5 seconden...")
    time.sleep(5)
    print("Je bent nu klaar met tanden poetsen! Wat wil je nu gaan doen?")
    print("A | Ontbijten")
    print("B | Spullen pakken")
    print("C | Weg Gaan")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_ontbijten()
    if choice in answer_B:
        option_spullen()
    if choice in answer_C:
        print("Je bent weg gegaan van huis!")
        sys.exit()
    else:
        print(required)
        option_tandenpoetsen()


def option_ontbijten():
    print("Je hebt er voor gekozen om te gaan ontbijten, wat wil je eten als ontbijt?")
    print("A | Vla Met Muesli")
    print("B | Appel")
    print("C | Broodje")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Je hebt er voor gekozen om vla met muesli te eten, wacht nu 5 seconden...")
        time.sleep(5)
        print("Het is nu wel tijd om te gaan, anders kom je te laat...")
        sys.exit()
    if choice in answer_B:
        print("Je hebt er voor gekozen om een appel te eten, wacht nu 5 seconden...")
        time.sleep(5)
        print("Het is nu wel tijd om te gaan, anders kom je te laat...")
        sys.exit()
    if choice in answer_C:
        print("Je hebt er voor gekozen om een broodje te eten, wacht nu 5 seconden...")
        time.sleep(5)
        print("Het is nu wel tijd om te gaan, anders kom je te laat...")
        sys.exit()
    else:
        print(required)
        option_ontbijten()


def option_spullen():
    print("Je hebt er voor gekozen om je spullen te pakken, wacht nu 5 seconden...")
    time.sleep(5)
    print("Je spullen zijn gepakt! Wat wil je nu gaan doen?")
    print("A | Weg Gaan")
    print("B | Chillen")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Je bent weg gegaan van huis!")
        sys.exit()
    if choice in answer_B:
        print("Je hebt er voor gekozen om te chillen, wacht nu 5 seconden...")
        time.sleep(5)
        print("Het is nu wel tijd om te gaan, anders kom je te laat...")
        sys.exit()
    else:
        print(required)
        option_spullen()

begin()