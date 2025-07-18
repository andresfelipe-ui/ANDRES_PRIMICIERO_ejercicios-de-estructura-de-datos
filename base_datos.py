class BaseDatos:
    def __init__(self):
        self.tupla_pares = ()
        self.tupla_impares = ()

    def crear_tupla_pares(self, lista):
        pares = [num for num in lista if isinstance(num, (int, float)) and num % 2 == 0]
        self.tupla_pares = tuple(pares)
        print(f"Tupla pares creada: {self.tupla_pares}")

    def crear_tupla_impares(self, lista):
        impares = [num for num in lista if isinstance(num, (int, float)) and num % 2 != 0]
        self.tupla_impares = tuple(impares)
        print(f"Tupla impares creada: {self.tupla_impares}")

    def ver_tupla(self, lista, tipo):
        if tipo == "par":
            tupla = tuple(n for n in lista if isinstance(n, (int, float)) and n % 2 == 0)
            print(f"Tupla de pares: {tupla}")
        elif tipo == "impar":
            tupla = tuple(n for n in lista if isinstance(n, (int, float)) and n % 2 != 0)
            print(f"Tupla de impares: {tupla}")
        else:
            print("Tipo inválido.")

            print("Índice fuera de rango.")
            
    def modificar_valor_lista(self):
        lista = self.objlista.ver_numero()
        print(f"Lista actual: {lista}")

        entrada = input("Índice a modificar: ").strip()

        try:
            valor_float = float(entrada)
            if valor_float.is_integer():
                indice = int(valor_float)
            else:
                print("Error: El índice debe ser un número entero sin decimales.")
                return
        except ValueError:
            print("Error: Entrada no es un número válido.")
            return

        if indice < 0 or indice >= len(lista):
            print("Índice fuera de rango.")
            return

        try:
            nuevo_valor = float(input("Nuevo valor: "))
        except ValueError:
            print("Error: Debes ingresar un número válido.")
            return

        lista[indice] = nuevo_valor
        print(f"Lista actualizada: {lista}")

def eliminar_valor(self, tipo, valor):
        if tipo == "par":
            lista = list(self.tupla_pares)
        elif tipo == "impar":
            lista = list(self.tupla_impares)
        else:
            print("Tipo inválido")
            return

        if valor in lista:
            lista.remove(valor)
            if tipo == "par":
                self.tupla_pares = tuple(lista)
            else:
                self.tupla_impares = tuple(lista)
            print(f"Valor {valor} eliminado de la tupla {tipo}.")
        else:
            print(f"Valor {valor} no encontrado en la tupla {tipo}.")
