import assets

def main():
    print("main")
    print('Iniciando')
    results = assets.access() #función que enciende el sistema
    assets.save() #función que guarda datos
    #send_to_arduino(results[1])     #Envía a arduino el valor de la puerta

if __name__ == '__main__':
    main()
