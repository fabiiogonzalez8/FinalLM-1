import requests
import json

print("Ejercicio 1 del proyecto final de lenguaje de marcas")
print("por Fabio Gonzalez, utilizando una API de Pokémon.")

url_base='https://pokeapi.co/api/v2/'

menu='''
1) Mostrar la lista de tipos.
2) Se muestran todas las regiones pokémon, indica una y se muestra en que juego aparece.
3) Ver de que tipo es un pokémon de la primera generación.
4) Salir del programa
'''
print(menu)
opcion=int(input("Elige una opcion del menu: "))

while opcion!=4:

# EJERCICIO 1

    if opcion == 1:
        url="type/"
        r=requests.get(url_base+url)
        tipos=r.json()
        nuevostipos=[]
        print(tipos)
        for i in tipos["results"][:-2]:
            nuevostipos.append(i["name"])
        print(', '.join(nuevostipos))
        print(menu)
        opcion=int(input("Elige una opcion del menu: "))

# EJERCICIO 2

    if opcion == 2:
        url="region/"
        r=requests.get(url_base+url)
        regiones=r.json()
        listaregiones=[]
        for i in regiones["results"]:
            listaregiones.append(i["name"])
        print(', '.join(listaregiones))
        regi=input("Selecciona una región de las vistas: ")
        while regi not in listaregiones:
            regi=input("La región debe ser una de las vistas anteriormente: ")
        posicion = listaregiones.index(regi)
        cadenaposi=str(posicion+1)
        r=requests.get(url_base+url+cadenaposi)
        inforegi=r.json()
        listaregis=[]
        for i in inforegi["version_groups"]:
            listaregis.append(i["name"])
        print("Esta región aparece en los siguientes juegos: ")
        print(', '.join(listaregis))
        opcion=int(input("Elige una opción del menu: "))

# EJERCICIO 3

    if opcion == 3:
        url="pokemon/"
        parametros={'start':'1','limit':'151'}
        r=requests.get(url_base+url,params=parametros)
        pokemons=r.json()
        listapokes=[]
        for i in pokemons["results"]:
            listapokes.append(i["name"])
        poke=input('Introduce el nombre de un Pokémon de la primera generación, por ejemplo charmander: ')
        while poke not in listapokes:
            poke=input("Debe ser un pokemon que pertenezca a la primera generación, por ejemplo rattata: ")
        posicion = listapokes.index(poke)
        cadenaposi=str(posicion+1)
        r=requests.get(url_base+url+cadenaposi)
        infopokes=r.json()
        tipopoke=[]
        for i in infopokes["types"]:
            tipopoke.append(i["type"])
        name=tipopoke[0]["name"]
        print(poke,"es del tipo:",name)
        opcion=int(input("Elige una opcion del menu: "))

# SALIDA    

    else:
        opcion=int(input("Debes introducir un número del 1 al 4. Si deseas salir introduce el 4: "))
        