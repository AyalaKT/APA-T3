"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Eric Ayala

    Pruebas

    >>> Vector([1, 2, 3]) * 2
    Vector([2, 4, 6])

    >>> 2 * Vector([1, 2, 3])
    Vector([2, 4, 6])

    >>> Vector([1, 2, 3]) * Vector([4, 5, 6])
    Vector([4, 10, 18])

    >>> Vector([1, 2, 3]) @ Vector([4, 5, 6])
    32

    >>> Vector([2, 1, 2]) // Vector([0.5, 1, 0.5])
    Vector([1.0, 2.0, 1.0])

    >>> Vector([2, 1, 2]) % Vector([0.5, 1, 0.5])
    Vector([1.0, -1.0, 1.0])

    >>> Vector([1, 0, 0]) @ Vector([0, 1, 0])
    0

    >>> Vector([5, 5, 5]) - 2
    Vector([3, 3, 3])
"""

class Vector:
    """
    Clase para representar y operar con vectores básicos.
    """

    def __init__(self, componentes):
        """
        Constructor que recibe un iterable con las componentes del vector.
        """
        self.valores = list(componentes)

    def __repr__(self):
        """
        Representación oficial del vector (útil para debugging).
        """
        return f"Vector({repr(self.valores)})"

    def __str__(self):
        """
        Representación legible del vector.
        """
        return str(self.valores)

    def __getitem__(self, indice):
        return self.valores[indice]

    def __setitem__(self, indice, valor):
        self.valores[indice] = valor

    def __len__(self):
        return len(self.valores)

    def __add__(self, otro):
        """
        Suma del vector con una constante o con otro vector.
        """
        if isinstance(otro, (int, float, complex)):
            return Vector(valor + otro for valor in self)
        else:
            return Vector(a + b for a, b in zip(self, otro))

    __radd__ = __add__

    def __neg__(self):
        return Vector(-valor for valor in self)

    def __sub__(self, otro):
        return -(-self + otro)

    def __rsub__(self, otro):
        return -self + otro

    def __mul__(self, otro):
        """
        Producto por escalar o producto componente a componente.
        """
        if isinstance(otro, (int, float, complex)):
            return Vector(valor * otro for valor in self)
        else:
            return Vector(a * b for a, b in zip(self, otro))

    __rmul__ = __mul__

    def __matmul__(self, otro):
        """
        Producto escalar de dos vectores.
        """
        return sum(a * b for a, b in zip(self, otro))

    __rmatmul__ = __matmul__

    def __floordiv__(self, otro):
        """
        Componente paralela (proyección tangencial) del vector.
        """
        coef = (self @ otro) / (otro @ otro)
        return coef * otro

    def __rfloordiv__(self, otro):
        coef = (otro @ self) / (self @ self)
        return coef * self

    def __mod__(self, otro):
        """
        Componente perpendicular del vector (proyección normal).
        """
        return self - (self // otro)

    def __rmod__(self, otro):
        return otro - (otro // self)


# --- Pruebas automáticas con doctest ---
import doctest

if __name__ == "__main__":
    doctest.testmod(verbose=True)

