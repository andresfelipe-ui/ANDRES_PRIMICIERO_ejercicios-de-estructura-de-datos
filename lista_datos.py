class lista_numeros:
    def _init_(self):
        self.lista_numero=[]
        
    def guardar_numero(self, dato_numero):
        self.lista_numero.append(dato_numero)
        print(self.lista_numero)
    
    def incluir_lista(self, dato_numero):
        self.lista_numero.extend(dato_numero) 
        print(self.lista_numero)
    
    def insertar_dato(self, posicion, dato):
        self.lista_numero.insert(posicion, dato)
        print(self.lista_numero)
        
    def eliminar_dato(self):
      pass
    
    def ver_numero(self):
       pass