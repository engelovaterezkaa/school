krestni_jmeno = "Hugo" #nepouzivame let aby jsme udelali promennou
cislo = 5
pravda = True

seznam_studentu = ["Emil", "Emilie", "Jarmil", "Jarmila", "Hvězdoň"] #list


print(krestni_jmeno)
#misto console log

def nahodna_funkce(): #def = funkce
    print("funguje")
#nutné odsadit, co je odsazené patří do funkce, to samé je u podmínek
#nepoutivaji se slozene zavorky ale odsazeni a dvojtecky

nahodna_funkce() #spusteni funkce

#podminky
if cislo > 0:
    print("číslo je kladné")
elif cislo < 0: #else if = elif
    print("číslo je záporné")
else:
    print("číslo je 0")


#cykly
i = 1

while i < 11:
    print(i)
    i+=1 # +=1 místo ++, ++ nefunguje

#rozsah počítání= in range
for x in range(0 , 11, 1): #od kolika začíná (0), do kolika ale ne včetně (11), o kolik počítá (1; defaultně je nastavena o 1, nemusí se uvádět)
    print(x)


print(seznam_studentu[1]) #vypsani jednoho studenta

#vybira studenta (jako jednu promennou) v rozmezí seznamu studentů
for student in seznam_studentu:
    print(student) #na vypsani vsech studentu se pouziva cyklus