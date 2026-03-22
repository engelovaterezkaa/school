import random, json

studenty = {
    "Sofie": "",
    "Dolomil": "",
    "Diviš": "",
}

path = "znamky.json"

def uloz_znamku():
    with open(path, mode="w") as file:
        json.dump(studenty, file, indent=4)
    print("Uloženo")

def udel_znamku():
    jmeno = input("Vyber si jméno: ")

    if jmeno in studenty:
        znamka = random.randint(1, 5)
        studenty[jmeno] = znamka
        for key, value in studenty.items():
            print(f"{key}:{value}")
        uloz_znamku()
                
    if jmeno not in studenty:
        print("Máš špatnou školu trubko")
        pridat = input("Má chodit do téhle školy? Ano nebo Ne? ")
        znamka = random.randint(1, 5)

        if pridat == "Ano": 
            studenty[jmeno] = znamka
            for key, value in studenty.items():
                print(f"{key}:{value}")
            uloz_znamku()
    
        if pridat == "Ne":
            print("Tak čauťe")
            


udel_znamku()
print("damn")