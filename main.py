from cliente import nuevocliente
from cliente import listarcliente
from cliente import eliminarcliente
from cliente import buscarcliente
#from producto import modificarcliente
from producto import nuevoproducto
from producto import listarproducto
from producto import eliminarproducto
from producto import buscarproducto
#from producto import modificarproducto
from comprobante import emitircomprobante
from comprobante import listarfactura
from comprobante import eliminarfactura
from comprobante import buscarfactura
#dddddddddddddddddddddddddddddddddddd
#from admin import generar_data


#from producto import elimi

# | ǁ ˥ ˩ ˦ ˧ ˨ Ͱ ͱ ‖ ― │ ┌ ┐ └ ┘
def menu_de_opciones():

    continuar: bool = True
    def menu_cliente():
        
        
        print("*****************************************")
        print("***********SISTEMA DE VENTAS*************")
        print("                                         ")
        print("==============MENÚ CLIENTE===============")
        print("***********INGRESE OPCIONES**************")
        print("ǁ                                       ǁ")
        print("ǁ      1) agregar cliente               ǁ")
        print("ǁ      2) listar cliente                ǁ")
        print("ǁ      3) eliminar cliente              ǁ")
        print("ǁ      4) buscar cliente                ǁ")
        #print("ǁ      4) modificar cliente             ǁ")
        print("ǁ      5)    <------                    ǁ")
        print("ǁ                                       ǁ")        
        print("*****************************************")
            

        caso:str = str(input("     --> "))

        match caso :
            case "1":
                nuevocliente.__init__()
            case "2":
                listarcliente.__init__()
            case "3":
                eliminarcliente.__init__()
            case "4":
                buscarcliente.__init__()
            case "5":
                menu_de_opciones()

    def menu_producto():
        

        print("*****************************************")
        print("ǁ**********SISTEMA DE VENTAS************ǁ")
        print("ǁ                                       ǁ")
        print("ǁ============MENÚ PRODUCTO==============ǁ")
        print("ǁ**********INGRESE OPCIONES*************ǁ")
        print("ǁ                                       ǁ")
        print("ǁ      1) nuevo producto                ǁ")
        print("ǁ      2) listar producto               ǁ")
        print("ǁ      3) eliminar producto             ǁ")
        print("ǁ      4) buscar producto               ǁ")
        #print("ǁ      5) modificar producto            ǁ")
        print("ǁ      5)    <------                    ǁ")
        print("ǁ                                       ǁ")        
        print("ǁ***************************************ǁ")

        caso:str = str(input("-->"))

        match caso :
            case "1":
                nuevoproducto.__init__()
            case "2":
                listarproducto.__init__()
            case "3":
                eliminarproducto.__init__()
            case "4":
                buscarproducto.__init__()
            #case "5":
                #modificarproducto.__init__()
            case "5":
                menu_de_opciones()

    def menu_comprobante():
        def comprobante():
            print("*****************************************")
            print("ǁ**********SISTEMA DE VENTAS************ǁ")
            print("ǁ                                       ǁ")
            print("ǁ============MENÚ PRODUCTO==============ǁ")
            print("ǁ**********INGRESE OPCIONES*************ǁ")
            print("ǁ                                       ǁ")
            print("ǁ      1) factura                       ǁ")
            #print("ǁ      2) Boleta                        ǁ")
            print("ǁ      2)    <------                    ǁ")
            print("ǁ                                       ǁ")        
            print("ǁ***************************************ǁ")

            caso:str = str(input("-->"))

            match caso :
                case "1":
                    emitircomprobante.factura()
                #case "2":
                    #emitircomprobante.factura()
                case "2":
                    menu_de_opciones()
        print("*****************************************")
        print("ǁ**********SISTEMA DE VENTAS************ǁ")
        print("ǁ                                       ǁ")
        print("ǁ=============MENÚ VENTA================ǁ")
        print("ǁ**********INGRESE OPCIONES*************ǁ")
        print("ǁ                                       ǁ")
        print("ǁ      1) nuevo venta                   ǁ")
        print("ǁ      2) listar venta                  ǁ")
        print("ǁ      3) eliminar venta                ǁ")
        print("ǁ      4) buscar venta                  ǁ")
        #print("ǁ      4) modificar venta               ǁ")
        print("ǁ      5)    <------                    ǁ")
        print("ǁ                                       ǁ")        
        print("ǁ***************************************ǁ")
            

        caso:str = str(input("-->"))

        match caso :
            case "1":
                comprobante()
            case "2":
                listarfactura.__init__()
            case "3":
                eliminarfactura.__init__()
            case "4":
                buscarfactura.__init__()
            case "5":
                menu_de_opciones()


    while continuar:
        print("*****************************************")
        print("***********SISTEMA DE VENTAS*************")
        print("                                         ")
        print("===================MENÚ==================")
        print("**************INGRESE OPCIONES***********")
        print("ǁ                                       ǁ")
        print("ǁ      1) CLIENTE                       ǁ")
        print("ǁ      2) PRODUCTO                      ǁ")
        print("ǁ      3) COMPROBANTE                   ǁ")
        print("ǁ      4) salir                         ǁ")
        print("ǁ                                       ǁ")        
        print("*****************************************")

        caso:str = str(input("-->"))

        match caso :
            case  "1":
                menu_cliente()
            case  "2":
                menu_producto()
            case  "3":
                print("")
                menu_comprobante()
            case  "4":
                continuar = False
            #case  "system.admin.datagenerate.cliente":
                #generar_data()

menu_de_opciones()
