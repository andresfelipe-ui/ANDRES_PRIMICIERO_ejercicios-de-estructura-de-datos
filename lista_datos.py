class ListaNumeros:
    def __init__(self):
        # Inicializa una lista vacía
        self.lista_numero = []

    def guardar_numero(self, dato_numero):
        """
        Agrega un número al final de la lista.
        """
        self.lista_numero.append(dato_numero)
        print(f"[guardar_numero] Lista actual: {self.lista_numero}")

    def incluir_lista(self, datos):
        """
        Agrega múltiples números al final (lista).
        """
        self.lista_numero.extend(datos)
        print(f"[incluir_lista] Lista actual: {self.lista_numero}")

    def insertar_dato(self, posicion, dato):
        """
        Inserta un número en la posición indicada.
        """
        if 0 <= posicion <= len(self.lista_numero):
            self.lista_numero.insert(posicion, dato)
            print(f"[insertar_dato] Lista actual: {self.lista_numero}")
        else:
            print("[insertar_dato] Posición inválida.")

    def eliminar_dato(self, dato):
        """
        Elimina el primer elemento igual a dato, si existe.
        """
        if dato in self.lista_numero:
            self.lista_numero.remove(dato)
            print(f"[eliminar_dato] '{dato}' eliminado. Lista actual: {self.lista_numero}")
        else:
            print(f"[eliminar_dato] '{dato}' no encontrado en la lista.")

    def ver_numero(self):
        """
        Muestra la lista completa.
        """
        print(f"[ver_numero] Lista completa: {self.lista_numero}")
        return self.lista_numero
