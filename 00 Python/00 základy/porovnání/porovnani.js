let krestniJmeno = "Hugo"
let cislo = 5
let pravda = true

let seznamStudentu = ["Emil", "Emilie", "Jarmil", "Jarmila", "Hvězdoň"] /*array*/


console.log(krestniJmeno)

function NahodnaFunkce() {
    console.log("funguje")
}


NahodnaFunkce()

if (cislo > 0) {
    console.log("číslo je kladné")
} else if (cislo < 0) {
    console.log("číslo je záporné")
} else {
    console.log("číslo je 0")
}


/*cykly*/
let i = 1

while (i < 11) {
    console.log(i)
    i++
}

for (let n = 0; n < 11; n++) {
    console.log(n)
}


/*array zacina vzdy na nule */
for (let i = 0, i < seznamStudentu.length; i++)  {
    console.log(seznamStudentu[i])
}