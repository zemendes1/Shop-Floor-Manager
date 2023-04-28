def n_of_pieces(vetor):
    peca1, peca2, peca3, peca4, peca5, peca6, peca7, peca8, peca9 = 0, 0, 0, 0, 0, 0, 0, 0, 0

    for i in range(1, 9):
        if vetor[i] == 1:
            peca6 += 1
        elif vetor[i] == 2:
            peca3 += 1
        elif vetor[i] == 3:
            peca4 += 1
        elif vetor[i] == 4:
            peca5 += 1
        elif vetor[i] == 5:
            peca6 += 1
        elif vetor[i] == 6:
            peca7 += 1
        elif vetor[i] == 7:
            peca8 += 1
        elif vetor[i] == 8:
            peca9 += 1

    return peca1, peca2, peca3, peca4, peca5, peca6, peca7, peca8, peca9
