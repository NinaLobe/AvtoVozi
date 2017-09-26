#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Avto import Avto


# napise trenutni seznam v konzolo
def tiskaj_seznam(seznam_vozil):
    for v in seznam_vozil:
        print v.znamka
        print v.model
        print v.km
        print v.servis
#vpiše seznam v datoteko - seznam dela ok, za vnos bomo se videli
def vpisi_avto(seznam_vozil):
    # shranimo v file
    seznam_file = open("seznam.txt", "w+")
    seznam_file.write("Seznam vozil: \n")

   # seznam_file.write(str(tiskaj_avto(seznam_vozil))) - vprasaj zakaj
    for index, vozilo in enumerate(seznam_vozil):
        #seznam_file.write(tiskaj_avto(seznam_vozil)) - vprasaj zakaj
        seznam_file.write("Id: " + str(index)+ "\n")
        seznam_file.write("Znamka: "+ vozilo.znamka +"\n")
        seznam_file.write("Model: " + vozilo.model + "\n")
        seznam_file.write("Prevozenih km: " + vozilo.km + "\n")
        seznam_file.write("Naslednji servis: " + vozilo.servis + "\n")
        seznam_file.write("\n")


#vpise nov avto v seznam znotraj programa, avtomatsko v oba seznama
def vpisi_nov_avto(seznam_vozil):

    znamka=raw_input("Znamka: ")
    model=raw_input("model: ")
    km=raw_input("prevozenih km: ")
    servis=raw_input("Servis: ")

    nov_avto = Avto(znamka=znamka,model=model,km=km,servis=servis)
    seznam_vozil.append(nov_avto)

    vnos_v_bazo(seznam_vozil)
    vpisi_avto(seznam_vozil)

def vnos_v_bazo(seznam_vozil):
    # shranimo v file za vnos nazaj z drugim obiskom programa
    seznam_file = open("vnos.txt", "w+")

    for index, vozilo in enumerate(seznam_vozil):
        seznam_file.write(str(index)+ "\n")
        seznam_file.write(vozilo.znamka+ "\n")
        seznam_file.write(vozilo.model+ "\n")
        seznam_file.write(vozilo.km+ "\n")
        seznam_file.write(vozilo.servis+ "\n")

def edit_km(seznam_vozil):
    print "Spremenimo prevožene km našega vozila: "

    for index, Avto in enumerate(seznam_vozil):
        print str(index) + ") " + Avto.znamka

    print ""  # empty line
    selected_id = int(raw_input("Kateremu vozilu bi rad-a spremnil-a km? (vnesi ID): "))
    selected_vozilo = seznam_vozil[int(selected_id)]
    print selected_vozilo.km
    nov_km = raw_input("Prosim vnesi nove km: ")
    selected_vozilo.km=nov_km

    print ""  # empty line
    print "Km posodobljeni."
    print selected_vozilo.km
    # ... you can do the same for other fields.
def edit_servis(seznam_vozil):
    print "Spremenimo datum servisa na vozilu: "

    for index, Avto in enumerate(seznam_vozil):
        print str(index) + ") " + Avto.znamka

    print ""  # empty line
    selected_id = int(raw_input("Kateremu vozilu bi rad-a spremnil-a datum servisa? (vnesi ID): "))
    selected_vozilo = seznam_vozil[int(selected_id)]
    print selected_vozilo.servis
    nov_servis = raw_input("Vnesi datum servisa: ")
    selected_vozilo.servis=nov_servis

    print ""  # empty line
    print "Servis posodobljen."
    print selected_vozilo.servis
    # ... you can do the same for other fields.

def delete_avto(seznam_vozil):
    print "Izbris vozila: "

    for index, Avto in enumerate(seznam_vozil):
        print str(index) + ") " + Avto.znamka

    print ""  # empty line
    selected_id = int(raw_input("Izberi katero vozilo je za izbris? (enter ID number): "))
    selected_contact = seznam_vozil[int(selected_id)]

    seznam_vozil.remove(selected_contact)
    print ""  # empty line
    print "Vozilo je bilo izbrisano"

def preberi_bazo(seznam_vozil):
    with open("vnos.txt", "r") as ins:
        nov_avto=Avto(znamka="",model="",km="",servis="")

        for line in ins:
            nov_avto=Avto(line)
            seznam_vozil.append(nov_avto)
'''
def save(self):
    f = open('vnos.info', 'w')
    f.write(self.znamka + '\n')
    f.write(str(self.model) + '\n')
    f.write(str(self.km) + '\n')
    f.write(str(self.servis) + '\n')
    f.close()
'''
'''
def loadFromFile(self):
    f = open('vnos.info', 'r')
    self.znamka = f.readline().rstrip()
    self.model = f.readline()
    self.km = f.readline()
    self.servis = f.readline()


    nov_avto = Avto(znamka=self.znamka,model=self.model,km=self.km,servis=self.servis)
    seznam_vozil.append(nov_avto)
    '''