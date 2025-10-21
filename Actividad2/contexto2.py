# Solicitamos al usuario el nombre del archivo a crear
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")

# Usamos 'with' para crear el contexto y escribir datos en el archivo 
with open(nombre_archivo, 'w') as archivo:
    # Solicitamos al usuario los datos a escribir en el archivo
    datos = ["Hola,¿cómo estas?\n", "Bien,¿y tú?\n", "Bien\n"]
    archivo.writelines(datos)

# Ahora usamos 'with' para crear el contexto donde leer los datos del archivo
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)