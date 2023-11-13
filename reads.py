from data import data, times

def search(dni):
    return dni in data

def val_dnitype(dni):
    if len(dni) == 8:
        return search(dni)
    else:
        print("El DNI es incorrecto")
        return False

def reserved_gate(dni):
    user_data = data.get(dni, {})
    return user_data.get('Gate', 0)

def have_permission(dni):
    user_data = data.get(dni, {})
    return user_data.get('Reserva', 0)

def day_():
    return '10/11/2023'

def time_():
    return '9:00pm'

def val_gate(day, time):
    time_data = times.get(day, {}).get(time, [])
    for gate_info in time_data:
        if gate_info['reserva'] == 0:
            return gate_info['gate']
    return 0

def available_gate():
    _day = day_()
    _time = time_()
    return val_gate(_day, _time)

def dni_read(dni):
    print("Leyendo DNI...")
    val_access = val_dnitype(dni)
    if val_access:
        gate = reserved_gate(dni)
        access = have_permission(dni)
        return [access, gate]
    else:
        print("Usted no tiene acceso")
        return [0, 0]

def reservation_now():
    ava_g = available_gate()
    if ava_g == 0:
        print('No hay puerta disponible')
        return [0, 0]
    else:
        return [ava_g, 1]

