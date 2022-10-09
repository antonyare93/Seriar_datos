import pickle

class Vehiculo():
    color = 'Negro'
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 180
    cilindrara = 2000

def main():   

    global mazda
    mazda = Coche()
    mazda.color = 'Blanco'

    with open('datos.bin', 'wb') as f:
        pickle.dump(mazda, f)

    with open('datos.bin', 'rb') as f:
        pickle.load(f)

    print(f'Color: {mazda.color}')
    print(f'Ruedas: {mazda.ruedas}')
    print(f'Puertas: {mazda.puertas}')
    print(f'Velocidad: {mazda.velocidad}')
    print(f'Cilindrada: {mazda.cilindrara}')

if __name__ == '__main__':
    main()