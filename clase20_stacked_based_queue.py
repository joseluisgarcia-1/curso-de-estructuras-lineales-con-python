class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    #para agregar datos
    def enqueue(self, data):
        self.inbound_stack.append(data)
    
    #para eliminar datos
    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        
        return self.outbound_stack.pop()

numbers = Queue()
numbers.enqueue(5)
numbers.enqueue(6)
numbers.enqueue(7)
print(numbers.inbound_stack)
#quita el primer número que se agregó
print(numbers.dequeue())
#nos imprime vacío porque le aplicamos el método pop en la línea 14
print(numbers.inbound_stack)
#En este falta el 5 porque en la línea 16 le decimos que saque ese número que pasó a ser la primera posición en el queue
print(numbers.outbound_stack)
