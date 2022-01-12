def mi_funcion():
    print("hola mundo")

mi_funcion()
def mi2_funcion():
    return "hola mundo2"

frase = mi2_funcion()
print(frase)

def nombre_apellido(nombre,apellido):
    nombre_completo = nombre,apellido
    print(nombre_completo)

nombre_apellido("Wilson","Avila")

def saludar (nombre, mesaje="hola"):
    print(nombre,mesaje)

saludar("Eduardo")
saludar(mesaje="Buen dia", nombre="Obed")

def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios):
    print(parametro_fijo)
# Los parámetros arbitrarios se corren como tuplas
    for argumento in arbitrarios:
        print(argumento)
recorrer_parametros_arbitrarios('Wilson', 'Desayuno', 'Almuerzo','Cena')
