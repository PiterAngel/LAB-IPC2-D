

def menu():
    print("=== calculadora === ")
    print("1. sumar dos números ")
    print("2. restar dos números ")
    print("3. multiplicar dos números ")
    print("4. dividir dos números ")
    print("5. salir ")


def obtener_numeros():
    while True:
        try:
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))
            return numero1, numero2
        except ValueError:
            print("Entrada inválida, porfavor ingrese solo números")


def main():
    print("Bienvenidos a mi calculadora :)")
    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            numero1, numero2 = obtener_numeros()
            resultado = numero1 + numero2
            print("El resultado de la suma es: ", resultado)
            print(f"El resultado de la suma es: {resultado}")

        elif opcion == "2":
            numero1, numero2 = obtener_numeros()
            resultado = numero1 - numero2
            print("El resultado de la resta es: ", resultado)
            print(f"El resultado de la resta es: {resultado}")
        

        elif opcion == "3":
            numero1, numero2 = obtener_numeros()
            resultado = numero1 * numero2
            print("El resultado de la multiplicacion es: ", resultado)
            print(f"El resultado de la multiplicacion es: {resultado}")

        elif opcion == "4":
            numero1, numero2 = obtener_numeros()
            if numero2 != 0:
                resultado = numero1 / numero2
                print("El resultado de la division es: ", resultado)
                print(f"El resultado de la division es: {resultado}")
            else: 
                print("Error, no se puede dividir entre 0 :(")

        elif opcion == "5":
            print("Adios, gracias por su atención :)")
            break

        else:
            print("Opcion no válida :c")

if __name__ == "__main__":
    main()