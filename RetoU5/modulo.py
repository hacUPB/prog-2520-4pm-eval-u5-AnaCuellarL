import matplotlib.pyplot as plt, csv, pandas as pd, statistics, seaborn as sns
def cont1():
    ruta1 = "C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\RetoU5"

    ruta1 += "\\cuento_para_dormir.txt"
    modo="r"
# Inicio uso de IA 
    try: # Para que no corte el código si ocurre un error
        with open(ruta1, modo, encoding="utf-8") as fp:
            texto = fp.read()
            palabras = texto.split()#separa las palabras (como cadena de caracteres) de los espacios y los \n
            cantidad = len(palabras)# Recoje la cantidad de palablas
            print(f"El archivo contiene {cantidad} palabras.")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
# fin de uso de IA

def cont2():
    ruta2 = "C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\RetoU5"
    file_name= "cuento_para_dormir.txt"
    modo="r"
    fp= open(ruta2+"\\"+ file_name, modo, encoding="utf-8")
    try:
            fp= open(ruta2+"\\"+ file_name, modo, encoding="utf-8")
            with fp as archivo:
                texto= archivo.read()
                cantidad= len(texto)
                print(f" El archivo tiene {cantidad} caracteres incluyendo los espacios")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def cont3():
    ruta = "C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\RetoU5"
    file_name= "cuento_para_dormir.txt"
    modo="r"
    fp= open(ruta+"\\"+ file_name, modo, encoding="utf-8")
    try:
        with fp as archivo:
            texto= archivo.read()
            texto_sin_espacios= texto.replace(" ", "")
            cantidad= len(texto_sin_espacios)
            print(f"El archivo tiene {cantidad} caracteres sin espacios")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def reemplazador_de_palabras():
    ruta = "C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\RetoU5"
    file_name= "cuento_para_dormir.txt"
    modo="r"
    fp= open(ruta+"\\"+ file_name, modo, encoding="utf-8")
    try:
        with fp as archivo:
            palabra_antigua= str(input("Ingrese la palabra que desee reemplazar: "))
            palabra_nueva= str(input("Ingrese la palabra por la que desea reemplazar a la palabra anterior: "))
            texto= archivo.read()
            texto_modificado= texto.replace(palabra_antigua, palabra_nueva)
        modo2="w"
        fp2= open(ruta+"\\"+ file_name, modo2, encoding="utf-8")
        with fp2 as archivo:
            archivo.write(texto_modificado)
            print(f"Se reemplazó {palabra_antigua} por {palabra_nueva} en el texto")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def histogram():
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    ruta = "C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\RetoU5"
    file_name= "cuento_para_dormir.txt"
    modo="r"    
    fp= open(ruta+"\\"+ file_name, modo, encoding="utf-8")
    try:
        with fp as archivo:
            texto = archivo.read().lower()
            for letra in texto:
                if letra in vocales:
                    vocales[letra]+= 1
        plt.bar(vocales.keys(), vocales.values(), color="skyblue")
        plt.title("Histograma de ocurrencia de vocales")
        plt.xlabel("Vocales")
        plt.ylabel("frecuencia")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.savefig("histograma_vocales.png")
        plt.show()    
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def filas_csv(filas=15):
    try:
        with open('C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\RetoU5\\llegada_pax_de_origen_ncl.csv','r') as csvfile:
            lector = csv.reader(csvfile, delimiter = ";")
            contador=0
            # filas=15
            for fila in lector:
                print(fila)
                contador+=1
                if contador>=filas:
                    break
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def estadistics (archivo, columna):
    try:

        df = pd.read_csv(archivo, delimeter=";")
        datos = pd.to_numeric(df[columna], errors='coerce').dropna()
        return {
            "Número de datos": len(datos),
            "Promedio": datos.mean(),
            "Mediana": datos.median(),
            "Desviación estándar": datos.std(),
            "Máximo": datos.max(),
            "Mínimo": datos.min()
        }

    except FileNotFoundError:
        return "El archivo no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error: {e}"

def main():
    try:
        with open('C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\RetoU5\\llegada_pax_de_origen_ncl.csv','r') as archivo:       
            columna =input("Nombre de la columna: ")
            resultado = estadistics(archivo, int(columna))
            for clave, valor in resultado.items():
                print(f"{clave}: {valor}")
    except ValueError:
        print("Elvalor ingresado no es un número")
# Ejecutar main
if __name__=="__main__":
    main()

def grafics(columna_de_dispersion, columna_barras):
    try:
        columna_barras= str(input("Ingrese nombre de la columna que va a ingresar: "))
        columna_de_dispersion= int(input("Ingrese poscision de la columna a graficar: "))
        csvfile= open('C:\\Users\\ANA SOFIA\\Documents\\Repositorio-Programación\\prog-2520-4pm-eval-u5-AnaCuellarL\\RetoU5\\llegada_pax_de_origen_ncl.csv','r')
        df= pd.read_csv(csvfile, delimiter=";")
            

        # Verificar si las columnas existen
        if columna_de_dispersion not in df.columns or columna_barras not in df.columns:
            print("Una o ambas columnas no existen en el archivo.")
            return

        # Convertir la columna de dispersión a numérica
        datos_dispersion = pd.to_numeric(df[columna_de_dispersion], errors='coerce').dropna()
        indices_dispersión = range(len(datos_dispersion))

        # Gráfico de dispersión
        plt.figure(figsize=(10, 5))
        plt.scatter(indices_dispersión, datos_dispersion, color='teal', alpha=0.6)
        plt.title(f'Dispersión de la columna: {columna_de_dispersion}')
        plt.xlabel('Índice')
        plt.ylabel(columna_de_dispersion)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('grafico_dispersión.png')
        plt.close()

        # Reorganizar datos para gráfico de barras
        conteo_barras = df[columna_barras].value_counts()

        # Gráfico de barras
        plt.figure(figsize=(10, 5))
        sns.barplot(x=conteo_barras.index, y=conteo_barras.values, palette='viridis')
        plt.title(f'Frecuencia de valores en la columna: {columna_barras}')
        plt.xlabel(columna_barras)
        plt.ylabel('Frecuencia')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('grafico_barras.png')
        plt.close()

        print("Gráficos generados: 'grafico_dispersión.png' y 'grafico_barras.png'")

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

