import pypokedex
import PIL.Image , PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO
pokemon = pypokedex.get(name="charmander")


window = tk.Tk()
window.geometry("450x787")
window.resizable(0,0)
window.title("POKEDEX_SPAGETTI_CODE_v1")
window.configure(bg="black")
window.config(padx=6, pady=6)

title_label = tk.Label(window,text="POKE-DEX")
title_label.config(padx=10, pady=10)
title_label.config(font=("Arial" ,32))

pok = PIL.ImageTk.PhotoImage(PIL.Image.open('pokemon.jpg'))
openlabel = tk.Label(window, image = pok)
openlabel.config(bg='black',fg='black')
openlabel.image = pok
openlabel.pack()

pokemon_image1 = tk.Label(window)
pokemon_image1.pack(padx=10, pady=10)
pokemon_image1.configure(bg="black")

label1 = tk.Label(window)
label1.config(bg="black",font=("Helvetica",20),foreground="white")
label1.pack(padx=10, pady=10)


pokemon_image2 = tk.Label(window)
pokemon_image2.pack(padx=10, pady=10)
pokemon_image2.configure(bg="black")

label2 = tk.Label(window)
label2.config(bg="black",font=("Helvetica",20),foreground="white")
label2.pack(padx=10, pady=10)

pokemon_info = tk.Label(window)
pokemon_info.pack(padx=10, pady=10)
pokemon_info.config(font=("Helvetica",15))
pokemon_info.configure(bg="black",foreground="white")

pokemon_types = tk.Label(window)
pokemon_types.pack(padx=10, pady=10)
pokemon_types.config(font=("Helvetica",14))
pokemon_types.configure(bg="black",foreground="white")

pokemon_abilities = tk.Label(window)
pokemon_abilities.pack(padx=10, pady=10)
pokemon_abilities.config(font=("Helvetica",12))
pokemon_abilities.configure(bg="black",foreground="grey")


def onload_pokemon():
    pokemon=pypokedex.get(name=text_id.get(1.0,"end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET',pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img1 = PIL.ImageTk.PhotoImage(image)
    pokemon_image1.config(image=img1)
    pokemon_image1.image = img1

    label1.config(text=f"Normal",font=("helvetica",13))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('shiny'))
    image = PIL.Image.open(BytesIO(response.data))

    img2 = PIL.ImageTk.PhotoImage(image)
    pokemon_image2.config(image=img2)
    pokemon_image2.image = img2

    label2.config(text=f"Shiny",font=("helvetica",13))


    pokemon_info.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]))
    pokemon_abilities.config(text=f"Hp = {pokemon.base_stats.hp}  Atk = {pokemon.base_stats.attack}  Def = {pokemon.base_stats.defense} \n Height={pokemon.height} Weight={pokemon.weight}")

label_id = tk.Label(window,text="ID / Name")
label_id.config(font=("Helvetica",13))
label_id.pack(padx=10, pady=10)
label_id.configure(bg="black",foreground="white")

text_id = tk.Text(window,height=1)
text_id.config(font=("Helvetica",12))
text_id.pack(padx=10, pady=10)

btn_id = tk.Button(window,text=f" ?",command=onload_pokemon)
btn_id.config(font=("Helvetica",13),bg="white")
btn_id.pack(padx=9, pady=9)



window.mainloop()

