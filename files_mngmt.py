# Modos de Apertura

# r -> Solo lectura
# r+ -> Lectura y escritura
# w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# a -> Añadido (agregar contenido). Crea el archivo si éste no existe
# a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

def read():
    numbers = []
    with open("./python-intermedio/archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)

def write():
    names = ["Hola", "a", "todos"]
    with open("./python-intermedio/archivos/names.txt", "w", encoding="utf-8") as f:
        for el in names:
            f.write(el)
            f.write("\n")

def append():
    names = ["Hola", "a", "todos"]
    with open("./python-intermedio/archivos/names.txt", "a", encoding="utf-8") as f:
        for el in names:
            f.write(el)
            f.write("\n")

def run():
    read()
    write()
    append()

if __name__ == '__main__':
    run()