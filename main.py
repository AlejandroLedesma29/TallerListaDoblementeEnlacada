from doubleLinkedList import DoubleLinkedList
inst_DLL = DoubleLinkedList()

inst_DLL.add_node_head(4)
inst_DLL.add_node_head('B')
inst_DLL.add_node_head(9)
inst_DLL.add_node_head(5)
inst_DLL.add_node_head(36)
inst_DLL.show_double_linked_list()
print(f'El valor de el nodo buscado es {inst_DLL.get(2).value}')
inst_DLL.show_double_linked_list()
#TERCER PUNTO
inst_DLL.remove(4)
inst_DLL.show_double_linked_list()
#SEGUNDO PUNTO 
inst_DLL.insert(2,25)
inst_DLL.show_double_linked_list()
#PRIMER PUNTO
inst_DLL.update(2)
inst_DLL.show_double_linked_list()
#CUARTO PUNTO
inst_DLL.reverse()
inst_DLL.show_double_linked_list()
