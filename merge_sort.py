def merge_sort(vetor):
    if len(vetor) <= 1:
        return vetor
    
    meio = len(vetor) // 2
    esquerda = merge_sort(vetor[:meio])
    direita = merge_sort(vetor[meio:])
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

vetor = [38, 27, 43, 3, 9, 82, 10]    
print("Vetor original:", vetor)
print("Vetor ordenado:", merge_sort(vetor))