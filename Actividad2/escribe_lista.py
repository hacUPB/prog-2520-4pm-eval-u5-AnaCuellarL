lista = ["Una sonrisa al atardecer- Akash", "Niente da dire -Maneskin", "Brujas-Magö de Oz", "Your Rock my world- Michael Jackson", "Hace tiempo-Heroes del silencio"]
ruta ="C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\Actividad2"
file_name = "canciones.txt"
file_info = ruta+"\\"+file_name
modo = "w"
for i in range(len(lista)):
    lista[i] += "\n"
    '''for cancion in lista:
        fp.write(cancion+"\n")
    Otra forma de hacerlo'''
fp= open(file_info, modo, encoding="utf-8")
fp.writelines(lista)
fp.close()

