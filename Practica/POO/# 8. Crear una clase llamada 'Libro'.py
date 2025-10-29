# 8. Crear una clase llamada 'Libro' que tenga atributos para el título, el autor y el año de publicación. Implementar un método que devuelva una descripción completa del libro.
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def descripcion(self):
        return f"'{self.titulo}' de {self.autor} ({self.anio})"

# Ejemplo
libro = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
print(libro.descripcion())
