import tkinter as tk

def say_hello():
    print("Hello!")
    label_example.config(text="Hello :D") #meni nadpis(v label_example)

root = tk.Tk()

root.title("Hello?") #nadpis okna
root.geometry("800x600") #velikost 

label_example = tk.Label(root, text="Toto je pěkný text", font=("Consolas", 20)) #(kam ho cheme ulozit, jaky obsah tam napiseme, font je nepoviny)
label_example.pack() #pack hazi pod sebe, grid rika do jake rady a sloupce v text souboru: .grid(row=0, column=1)
#bud grid(mřížka) nebo pack

#text = .., image = "adresa obrázku"

btn_example = tk.Button(root, text="Click me", command=say_hello) #funkce nemaji zde zavorky; command=lambda: say_hello(label_example)
btn_example.pack() #nahrava se do gui

btn_example2 = tk.Button(root, text="Click me", command=lambda: say_hello(label_example))
btn_example2.pack()

root.mainloop()