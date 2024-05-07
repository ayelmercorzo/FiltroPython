
import json
import os

Tienda = 'EjercicioNum3/data/tienda.json'
tiendaViveres = {"dataViveres": {}}


def revisarArchivos(databaseFile, datachek):
    if os.path.isfile(databaseFile):
        return  
    with open(databaseFile, "w") as file:
        json.dump(datachek, file, indent=4)

def aggdataViveres(*param):
    dataViveres = list(param)
    with open(Tienda, "r+") as rwf:
        dataViveres_file = json.load(rwf)
        if len(param) > 1:
            dataViveres_file[dataViveres[0]].update({dataViveres[0]:dataViveres[1]})
        else:
            dataViveres_file.update({param[0]})
        rwf.seek(0)
        json.dump(dataViveres_file, rwf, indent=4)

def ingresoDatos():
    print("---Ingresar nuevos datos para la tienda---")
    try:
        id = int(input("Ingrese la identificacion del producto: "))
    except ValueError:
            return
    try:
        nombre = str(input("Ingrese el nombre del producto: "))
    except ValueError:
            return
    try:
        valorUnitarioCompra = int(input("Ingrese el de compra: "))
    except ValueError:
            return
    try:
        stockmin = int(input("Ingrese la cantidad(stock) minimo: "))
    except ValueError:
            return
    try:
        stockmax = int(input("Ingrese la cantidad(stock) maxima: "))
    except ValueError:
            return
    try:
        valorUnitarioVenta = int(input("Ingrese el Valor de venta (Sin Puntos Ni comas)"))
    except ValueError:
            return
    Producto = {
            id: {
               'id': id,
               'nombre': nombre,
               'Valor Unitario Compra': valorUnitarioCompra,
               'stock minimo': stockmin,
               'stock maximo': stockmax,
               'Valor Unitario Venta': valorUnitarioVenta,
            }
        }

    aggdataViveres('dataViveres',Producto)
    print("El producto se agrego correctamente.")

if __name__ == '__main__':
    revisarArchivos(Tienda, tiendaViveres)
    ingresoDatos()
    

