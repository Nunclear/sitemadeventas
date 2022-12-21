from producto import buscarproducto
from cliente import buscarcliente
import datetime
import csv

def numero_serie(archivo):
    # Abrir el archivo CSV 
    with open(archivo, 'r') as file:
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
        serie = str(f"F00{serie+1}")        
        #print(serie)
        #serie:list = []
        #serie.append(generar)

    return serie

def Eliminar_Vacias(archivo):
        with open(archivo, 'r') as fichero:
            lines = fichero.readlines()
        with open(archivo, 'w') as fichero:
            for line in lines:
                if line.strip():  # Elimina línea vacía
                    fichero.write(line)
#comprobante = [[],[],[]]


class emitircomprobante():

    def factura():
        #serie = numero_serie('factura.csv')
        #serie += 1
        #serie = str(f"F00{serie+1}")
        factura:tuple
        factura = emitircomprobante.comprobante()
        with open('factura.csv', 'a') as File:
            writer = csv.writer(File)
            writer.writerow(factura)
        Eliminar_Vacias("factura.csv")
        print ("\nEl la factura se ha registrado correctamente")
        

    def comprador():
        #comprador = []
        cliente = buscarcliente.__init__()
        #comprador.append(cliente[0])
        #comprador.append(cliente[1])
        #comprador.append(cliente[2])
        #comprador.append(cliente[3])
        #comprador.append(cliente[4])
        return cliente #comprador

    def productos():
        productos = []
        compra = []
        salir=False
        agregar = "+"
        while salir==False:
            
            if agregar=="+":
                producto:list = []
                productos:list = []
                #compra:list = []
                producto = buscarproducto.__init__()
                cantidad = str(input("cantidad :"))
                #productos:list = [cantidad,producto[0],producto[1],producto[2],producto[3]]
                productos.append(cantidad)
                productos.append(producto[0])
                productos.append(producto[1])
                productos.append(producto[2])
                productos.append(producto[3])
                compra.append(productos)
                agregar = str(input(" (+)agregar    (-)lista completa"))
            else:
                salir=True
        #contador = len(compra)
        #print(contador)
        #print(compra)
        return compra


    def fechasistema():
        fecha : list = []
        ahora = datetime.datetime.now()
        time =str(ahora.strftime("%d/%m/%Y")) 
        fecha.append(time)
        #print(fecha)
        return fecha

    def comprobante():
        #comprobante:tuple 
        cliente = emitircomprobante.comprador()
        compra = emitircomprobante.productos()
        fecha = emitircomprobante.fechasistema()
        serie = numero_serie('factura.csv')
        comprobante:list = [serie,cliente,compra,fecha]
        print(comprobante)
        return comprobante
        #comprobante.append(serie)
        #comprobante.append(cliente)
        #comprobante.append(compra)
        #comprobante.append(fecha)
        #comprobante.append(comprador(),productos)

    #comprobante = [[cliente[]],[producto[]],[fecha[]]]
    #comprobante[0] = cl

        #comprobante = []
        #comprador = []
        #productos = []


    #comprobante.append(comprador,productos,fecha)
        #comprobante = comprador,productos,fecha

class buscarfactura():

    

    def buscarDatos1(archivo, dato1):
        with open(archivo, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[0] == dato1:
                    return row
    def buscarDatos2(archivo, dato1, dato2):
        with open(archivo, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[1][2] == dato1 and row[-1] == dato2:
                    return row
    def __init__():
        #dato1 = input("Ingrese el primer dato que desea buscar en el archivo: ")
        #dato2 = input("Ingrese el segundo dato que desea buscar en el archivo: ")

        print("===========================================")
        print("ǁ datos para buscar (minimo 2 parametros) ǁ")
        print("ǁ=========================================ǁ")
        print("ǁ                                         ǁ")
        print("ǁ       1) serie de factura               ǁ")
        print("ǁ       2) dni y fecha                    ǁ")
        #print("ǁ       3) dni del cliente                ǁ")
        #print("ǁ       4) ruc de cliente                 ǁ")
        print("===========================================")
        parametro1 = str(input("ǁparametro         :"))
        match parametro1 :
            case "1":  
                dato1= str(input("ǁSERIE DE FACTURA:      "))
                #buscarfactura.buscarDatos1("factura.csv",dato1)
                resultado = buscarfactura.buscarDatos1('factura.csv', dato1,)
            case "2":
                dato1 = str(input("ǁDNI:        "))
                dato2 = str(input("ǁFECHA:      "))
                #buscarfactura.buscarDatos2("factura.csv",dato1,dato2)
                resultado = buscarfactura.buscarDatos2('factura.csv', dato1, dato2)
        if resultado is None:
            buscarfactura.__init__()
        else:
            print(resultado)
        return resultado

class listarfactura():
    def __init__():
        Eliminar_Vacias("factura.csv")
        print ("\nLISTA DE FACTURAS EMITIDAS")
        print ("==============================")
        with open('factura.csv') as File:  
            reader = csv.reader(File)
            for row in reader:
                print (row)

class eliminarfactura():
    def __init__():
        Eliminar_Vacias("factura.csv")
        listarfactura.__init__()
        eliminar:int = int(input('Ingrese el número de comprobante a eliminar: '))
        # abrir el archivo csv
        with open('factura.csv', 'r') as csv_file:
            # leer el archivo csv
            csv_reader = csv.reader(csv_file)
            # guardar los datos leidos en una lista
            datos = list(csv_reader)

        # eliminar la fila deseada
        datos.remove(datos[eliminar-1])

        # escribir el archivo csv con la fila eliminada
        with open('factura.csv', 'w') as csv_file:
            # escribir el archivo csv
            csv_writer = csv.writer(csv_file)
            # escribir las filas en el archivo csv
            csv_writer.writerows(datos)
        Eliminar_Vacias("factura.csv")
#eliminarfactura.__init__()
#listarfactura.__init__()
#print(comprobante)

