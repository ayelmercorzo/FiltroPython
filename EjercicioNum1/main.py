import os

def numero():
    os.system('cls')
    try:
        dato_a_convertir = int(input("Ingrese la cantidad a convertir (sin puntos ni comas): "))
    except ValueError:
        print("ingrese un numero siguiendo las especificaciones.")
        os.system('pause')
        return numero()
    convert = "1.Yenes \n2.Dolares\n3.Euro"

    _yen = 26.30
    _dolar = 3.944
    _euro = 4.279

    try:
        print(convert)
        op = int(input("Opcion: "))
        if (op !=4):
            match op:
                case 1:
                    resultado_yen = _yen * dato_a_convertir 
                    print("Y$",resultado_yen)
                case 2:
                    resultado_dolar = _dolar * dato_a_convertir 
                    print ("$",resultado_dolar)
                case 3:
                    resultado_euro = _euro * dato_a_convertir 
                    print("E$",resultado_euro)
        
    except ValueError:
        print("Introduzca un numero valido.")
        os.system('pause')
        return numero()

if __name__ == '__main__':
      numero()