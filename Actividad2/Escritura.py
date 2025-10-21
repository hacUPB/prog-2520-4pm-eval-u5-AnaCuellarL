ruta = "C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\Actividad2"

file_name = "aviones1.txt"

modo = "X"

fp= open(ruta+"\\"+file_name, modo, encoding="utf-8")

nombre= input("Ingrese el nombre de un avión: ")

peso = int(input("Ingrese el peso del avión: "))

velocidad = float(input("Velocidad máxima: "))

fp.write(nombre+"\n")
fp.write(str(peso)+"\n")
fp.write(str(velocidad)+"\n")

fp.close()