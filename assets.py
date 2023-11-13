import reads
num_gate = 2
in_gate = False #Inicialmente la puerta está cerrada

def access():
    dni = input("Ingrese su DNI: ")
    reserve = reads.dni_read(dni)
    gate = reserve[1]
    
    if reserve == [0, 0] and not reads.search(dni):
        print("El DNI no está en la base de datos")
        print("Ingrese un DNI que sí esté en la base de datos")
        return access()
    elif reserve == [0, 0] and reads.search(dni):
        _action = input('Ingresa s o n para definir si quieres reservar ahora: ')
        if _action == 's':
            access_val = reads.reservation_now()[1]
            gate = reads.reservation_now()[0]
            if gate == 0:
                print('No hay puerta disponible')
            else:
                print(f"Abriendo la cancha {gate}")
                return [access_val, gate]
        else:
            print('Ha elegido no reservar')
            print('Iniciando el programa...')
            return [0, 0]
    else:
        access_val = reserve[0]
    
    print(f"Abriendo la cancha {gate}")
    return [access_val, gate]


def save():
    return save