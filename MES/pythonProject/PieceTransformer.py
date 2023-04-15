pathVector = []  # Categorias de transformação que a peça de origem tem de alcançar para se transformar na peça pedida


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

# Peça Base
# Peça Final
# Transformação1
# Transformação2
# Transformação3

def define_vector(orderpiece):
    if orderpiece == 'P3_from_P2':
        pathVector.append(3)
        pathVector.append(2)
        pathVector.append(0)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P4_from_P2':
        pathVector.append(4)
        pathVector.append(3)
        pathVector.append(0)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P5_from_P2':
        pathVector.append(5)
        pathVector.append(4)
        pathVector.append(4)
        pathVector.append(3)
        pathVector.append(4)

    if orderpiece == 'P5_from_P4':
        pathVector.append(5)
        pathVector.append(4)
        pathVector.append(3)
        pathVector.append(4)
        pathVector.append(0)

    if orderpiece == 'P5_from_P7':
        pathVector.append(5)
        pathVector.append(3)
        pathVector.append(4)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P5_from_P9':
        pathVector.append(5)
        pathVector.append(4)
        pathVector.append(0)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P6_from_P1':
        pathVector.append(6)
        pathVector.append(1)
        pathVector.append(0)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P6_from_P2':
        pathVector.append(6)
        pathVector.append(2)
        pathVector.append(1)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P6_from_P3':
        pathVector.append(6)
        pathVector.append(1)
        pathVector.append(0)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P7_from_P2':
        pathVector.append(7)
        pathVector.append(3)
        pathVector.append(4)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P7_from_P4':
        pathVector.append(7)
        pathVector.append(4)
        pathVector.append(0)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P8_from_P1':
        pathVector.append(8)
        pathVector.append(1)
        pathVector.append(3)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P8_from_P2':
        pathVector.append(8)
        pathVector.append(2)
        pathVector.append(1)
        pathVector.append(3)
        pathVector.append(0)

    if orderpiece == 'P8_from_P3':
        pathVector.append(8)
        pathVector.append(1)
        pathVector.append(3)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P8_from_P6':
        pathVector.append(8)
        pathVector.append(3)
        pathVector.append(0)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P9_from_P2':
        pathVector.append(9)
        pathVector.append(3)
        pathVector.append(4)
        pathVector.append(3)
        pathVector.append(0)

    if orderpiece == 'P9_from_P4':
        pathVector.append(9)
        pathVector.append(4)
        pathVector.append(3)
        pathVector.append(0)
        pathVector.append(0)

    if orderpiece == 'P9_from_P7':
        pathVector.append(9)
        pathVector.append(3)
        pathVector.append(0)
        pathVector.append(0)
        pathVector.append(0)


define_vector('P7_from_P2')
print(pathVector)
