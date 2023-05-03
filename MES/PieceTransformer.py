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

# Peça Final → n.º de transfromações
# Transformação1 → Tempo de Transformação
# Transformação2 → Tempo de Transformação
# Transformação3 → Tempo de Transformação
# Transformação4 → Tempo de Transformação

def define_vector(orderpiece):
    pathVector = []
    # Categorias de transformação que a peça de origem tem de alcançar para se transformar na peça pedida
    if orderpiece == 'P3_from_P2':
        pathVector.append([3, 1])
        pathVector.append([2, 10])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P4_from_P2':
        pathVector.append([4, 1])
        pathVector.append([3, 10])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P5_from_P2':
        pathVector.append([5, 4])
        pathVector.append([3, 10])
        pathVector.append([6, 10])
        pathVector.append([8, 10])
        pathVector.append([4, 15])

    if orderpiece == 'P5_from_P4':
        pathVector.append([5, 3])
        pathVector.append([6, 10])
        pathVector.append([8, 10])
        pathVector.append([4, 15])
        pathVector.append([0, 0])

    if orderpiece == 'P5_from_P7':
        pathVector.append([5, 2])
        pathVector.append([8, 10])
        pathVector.append([4, 15])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P5_from_P9':
        pathVector.append([5, 1])
        pathVector.append([4, 15])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P6_from_P1':
        pathVector.append([6, 1])
        pathVector.append([1, 20])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P6_from_P2':
        pathVector.append([6, 2])
        pathVector.append([2, 10])
        pathVector.append([5, 20])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P6_from_P3':
        pathVector.append([6, 1])
        pathVector.append([5, 20])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P7_from_P2':
        pathVector.append([7, 2])
        pathVector.append([3, 10])
        pathVector.append([6, 10])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P7_from_P4':
        pathVector.append([7, 1])
        pathVector.append([6, 10])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P8_from_P1':
        pathVector.append([8, 2])
        pathVector.append([1, 20])
        pathVector.append([7, 30])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P8_from_P2':
        pathVector.append([8, 3])
        pathVector.append([2, 10])
        pathVector.append([5, 20])
        pathVector.append([7, 30])
        pathVector.append([0, 0])

    if orderpiece == 'P8_from_P3':
        pathVector.append([8, 2])
        pathVector.append([5, 20])
        pathVector.append([7, 30])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P8_from_P6':
        pathVector.append([8, 1])
        pathVector.append([7, 30])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P9_from_P2':
        pathVector.append([8, 3])
        pathVector.append([3, 10])
        pathVector.append([6, 10])
        pathVector.append([8, 10])
        pathVector.append([0, 0])

    if orderpiece == 'P9_from_P4':
        pathVector.append([8, 2])
        pathVector.append([6, 10])
        pathVector.append([8, 10])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'P9_from_P7':
        pathVector.append([8, 1])
        pathVector.append([8, 10])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    if orderpiece == 'null':
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])
        pathVector.append([0, 0])

    return pathVector


""""
print(define_vector('P7_from_P2'))
"""
