import csv
Temperatura=[]
humedad= []
Presion =[]

with open('C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\Actividad3\\CSV_1.csv','r') as csvfile:
    lector = csv.reader(csvfile, delimiter = ";")
    #print(lector)
    encabezado = next(lector)
    for fila in lector:
       dato= int(fila[0])
       Temperatura.append(dato)
    print(encabezado[0])
    print(Temperatura)
    
    csvfile.seek(0)
    next(lector)
    for fila in lector:
       dato= int(fila[1])
       humedad.append(dato)
    print(encabezado[1])
    print(humedad)

    csvfile.seek(0)
    next(lector)
    for fila in lector:
       dato= fila[2]
       dato = float(dato.replace(",","."))
       Presion.append(dato)
    print(encabezado[2])
    print(Presion)

