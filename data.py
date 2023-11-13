data = {
    '70398195': {'Usuario': 'Sofía Bobadilla', 'Reserva': 1, 'Gate': 1, 'time': '8:00pm', 'day': '10/11/2023'},
    '72832947': {'Usuario': 'Carlos Oliva', 'Reserva': 0, 'Gate': 0, 'time': '8:00pm', 'day': '10/11/2023'},
    '72345135': {'Usuario': 'Hola Mundo', 'Reserva': 1, 'Gate': 2, 'time': '9:00pm', 'day': '11/11/2023'}
}

times = {
    '10/11/2023': {
        '8:00pm': [{'gate': 1, 'reserva': 0}, {'gate': 2, 'reserva': 1}],
        '9:00pm': [{'gate': 1, 'reserva': 0}, {'gate': 2, 'reserva': 1}]
    },
    '11/11/2023': {
        '8:00pm': [{'gate': 1, 'reserva': 1}, {'gate': 2, 'reserva': 0}],
        '9:00pm': [{'gate': 1, 'reserva': 0}, {'gate': 2, 'reserva': 1}]
    }
}
