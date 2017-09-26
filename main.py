#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Avto import Avto
from Uprava import tiskaj_seznam
from Uprava import vpisi_nov_avto
from Uprava import vpisi_avto
from Uprava import edit_servis
from Uprava import edit_km
from Uprava import delete_avto



def main():
    print "Vasa vozila so v dobrih rokah. Aplikacija vam pomaga voditi vse tipi topi"
    '''
    vozilo=Avto(znamka="",model="",km="",servis="")
    file = open("vnos.txt", "r")
    with open('vnos.txt') as input_file:
        for line in input_file:
            print line
    
    '''

    pikec=Avto(znamka="Kia",model="Piccanto",km="130000km",servis="5.5.2018")
    turan=Avto(znamka="WV",model="Turan",km="220000km",servis="10.5.2020")

    seznam_vozil=[pikec,turan]

    #Zacetek glavnega dela programa:
    while True:
        print ""  # empty line
        print "Izberi naslednje možnosti:"
        print "a) Preveri svoj seznam vozil"
        print "b) Dodaj novo vozilo"
        print "c) Popravi prevožene km"
        print "d) Popravi datum servisa"
        print "e) Izbriši vozilo"
        print "f) Zapusti program."
        print ""  # empty line

        selection = raw_input("Vpiši svojo izbiro (a, b, c, d, e, f): ")
        print ""  # empty line

        if selection.lower() == "a":
            tiskaj_seznam(seznam_vozil)
        elif selection.lower() == "b":
            vpisi_nov_avto(seznam_vozil)
        elif selection.lower() == "c":
            edit_km(seznam_vozil)
        elif selection.lower() == "d":
            edit_servis(seznam_vozil)
        elif selection.lower() == "e":
            delete_avto(seznam_vozil)
        elif selection.lower() == "f":
            print "Hvala za uporabo našega programa. Goodbye!"
            break
        else:
            print "Oprosti, nisi dobro izbral, poskusi še enakrat"
            continue

if __name__ == '__main__':
    main()