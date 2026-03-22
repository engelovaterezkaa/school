# 0(index)-Alice(value) -> kdyz cislujeme array, "student"(key)-Bob
#muzeme dosazovat i cisla napr. "year" : 25

#JSON - slovnik

ukazka = {
    "student" : "Alice",
    "teacher" : "Bob",
    "janitor" : "Charlie"
} 

#vypsani jedne hodnoty
print(ukazka["teacher"]) #odkazujeme na key
print(ukazka["student"])

cat = {
    "name" : "Mycash",
    "age" : 5,
    "colour" : "black",
    "fav_food" : "lasagna",
    "alive" : True,
    "friends" : ["Tom", "Jerry"] #lze psat vice hodnot
}

print(cat["colour"])

#vypsani hodnoty ze seznamu
print(cat["friends"][1])

# lze vse kombinovat: random_list = [{"stuff": "blabla"}, {"happy":"not really"}]

#print(cat) - vypise vsecvhno i s key

#vypsani vseho==
#for key in cat:
#    print(key)


#1.zp
for key in cat: 
    print(cat[key]) 

    #cat[key]=> 1.kolo cat["name"]; 2.kolo cat["age"]
    #cyklus for vypisuje levou cast

#2.zp
for value in cat.values(): #cat.values - vraci hodnoty, vypise vsechno
    print(value)

#3.zp, items vypisuje 2 hodnoty, for je opakuuje
#for key, value in cat.items(): 
#        for value in cat[key]:
#            print(f"Tohle je key {key}. tohle je value {value}")

#for friend in cat["friends"]:
#    print(friend)

for key, value in cat.items():
     print(f"Tohle je key {key}, tohle je value {value}")

#zmena/prepsani value
cat["fav_food"] = "mouse"
for key in cat: 
    print(cat[key]) 

#pres podminku lze zjistit jestli se tenhle value v dokumentu nachazi
if "fav_food" in cat:
    print(cat["fav_food"])

#pridani hodnoty (key)
cat["number_of_legs"] = 4
for key in cat: 
    print(cat[key]) 

