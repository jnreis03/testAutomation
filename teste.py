import pytest
from soma import soma  # Substitua 'sua_função' pelo nome do arquivo onde a função soma está definida

def test_soma():
    # Teste 1: Verifica se a soma de 1 e 2 é igual a 3
    assert soma(1, 2) == 3

    # Teste 2: Verifica se a soma de números negativos está correta
    assert soma(-1, -1) == -2

    # Teste 3: Verifica se a soma de um número positivo e um negativo está correta
    assert soma(5, -3) == 2

    # Teste 4: Verifica se a soma de zeros está correta
    assert soma(0, 0) == 0

    # Teste 5: Verifica se a soma de um número positivo e zero está correta
    assert soma(7, 0) == 7
