import EntradaDeDatos as menu
import movimientosJson as moves
Trabajadores = 'EjercicioNum4/data/trabajadores.json'
dataTrabajadores = {"dataTrabajadores": {}}


if __name__ == '__main__':
    moves.revisarArchivos(Trabajadores,dataTrabajadores)
    menu.mainMenu()
    