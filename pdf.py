#import pdfkit
"""from comprobante import buscarfactura

datos = buscarfactura.__init__()
cliente: list = []
#datos[1] = datos[1][1:-1]
datos_cliente:list
datos_cliente = datos[2]
nombrecliente = datos_cliente[0]
#print( datos)
#serie = datos[0][0]
#nombre = datos[1][0]
#pellido = datos[1][1]
#cliente = nombre,apellido  #str(f"{datos[1][0]} {datos[1][1]}")
#serie = datos[0]
print("--------------------------------------")

print(datos_cliente)
print(nombrecliente)
#print("dddd",nombre)
"""""
import fpdf 

# creamos la clase de factura 
class Factura:
    # definimos el constructor de la clase 
    def __init__(self, cliente, numero_de_factura, fecha, monto, productos):
        self.cliente = cliente
        self.numero_de_factura = numero_de_factura
        self.fecha = fecha
        self.monto = monto
        self.productos = productos
 
    # definimos la funcion para crear la factura
    def crearFactura(self):
        
        # creamos el documento pdf
        pdf = fpdf.FPDF()
        # creamos una pagina
        pdf.add_page()
        # definimos el tamano de la fuente
        pdf.set_font("Arial", size = 12)
        # agregamos el titulo
        pdf.cell(200, 10, txt = "Factura", ln = 1, align = "C")
        # agregamos los datos del cliente
        pdf.cell(200, 10, txt = "Cliente: " + self.cliente, ln = 1, align = "L")
        pdf.cell(200, 10, txt = "Numero de factura: " + self.numero_de_factura, ln = 1, align = "L")
        pdf.cell(200, 10, txt = "Fecha: " + self.fecha, ln = 1, align = "L")
        
        # agregamos los productos a la factura
        pdf.cell(200, 10, txt = "Productos: ", ln = 1, align = "C")
        # iteramos sobre la lista de productos
        for producto in self.productos:
            # agregamos los productos a la factura
            pdf.cell(200, 10, txt = producto, ln = 1, align = "L")
        
        # agregamos el monto a la factura
        pdf.cell(200, 10, txt = "Monto: " + str(self.monto), ln = 1, align = "L")
        # guardamos el documento
        pdf.output("factura.pdf")

# creamos una instancia de Factura
factura = Factura("Juan Perez", "12345", "07/01/2020", 100.0, ["Producto 1", "Producto 2"])
# creamos la factura
factura.crearFactura()