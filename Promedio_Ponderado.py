"""
El usuario ingresa materias con su nota y sus créditos. 
Valida que la nota esté entre 0 y 5 y que los créditos sean un entero positivo. 
Guarda todo y, con una función, calcula el promedio ponderado (cada nota pesa según sus créditos). 
Al final dice si estás por encima de tu meta de 3.8.

"""

def verificar (a): #Verifica que sea un valor numero y no un texto por ejemplo
    try:
        b = float(a)
        return b
    except ValueError:
        print("Debes seleccionar un valor numerico")
        b = False
        return b


materias_totales = { # se creal el diccionario para añadir las materias, notas y creditos

}

cantidad = 0

while True:
    terminar = input("Vas a agregar alguna materia para calcular tu promedio? si/no: ")
    match terminar:
        case "si":
            cantidad += 1 # solo para ver cuantas materias tiene y verificar que por lo menos haya una
        case "no":
            if cantidad < 1:
                print("debe haber al menos 1 materia para calcular el promedio") # si no tiene ninguna no se puede
                continue
            break

        case _:
            print("selecciona una opcion valida") # si el usuario se equivoca y selecciona alguna cosa que no este en las opciones
            continue


    while True:
        materia = input("Escribe La materia: ")
        try:
            a = int(materia)
            print("No se aceptan numeros como materias") # si ingresa un numero no se puede porque no existen materias que se llamen por numeros
        except ValueError:
            if materia in materias_totales:
                print("No puedes tener materias repetidas") # verifica que no se repitan materias
                continue
            break

    while True: 
        nota = input("Escribe la nota (una valida): ")
        a = nota
        b = verificar(a)
        if b or b == 0:
            nota = b
            if 0 <= b <= 5: #Verifica que la nota de la materia sea valida
                break
            else:
                print("La nota solo se acepta entre 0 y 5")
                continue
        else: # verifica con la funcion que sea un numero
            continue

    while True: 
        creditos = input("Escribe los creditos: ")
        a = creditos
        b = verificar(a)
        if b:
            if 0 < b:
                if int(b) == b:
                    creditos = int(b)
                    break
                print("No existen creditos con decimales")
                continue
            else: # Verifica que no se ingresen creditos negativos o 0 creditos ya que no se puede
                print("Los creditos deben ser mayores a 0")
                continue
        else: # verifica con la funcion que sea un numero
            if b == 0:
                print("Los creditos no pueden ser 0")
            continue

    materias_totales.update({materia: (nota,creditos)}) # Añade las materias, nota y creditos a nuestro diccionario

"""
Guia de como separe los datos del diccionario

print(materias_totales)
for nombre_materia,datos in materias_totales.items():
    print(nombre_materia)
    print(datos[0])
    print(datos[1])

"""

def calcular_prom(materias):
    creditos_totales = 0
    suma_promedio = 0
    for nom_materia,datos in materias.items():
        creditos_totales += datos[1]
        suma_promedio += (datos[0] * datos[1])
    return round(suma_promedio / creditos_totales,2)


promedio_ponderado = calcular_prom(materias_totales)

print()
print("==============Promedio Ponderado==============")
print()
print(f"Para un total de {cantidad} materias")
if promedio_ponderado >= 3.8:
    print(f"Tu promedio de {promedio_ponderado} si alcanza")
else:
    print(f"Tu promedio de {promedio_ponderado} no alcanza")
print()