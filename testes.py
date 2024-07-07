# Lista original de listas
lista_original = [[1, 2], [3, 4], [5, 6]]

# Shallow copy da lista de listas
shallow_copy = lista_original[:]

# Iteração e remoção na shallow copy
for sublist in shallow_copy[:]:  # Usando [:] para criar uma cópia e iterar sobre ela
    if sublist[0] == 3:  # Exemplo de condição de remoção
        shallow_copy.remove(sublist)

print("Lista Original:", lista_original)  # Saída: [[1, 2], [3, 4], [5, 6]]
print("Shallow Copy após Remoção:", shallow_copy)  # Saída: [[1, 2], [5, 6]]