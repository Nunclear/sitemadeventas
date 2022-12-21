import csv

def Eliminar_Vacias(archivo):
        with open(archivo, 'r') as fichero:
            lines = fichero.readlines()
        with open(archivo, 'w') as fichero:
            for line in lines:
                if line.strip():  # Elimina línea vacía
                    fichero.write(line)
class nuevoproducto():
    def __init__():
        Eliminar_Vacias("producto.csv")
        print ("REGISTRO DE NUEVO PRODUCTO")
        print ("==========================")
        serie = nuevoproducto.numero_serie()
        print            (f"numero de serie: {serie}")
        nombre = input   ("NOMBRE:          ")
        descripcion=input("DESCRIPCION:     ")
        precio=input     ("PRECIO:          ")
        cliente = serie,nombre,descripcion,precio
        with open('producto.csv', 'a') as File:
            writer = csv.writer(File)
            writer.writerow(cliente)
        print ("\nEl producto se ha registrado correctamente")
        #Eliminar_Vacias("producto.csv")

    def numero_serie():
    # Abrir el archivo CSV 
        with open('producto.csv', 'r') as file:
        # leer el archivo csv 
            reader = csv.reader(file)
            # obtener todas las filas del archivo
            filas = list(reader)
            # obtener la última fila 
            ultima_fila = filas[-1]
            # imprimir el primer valor de la última fila
            #print(ultima_fila[0])
            serie = ultima_fila[0]
            serie = serie[-1]
            serie = int(serie)
            #print(serie+1)
            serie = str(f"A00{serie+1}")
            #print(serie)
        return serie

class listarproducto():
    def __init__():
        Eliminar_Vacias("producto.csv")
        print ("\nLISTADO DE PRODUCTOS")
        print ("===================")
        with open('producto.csv') as File:  
            reader = csv.reader(File)
            for row in reader:
                print (row)
                
class eliminarproducto():
    def __init__():
        Eliminar_Vacias("producto.csv")
        listarproducto.__init__()
        eliminar:int = int(input('Ingrese el número de comprobante a eliminar: '))
        # abrir el archivo csv
        with open('producto.csv', 'r') as csv_file:
            # leer el archivo csv
            csv_reader = csv.reader(csv_file)
            # guardar los datos leidos en una lista
            datos = list(csv_reader)

        # eliminar la fila deseada
        datos.remove(datos[eliminar-1])

        # escribir el archivo csv con la fila eliminada
        with open('producto.csv', 'w') as csv_file:
            # escribir el archivo csv
            csv_writer = csv.writer(csv_file)
            # escribir las filas en el archivo csv
            csv_writer.writerows(datos)
        Eliminar_Vacias("producto.csv")
        
    
class buscarproducto():
    def __init__():
        Eliminar_Vacias("producto.csv")
        def buscarDatos(producto, dato1, dato2):
            with open(producto, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if row[1] == dato1 and row[2] == dato2:
                        return row

        dato1 = input("nombre del producto: ")
        dato2 = input("descripcion del producto: ")

        resultado = buscarDatos("producto.csv", dato1, dato2)

        if resultado is None:
            print("No se encontraron los datos especificados")
        else:
            #print(f"Los datos encontrados son {resultado[1]} y {resultado[2]}")
            print(resultado)
        return resultado 
#nuevoproducto.__init__()
"""class modificarproducto():
    def __init__():
        listarproducto()
        eliminarproducto()
        nuevoproducto()
        listarproducto()"""
        
"""class modificarproducto():
    def __init__():
        # Definimos los nombres de los campos  
        # Definimos la función para buscar una fila y sobreescribirla
        def sobreescribir(producto, buscar_fila, nueva_fila):
            # Abrimos el archivo
            with open(producto, 'r') as csv_file:
                # Leemos el archivo
                csv_reader = csv.reader(csv_file)
                # Creamos una lista con los datos leídos
                lista_csv = list(csv_reader)
                # Recorremos la lista
                for fila in lista_csv:
                    # Buscamos la fila
                    if fila[0] == buscar_fila:
                        # Sobreescribimos la fila con los nuevos datos
                        fila[0] = nueva_fila[0]
                        fila[1] = nueva_fila[1]
                        fila[2] = nueva_fila[2]
                        fila[3] = nueva_fila[3]
                # Abrimos el archivo para escribir
                with open(producto, 'w') as csv_file:
                    # Escribimos la lista con los datos sobreescritos
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerows(lista_csv)
        
        # Definimos la fila a buscar
        buscar_fila = str(input("buscar por nombre"))
        serie:int = int(input("serie del producto: A00"))
        descripcion =str(input("descripcion"))
        precio = str(input("precio"))
        # Definimos la nueva fila
        nueva_fila = [serie,buscar_fila, descripcion, precio]
        # Llamamos a la función
        sobreescribir('producto.csv', buscar_fila, nueva_fila)"""