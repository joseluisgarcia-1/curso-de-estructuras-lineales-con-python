"""
Se crea una clase y se le añaden dos métodos para que pueda funcionar
"""

class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    #Agregar elementos
    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    #eliminar elementos
    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    #método de recorrido para saber qué es lo que hay dentro del queue, cuántos y qué elementos hay
    def traverse(self):
        total_items = self.size

        for item in range(total_items):
            print(self.items[item])

food = ListQueue()
food.enqueue("egg")
food.enqueue("ham")
food.enqueue("spam")
#saca el dato que entró de primero
print(food.dequeue())
food.traverse()