from Punto import Punto
from Rectangulo import Rectangulo

if __name__ == "__main__":
    # Crear los puntos A(2, 3), B(5, 5), C(-3, -1) y D(0, 0)
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    # Imprimir los puntos
    print("Puntos:")
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print(f"D: {D}")

    # Consultar a qué cuadrante pertenecen los puntos A, C y D
    print("\nCuadrantes:")
    print(f"A pertenece al cuadrante: {A.cuadrante()}")
    print(f"C pertenece al cuadrante: {C.cuadrante()}")
    print(f"D pertenece al cuadrante: {D.cuadrante()}")

    # Consultar los vectores AB y BA
    print("\nVectores:")
    print(f"Vector AB: {A.vector(B)}")
    print(f"Vector BA: {B.vector(A)}")

    # Consultar la distancia entre los puntos 'A y B' y 'B y A'
    print("\nDistancias:")
    print(f"Distancia entre A y B: {A.distancia(B):.3f}")
    print(f"Distancia entre B y A: {B.distancia(A):.3f}")
    

    # Determinar cuál de los puntos A, B o C está más lejos del origen
    print("\nPunto más lejano del origen:")
    distancias = {
        "A": A.distancia(D),
        "B": B.distancia(D),
        "C": C.distancia(D)
    }
    punto_mas_lejano = max(distancias, key=distancias.get) # Obtiene la clave con el mayor valor
    print(f"El punto más lejano del origen es: {punto_mas_lejano}")

    # Crear un rectángulo utilizando los puntos A y B
    rectangulo = Rectangulo(A, B)

    # Consultar la base, altura y área del rectángulo
    print("\nRectángulo:")
    print(f"Base: {rectangulo.base()}")
    print(f"Altura: {rectangulo.altura()}")
    print(f"Área: {rectangulo.area()}")
    