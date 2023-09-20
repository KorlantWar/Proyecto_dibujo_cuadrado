class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def dibujar_cuadrado(self):
        if self.lado <= 0:
            print("El lado del cuadrado debe ser un número positivo.")
            return

        for i in range(self.lado):
            for j in range(self.lado):
                if i == 0 or i == self.lado - 1 or j == 0 or j == self.lado - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()