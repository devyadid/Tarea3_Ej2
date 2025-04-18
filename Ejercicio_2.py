# animales.py

from datetime import datetime

class Animal:
    """
    Clase base para cualquier animal.
    Método hacer_sonido() devuelve un sonido genérico.
    """
    def hacer_sonido(self):
        return "Sonido de animal"


class Perro(Animal):
    """
    Subclase de Animal que representa un perro.
    Sobrescribe hacer_sonido() para devolver "Guau".
    """
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    """
    Subclase de Animal que representa un gato.
    Sobrescribe hacer_sonido() para devolver "Miau".
    """
    def hacer_sonido(self):
        return "Miau"


if __name__ == "__main__":
    # Fecha y hora para tu captura de pantalla
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Ejecución realizada el: {ahora}\n")
    
    # Creamos instancias de cada animal y mostramos su sonido
    animales = [Animal(), Perro(), Gato()]
    nombres = ["Animal genérico", "Perro", "Gato"]
    
    for nombre, instancia in zip(nombres, animales):
        print(f"{nombre}: {instancia.hacer_sonido()}")
