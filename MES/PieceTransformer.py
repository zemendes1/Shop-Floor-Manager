# Casos Possíveis
# P3_from_P2
# P4_from_P2
# P5_from_P2
# P5_from_P4
# P5_from_P7
# P5_from_P9
# P6_from_P1
# P6_from_P2
# P6_from_P3
# P7_from_P2
# P7_from_P4
# P8_from_P1
# P8_from_P2
# P8_from_P3
# P8_from_P6
# P9_from_P2
# P9_from_P4
# P9_from_P7

# Peça que vai se produzida→ Peça que sai do armazem
# Tool → Tempo de Transformação

def define_vector(orderpiece):
    pathVector = []
    # Categorias de transformação que a peça de origem tem de alcançar para se transformar na peça pedida
    if orderpiece == 'P3_from_P2':
        pathVector.append([3, 2])
        pathVector.append([2, 10])

    if orderpiece == 'P4_from_P2':
        pathVector.append([4, 2])
        pathVector.append([3, 10])

    if orderpiece == 'P5_from_P9':
        pathVector.append([5, 9])
        pathVector.append([4, 15])

    if orderpiece == 'P6_from_P1':
        pathVector.append([6, 1])
        pathVector.append([1, 20])

    if orderpiece == 'P6_from_P3':
        pathVector.append([6, 3])
        pathVector.append([1, 20])

    if orderpiece == 'P7_from_P4':
        pathVector.append([7, 4])
        pathVector.append([4, 10])

    if orderpiece == 'P8_from_P6':
        pathVector.append([8, 6])
        pathVector.append([3, 30])

    if orderpiece == 'P9_from_P7':
        pathVector.append([9, 7])
        pathVector.append([3, 10])

    if orderpiece == 'null':
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    return pathVector
