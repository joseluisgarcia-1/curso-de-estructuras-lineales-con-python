from clase10_node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1
    
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            return "The stack is empty"
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"
    
    def clear(self):
        while self.top:
            self.pop()

food = Stack()
food.push("egg")
food.push("ham")
food.push("spam")
#con este sacamos a spam porque es el ultimo dato en llegar y como la regla dice que el último en llegar es el primero en salir
food.pop()
print(food.peek())
#con esto limpiamos el stack
food.clear()
#aquí ya nos imprime que el stack está vacío
print(food.peek())