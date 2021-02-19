def bubbleSort(lista):
    for aux in range(len(lista)-1,0,-1):
        for i in range(aux):
            if lista[i]<lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

lista = [585,13,35,29,99,88,2,13,22]
bubbleSort(lista)
print(lista)