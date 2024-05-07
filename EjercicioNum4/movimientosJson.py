import json
import os
import main as main
import EntradaDeDatos as menu

def revisarArchivos(databaseFile, datachek):
    if os.path.isfile(databaseFile):
        return  
    with open(databaseFile, "w") as file:
        json.dump(datachek, file, indent=4)

def aggdataTrabajadores(*param):
    dataViveres = list(param)
    with open(main.Trabajadores, "r+") as rwf:
        dataViveres_file = json.load(rwf)
        if len(param) > 1:
            dataViveres_file[dataViveres[0]].update({dataViveres[0]:dataViveres[1]})
        else:
            dataViveres_file.update({param[0]})
        rwf.seek(0)
        json.dump(dataViveres_file, rwf, indent=4)

def leerDatos():
    with open(main.Trabajadores, "r") as read:
        json.load(read)

