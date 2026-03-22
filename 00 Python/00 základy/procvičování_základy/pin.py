pin = int(input("Zadej pin:"))
#pin = int(pin) prevadi to na čísla, protože promenne se prijimaji jako string
pokus = 0


i = 0
while pin !=1234:
    pin = int(input("Zadej pin:"))
    if pokus > 2:
        break
        pokus +=1

print("spravne")


#while pin !=1234 or pokus > 2:
#    pin = int(input("Zadej pin:"))
#    pokus +=1


#nebo lze napsat:

while True:
    pin = int(input("Zadej pin:"))
    if pin == 1234:
        print("spravne")
        break
    elif pokus > 2:
        print("moc pokusu")
        break
    print("spatne")
    pokus +=1