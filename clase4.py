fruits = []
fruits.append("Kiwi")
fruits.append("Berry")
fruits.append("Melón")
print(fruits)
fruits.sort()
print(fruits)
#pop nos elimina siempre el último dato de la lista
fruits.pop()
print(fruits)
#insert, podemos insertar datos en la lista y le podemos indicar su índice
fruits.insert(0, "Orange")
print(fruits)
#me imprime la fruta que está en la posición dos de la lista
print(fruits[2])
#saca la fruta que está en la posición dos de la lista
print(fruits.pop(2))
#puedo eliminar o remover un dato de la lista con remove
fruits.append("Kiwi")
print(fruits)
fruits.remove("Kiwi")
print(fruits)

#función recursiva

def pyramid_sum(lower,upper, margin=0):
    blanks = ""*margin
    print(blanks, lower,upper)
    #si el limite inferior es mayor que es el limite superior,unicamente imprima los espacios en blanco con cero como margen
    if lower > upper:
        print(blanks, 0)
        return 0
    #si no, imprimos el limite inferior más la función recursiva
    else:
        result = lower + pyramid_sum(lower +1, upper, margin +4)
        print(blanks, result)
        return result
pyramid_sum(1,4)