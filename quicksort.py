import random
def quicksort(array):
    if len(array)<2:
        return array
    else:
        randomindex = random.randint(0,len(array)-1)
        pivo = array[randomindex]
        esquerda = [i for i in array[1:] if i<=pivo]
        direita = [i for i in array[1:] if i>pivo]
        return quicksort(esquerda) + [pivo] + quicksort(direita)

print(quicksort([2,5,6,1,3,9,4]))