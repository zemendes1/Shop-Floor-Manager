# Peça a entregar -> Dock a entregar

def define_dock(delivery):
    Vector = []
    # Categorias de transformação que a peça de origem tem de alcançar para se transformar na peça pedida
    if delivery == 'P3_on_1':
        Vector = [3, 1]
    if delivery == 'P3_on_2':
        Vector = [3, 2]
    if delivery == 'P4_on_1':
        Vector = [4, 1]
    if delivery == 'P4_on_2':
        Vector = [4, 2]
    if delivery == 'P5_on_1':
        Vector = [5, 1]
    if delivery == 'P5_on_2':
        Vector = [5, 2]
    if delivery == 'P6_on_1':
        Vector = [6, 1]
    if delivery == 'P6_on_2':
        Vector = [6, 2]
    if delivery == 'P7_on_1':
        Vector = [7, 1]
    if delivery == 'P7_on_2':
        Vector = [7, 2]
    if delivery == 'P8_on_1':
        Vector = [8, 1]
    if delivery == 'P8_on_2':
        Vector = [8, 2]
    if delivery == 'P9_on_1':
        Vector = [9, 1]
    if delivery == 'P9_on_2':
        Vector = [9, 2]
    if delivery == 'null':
        Vector = [0, 0]
    return Vector
