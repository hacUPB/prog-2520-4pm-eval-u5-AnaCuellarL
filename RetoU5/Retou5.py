from modulo import cont1 , cont2, cont3, reemplazador_de_palabras , histogram, filas_csv, main, grafics  
import matplotlib.pyplot as plt, csv, pandas as pd, statistics, seaborn as sns

try:
    Bandera=True
    while Bandera==True:
        opcion= int(input("\n1.Consultar archivos disponibles.\n2. Ingreso al archivo .txt\n3. Ingreso al archivo .csv\n4.Salir\nElija una opción: \n"))
        if opcion==1:
            print("los textos disponibles son:")
            print("cuento_para_dormir.txt")
            print("llegada_pax_de_origen_ncl.csv")
        elif opcion== 2:
            bandera=True
            while bandera==True:
                opcion2= int(input("1.Conteo de palabras y caracteres\n2. Reemplazar palabras\n3.histograma de ocurrencia de vocales\n4. Salir\nElija una opción: \n"))
                if opcion2 == 1:               
                    bandera2= True
                    while bandera2==True:
                        opcion3= int(input("1. Contador de palabras\n2. Contador de caracteres con espacios\n3. Contador de caracteres sin espacios\n4. Salir\nElija una opcion: \n"))
                        if opcion3==1:
                            cont1()
                        elif opcion3== 2:
                            cont2()
                        elif opcion3== 3:
                            cont3()
                        elif opcion3== 4:
                            print("Volviendo al menú anterior")
                            bandera2 = False
                        elif opcion3>4:
                            print("Opción no valida")
                        elif opcion3<1:
                            print("Opción no valida")
                elif opcion2== 2:
                    reemplazador_de_palabras()
                elif opcion2== 3:
                    histogram()
                elif opcion2== 4:
                    print("Volviendo al menú anterior")
                    bandera= False
                elif opcion2<1:
                    print("Opción no valida")
                elif opcion2>4:
                    print("Opción no valida")                
        elif opcion== 3:
            bandera3= True
            while bandera3==True:
                opcion4= int(input("1. Mostrar las 15 primeras filas\n2. Calculadora de Estadísticas\n3. Graficar una columna completa de datos\n4.Salir\nElija una opción: \n"))
                if opcion4==1:
                    filas_csv()
                elif opcion4==2:
                    main()
                elif opcion4==3:
                    grafics()
                elif opcion4==4:
                    print("Volviendo al menú anterior")
                    bandera3=False
                elif opcion4<1:
                    print("Opción no valida")
                elif opcion4>4:
                    print("Opción no valida")            
        elif opcion==4:
            print("Gracias por usar este programa.")
            Bandera=False
        elif opcion<1:
            print("Opción no valida")
        elif opcion>4:
            print("Opción no valida")        
except ValueError:
     print("El valor ingresado no es un número")