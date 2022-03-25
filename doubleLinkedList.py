from math import sqrt


class DoubleLinkedList:
    #Creamos la clase anidada de nodo
    class Node:
        #Creamos el inicializador de nodo
        def __init__ (self, value):
            self.value = value
            self.next_node = None
            self.previuos_node = None
    #Creamos el metodo inicializadopr de double linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 
        
    #Imprimir
    def show_double_linked_list(self):
        array_double_linked_list = []
        current_node = self.head
        while (current_node != None):
            array_double_linked_list.append(current_node.value)
            current_node = current_node.next_node
        print(array_double_linked_list)

    #Añadir en la cabeza
    def add_node_head(self,value):
        new_node = self.Node(value)
        if self.head == None and self.tail == None :
            self.head = new_node
            self.tail = self.head
        else :
            self.head.previuos_node = new_node
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1
    
    #Añadir a la cola       
    def add_node_tail(self,value):
        new_node = self.Node(value)
        if self.head == None and self.tail == None :
            self.head = new_node
            self.tail = self.head
        else :
            self.tail.next_node = new_node
            new_node.previuos_node = self.tail
            self.tail = new_node
        self.length += 1
    
    #Eliminar cabeza        
    def delete_head(self):
        if self.length ==0 :
            self.head = None
            self.tail = None
        elif self.head != None :
            remove_node = self.head
            self.head = remove_node.next_node
            remove_node.next_node = None
            self.head.previous_node = None
            self.length -=1
        print(f' El nodo eliminado es :{remove_node.value}')
    
    #Eliminar cola    
    def delete_tail(self):
        if self.length ==0 :
            self.head = None
            self.tail = None
        elif self.head != None :
            remove_node = self.tail
            new_tail = self.tail.previuos_node
            self.tail.previuos_node = None
            new_tail.next_node = None 
            self.tail = new_tail
            self.length -=1
        print(f' El nodo eliminado es :{remove_node.value}')
    
    #Devolver un nodo por su indice
    def get(self,index):
        if index == self.length-1:
            return self.tail
        elif index == 0:
            return self.head
        elif  not (index >= self.length or index < 0):
            middle_index = int(self.length/2)
            contador = 0
            if index <= middle_index:
                current_node = self.head
                while(contador != index):
                    current_node = current_node.next_node
                    contador += 1
            else :
                contador =self.length-1
                current_node = self.tail
                while(contador != index):
                    current_node = current_node.previuos_node
                    contador -= 1
            return current_node
        else :
            return None
    
    #Insertar un valor en una posicion especifica
    def insert_v1(self, index, value):
        if index == self.length +1 :
            return self.add_node_tail(value)
        elif index == 1:
            return self.add_node_head(value)
        elif not (index >= self.length+1 or index <= 0):
            new_node = self.Node(value)
            previous_node = self.get(index-2)
            nodos_siguientes = previous_node.next_node
            previous_node.next_node = new_node
            new_node.previuos_node = previous_node
            new_node.next_node = nodos_siguientes
            nodos_siguientes.previuos_node = new_node
            self.length += 1
        else:
            return None
        
    #Actualizar el valor de un nodo por su indice sacando la potencia cuadrada del anterior
    def update(self,index):
        node_update = self.get(index-1)
        if node_update != None:
            try:
                valor = int(node_update.previuos_node.value)
                node_update.value = (valor)*(valor)
            except:
                print('No se puede realizar la actualizacion de dicho nodo')
    
    #Eliminar un nodo por su indice
    def remove(self,index):
        if index == self.length +1:
            return self.delete_tail()
        elif index == 1:
            return self.delete_head()
        elif not (index >= self.length or index <0):
            node_remove = self.get(index-1)
            previous_nodee = node_remove.previuos_node
            next_nodee = node_remove.next_node
            previous_nodee.next_node = next_nodee
            next_nodee.previous_node = previous_nodee
            self.length -=1
        else :
            return None
        
    #Agregar un nodo en una posicion pero para ser agregado debe ser un multiplo de el siguiente nodo
    def insert(self,index,value):
        node_insert = self.get(index-1) 
        new_node = self.Node(value)
        if node_insert != None :
            try :
                value_next = int(node_insert.value)
            except:
                print('El siguiente no es un entero')
            if  type(value) == str or type(node_insert.value) == str or value % value_next == 0 :
                if index == 1:
                    self.add_node_head(value)
                elif not (index >= self.length+1 or index <0):
                    previo = node_insert.previuos_node
                    previo.next_node = new_node
                    node_insert.previous_node = new_node
                    new_node.next_node = node_insert
                    new_node.previuos_node = previo
                    self.length += 1
            else :
                print('No se puede realizar la insercion')
        elif index == self.length+1:
            self.add_node_tail(value)
        
    ##Invierte el orden de la lista de nodos
    def reverse(self):
        current_node = self.head
        node_reverse = None
        self.tail = current_node
        while current_node != None:
            next_n = current_node.next_node
            current_node.next_node = node_reverse
            node_reverse = current_node
            current_node.previuos_node = next_n
            current_node = next_n 
        self.head = node_reverse
        self.change_root()
        return self.head
    
    def change_root(self):
        current_node = self.head
        while current_node != None:
            if type(current_node.value) == int :
                current_node.value = sqrt(current_node.value)  
            current_node = current_node.next_node