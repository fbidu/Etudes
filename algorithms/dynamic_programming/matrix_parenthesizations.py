from math import inf
from warnings import warn

warn("This module is not fully implemented and incorrect!", UserWarning)


def parenthesizations(dimensoes):
    """
    A forma ótima de 'parentizar' as matrizes A_i, ..., A_j é denotada A_ij.
    Suponha i<k<j, a parentização ótima de de A_ij contém A_ik e A_(k+1)j.
    A parentização A_ik contida em A_ij é ótima assim como a parentização
    de A_(k+1)j contida em A_ij é ótima também.

    Suponha que m[i][j] seja uma matriz que guarda o custo ótimo para
    multiplicar as matrizes i e j. Ora, se i=j, o custo é zero pois
    não é necessário realizar operação alguma uma vez que apenas
    uma matriz foi oferecida como entrada. Se i < j, podemos
    dividí-lo entre i->k e (k+1)->j e o custo m[i][j] será
    o custo mínimo para m[i][k] somado ao mínimo para
    m[k+1][j] e somado ao custo para multiplicar as
    duas matrizes.

    Portanto:

        m[i][j] = m[i][k] + m[k+1][j] + p_i-1*p_k*p_j

    Considerando que uma matriz A_i tem dimensões p_i-1 x p_i

    Note que k = i, i + 1, ..., j - 1; Como todos esses valores
    são possíveis, temos:

        m[i][j] = 0, se i = j
        m[i][j] = min(m[i][k] + m[k+1][j] + p_i-1*p_k*p_j) p/ todo k

    Se quisermos recuperar a informação sobre a parentização ótima - 
    e não só seu custo - podemos guardar s[i][j] que contém o valor
    do k-ótimo para A_ij.

    Assuma que a entrada desse algoritmo seja:

        p = [p_0, p_1, ..., p_n]
    
    Onde |p| = n+1 e a matriz A_i tem dimensões p_(i-1) X p_i


    Obs 1: Por que A_ik contida em A_ij é a solução ótima para A_ik?
            A_ik em A_ij é ótima pois, suponha que não fosse e que existe
            A_im, uma parametrização para Ai..Ak melhor do que A_ik, então
            poderíamos trocar A_ik por A_im em A_ij e chegar numa solução
            mais eficiente que A_ij *mas* A_ij foi dada como sendo uma
            solução *ótima*, portanto é impossível a existência de
            uma solução melhor que ela.
    """
    n = len(dimensoes) - 1
    cache = [[0 for _ in range(n)] for _ in range(n)]
    cuts = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        cache[i][i] = 0

    for l in range(2, n):
        for i in range(n - l):
            j = i + l - 1
            cache[i][j] = inf
            for k in range(i, j):
                q = (
                    cache[i][k]
                    + cache[k + 1][j]
                    + dimensoes[i - 1] * dimensoes[k] * dimensoes[j]
                )
                if q < cache[i][j]:
                    cache[i][j] = q
                    cuts[i][j] = k

    return (cache, cuts)


def main():
    matrixes = [10, 100, 5, 50]
    parenthesizations(matrixes)


if __name__ == "__main__":
    main()
