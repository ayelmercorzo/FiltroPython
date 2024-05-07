import main as m
import movimientosJson as moves
import os

def ingresoDatos():
    os.system('cls')
    horaExtra = 5500
    try:
        try:
            identificacion=int(input("Ingrese el numero de identificacion de empleados: "))
        except ValueError:
            return ingresoDatos()
        nombre = str(input("Ingrese el nombre del empleado: "))
        print("----Seleccione un cargo para el empleado-----")
        print("1. Almacenista \n2. Jefe IT \n3. Administrador \n4. Mensajero \n5. Gerente")
        cargo = str(input("Ingrese el cargo segun las opciones: "))
        try:
            salario = int(input("Ingrese el salario del empleado: "))
        except ValueError:
            return ingresoDatos()
        try:
            diasTrabajados = int(input("Cuantos dias trabajo el empleado: "))
        except ValueError:
            return ingresoDatos()
        horasExtras = str(input("Si el Empleado tuvo horas extras. ¿cuantas horas?"))
        valorDia = str(input("Cuanto vale el dia laboral: "))
        descuentoxCafeteria = str(input("Descuento "))
        cuotaPrestamo = str(input("CuotaPrestamo"))
        mesPagado  = str(input("Mes al que se paga"))
        fechaPago = str(input(""))
        sueldoBase = str(input(""))
        valorTotalHrasExtras = str(input(""))
        totalAPagar = str(input(""))
    except AttributeError:
        return ingresoDatos()  
     
    empleado = {
        'identificacion': identificacion,
        'nombre': nombre,
        'cargo': cargo,
        'salario':salario,
        'horas Trabajadas':{
            'diasTrabajados':diasTrabajados,
            'horas extras':horasExtras,
        },
        'Descuento': descuentoxCafeteria,
        'valorDia':valorDia,
        'Cuota Prestamo': cuotaPrestamo,
        'hora extra': horaExtra,
        'mesPagado':mesPagado,
        'fechaPago': fechaPago,
        'sueldoBase': sueldoBase,
        'valorTotalHrasExtras': valorTotalHrasExtras,
        'totalAPagar':totalAPagar,
    }

    moves.aggdataTrabajadores('dataTrabajadores',identificacion,empleado)
    print("empleado registrado!!")
def mainMenu():
    os.system('cls')
    titulo = """
    *************************
    *      Bienvenido       *
    *************************"""
    opciones = "1.Entrar Como Gerente \n2.Entrar Como Empleado. \n3.Ingresar Nuevo Empleado \n4.Salir"
    print(titulo)
    print(opciones)

    try:
        op = int(input("Ingrese Una Opcion: "))
    except ValueError:
        return mainMenu()
    if op == 1:
        menuGerente()
    if op == 2:
        consultarPagoDeterminadoEmpleado()
    if op == 3:
        ingresoDatos()
    if op == 4:
        os.system('exit')

def menuEmpleado():
    pass

def menuGerente():
    os.system('cls')
    titulo = """
    *************************
    *       Bienvenido      *
    *        Gerente        *
    *************************"""
    opciones = "\n1.Total pagado por concepto de nomina \n2.Consultar la colilla de pago de un determinado empleado. \n3.salir"
    print(titulo)
    print(opciones)

    try:
        op = int(input(""))
    except ValueError:
        return menuGerente()
    if op == 1:
        totalPagadoPorNomina()
    if op == 2:
        consultarPagoDeterminadoEmpleado()
    if op == 3:
        mainMenu()

def totalPagadoPorNomina():
    moves.leerDatos()


def consultarPagoDeterminadoEmpleado():
    moves.leerDatos()

#no alcance :(