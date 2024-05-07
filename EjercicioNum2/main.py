def usuario():

    identificacion = None
    while identificacion is None:
        try:
            identificacion =int(input("Ingrese la identificacion del usuario:"))
        except ValueError:
            print("ingrese datos .. volviendo al inicio")
            return usuario()
        else:
            continue
    nombres = None
    while nombres is None:
        try:
            nombres =str(input("Ingrese los nombres del usuario: "))
        except ValueError:
            print("ingrese datos .. volviendo al inicio")
            return usuario()
        else:
            continue
    apellidos = None
    while apellidos is None:
        try:
            apellidos =str(input("Ingrese los apellidos del usuario: "))
        except ValueError:
            print("ingrese datos .. volviendo al inicio")
            return usuario()
        else:
            continue
    
    direccion = None
    while direccion is None:
        try:
            direccion =str(input("Ingrese la direccion del usuario: "))
        except ValueError:
            print("ingrese datos .. volviendo al inicio")
            return usuario()
        else:
            continue
    ciudad = None
    while ciudad is None:
        try:
            ciudad =str(input("Ingrese la ciudad del usuario: "))
        except ValueError:
            print("ingrese datos .. volviendo al inicio")
            return usuario()
        else:
            continue
    longitud = None
    while longitud is None:
        try:
            longitud =(input("Ingrese la longitud de la ubicacion del usuario:"))
        except ValueError:
            print("ingrese datos .. volviendo al inicio")
            return usuario()
        else:
            continue
    latitud = None
    while latitud is None:
        try:
            latitud =bool(input("Ingrese la latitud de la ubicacion del del usuario:"))
        except ValueError:
            print("ingrese datos .. volviendo al inicio")
            return usuario()
        else:
            continue
    email = None
    while email is None:
        try:
            email =input("Ingrese el correo del usuario: ")
        except ValueError:
            print("ingrese datos .. volviendo al inicio")
            return usuario()
        else:
            continue
    edad = None
    while edad is None:
        try:
            edad =input("Ingrese la edad del usuario:")
        except ValueError:
            print("ingrese datos .. volviendo al inicio")
            return usuario()
        else:
            continue
    ocupacion = None
    while ocupacion is None:
        try:
            ocupacion=input("Ingrese la ocupacion del usuario:")
        except ValueError:
            print("ingrese datos .. volviendo al inicio")
            return usuario()
        else:
            continue

    usuariodatos = {
        'identificacion': {
            'identificacion': identificacion,
            'nombres': nombres,
            'apellidos': apellidos,
            'ubicacion': {
                'direccion':direccion,
                'ciudad':ciudad,
                'longitud':longitud,
                'latitud': latitud
                },
            'email':email,
            'edad':edad,
            'ocupacion':ocupacion
        }
    }
    print("Los Resultados de los datos ingresados son: ")
    print(usuariodatos)


if __name__ == '__main__':
    usuario()