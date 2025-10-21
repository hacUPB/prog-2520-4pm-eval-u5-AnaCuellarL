# 1. Leer el Archivo
fp = open("C:\\Users\\ANA SOFIA\\OneDrive - UPB\\Escritorio\\Texto_random.txt","r", encoding= "utf-8")
# 2. Leer el archivo
# datos= fp.read() lo lee todo
# datos=fp.read(20) Lee solo 20 caracteres
#datos = fp.read(7)
# 3. Cerrar el archivo
#fp.close()
#print(datos)

for linea in fp:
    print(linea[0])

fp.close()