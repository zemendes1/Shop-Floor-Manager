


pathVector = [] #Tipos de transformação que a peça de origem tem de alcançar para se transformar na peça pedida

OrderPiece = 'P7' #Peça Pedida
StartPiece = '' #Peça de origem

if OrderPiece in ['P4', 'P7', 'P9', 'P5', 'P3']:
    StartPiece = 'P2'
elif OrderPiece in ['P6', 'P8']:
    StartPiece = 'P1'


if OrderPiece == 'P3':
    pathVector.append(3)  #Peça Pedida
    pathVector.append(2)  #Tipo de transformação ou (se 0) sinal que não é preciso transformar mais
    pathVector.append(0)
    pathVector.append(0)
    pathVector.append(0)

if OrderPiece == 'P4':
    pathVector.append(4)
    pathVector.append(3)
    pathVector.append(0)
    pathVector.append(0)
    pathVector.append(0)

if OrderPiece == 'P5':
    pathVector.append(5)
    pathVector.append(3)
    pathVector.append(4)
    pathVector.append(3)
    pathVector.append(4)

if OrderPiece == 'P6':
    pathVector.append(6)
    pathVector.append(1)
    pathVector.append(0)
    pathVector.append(0)
    pathVector.append(0)

if OrderPiece == 'P7':
    pathVector.append(7)
    pathVector.append(3)
    pathVector.append(4)
    pathVector.append(0)
    pathVector.append(0)

if OrderPiece == 'P8':
    pathVector.append(8)
    pathVector.append(1)
    pathVector.append(3)
    pathVector.append(0)
    pathVector.append(0)

if OrderPiece == 'P9':
    pathVector.append(9)
    pathVector.append(3)
    pathVector.append(4)
    pathVector.append(3)
    pathVector.append(0)

print(pathVector)