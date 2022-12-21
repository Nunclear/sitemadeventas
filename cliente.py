import csv
def Eliminar_Vacias(archivo):
        with open(archivo, 'r') as fichero:
            lines = fichero.readlines()
        with open(archivo, 'w') as fichero:
            for line in lines:
                if line.strip():  # Elimina línea vacía
                    fichero.write(line)

class nuevocliente():

    def __init__():
        print         ("     REGISTRO DE NUEVO CLIENTE     ")
        print         ("===================================")
        nombre=input  ("ǁ    NOMBRE:            ")
        apellido=input("ǁ    APELLIDO:          ")
        dni=input     ("ǁ    DNI O RUC:         ")
        direccion=input("ǁ    DIRECCION:         ")
        celular=input ("ǁ    NUMERO DE CELULAR: ")
        #ruc=input     ("ǁ    RUC:               ")
        cliente: list =[]
        #cliente:list = [nombre,apellido,dni,celular,direccion]
        cliente.append(nombre)
        cliente.append(apellido)
        cliente.append(dni)
        cliente.append(celular)
        cliente.append(direccion)

        with open('cliente.csv', 'a') as File:
            writer = csv.writer(File)
            writer.writerow(cliente)
            Eliminar_Vacias("cliente.csv")
        print ("\nEl cliente se ha registrado correctamente")

    
class listarcliente():
    def __init__():
        Eliminar_Vacias("cliente.csv")
        print ("\nLISTADO DE CLIENTES")
        print ("===================")
        with open('cliente.csv') as File:  
            reader = csv.reader(File)
            for row in reader:
                print (row)
        



class eliminarcliente():
    def __init__():
        Eliminar_Vacias("cliente.csv")
        listarcliente.__init__()
        eliminar:int = int(input('Ingrese el número de comprobante a eliminar: '))
        # abrir el archivo csv
        with open('cliente.csv', 'r') as csv_file:
            # leer el archivo csv
            csv_reader = csv.reader(csv_file)
            # guardar los datos leidos en una lista
            datos = list(csv_reader)

        # eliminar la fila deseada
        datos.remove(datos[eliminar-1])

        # escribir el archivo csv con la fila eliminada
        with open('cliente.csv', 'w') as csv_file:
            # escribir el archivo csv
            csv_writer = csv.writer(csv_file)
            # escribir las filas en el archivo csv
            csv_writer.writerows(datos)
        Eliminar_Vacias("cliente.csv")

class buscarcliente():
    def __init__():
        Eliminar_Vacias("cliente.csv")
        def buscarDatos(producto, dato1):
            with open(producto, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if row[2] == dato1:# and row[2] == dato2:
                        return row


        dato1 = input("DNI:      ")
        #dato2 = input("descripcion del producto: ")

        resultado = buscarDatos("cliente.csv", dato1)

        if resultado is None:
            buscarcliente.__init__()
        else:
            #print(f"Los datos encontrados son {resultado[1]} y {resultado[2]}")
            print(resultado)
        return resultado 
"""class modificarcliente():
    def __init__():
        listarcliente.__init__()
        eliminarcliente.__init__()
        nuevocliente.__init__()"""
      
   
    
    
    