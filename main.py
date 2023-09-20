from clase import Cuadrado

def main():
    try:
        lado = int(input("Ingrese el número de asteriscos para cada lado del cuadrado: "))
        cuadrado = Cuadrado(lado)
        cuadrado.dibujar_cuadrado()
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()