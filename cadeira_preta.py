O que é um cabeçalho em um arquivo Python, para que serve? O que é uma docstring e qual a sua diferenca?
o cabecalho e a parte inicial de um arquivo py.
ex: """
Nome do arquivo: programa.py
Autor: Seu Nome
Data: 2025-08-25
Versão: 1.0
Descrição: Este programa faz...
"""

a Docstring serve para documentar funcoes, classes e modulos, Fica logo após a declaração e serve para explicar o que o código faz. Pode ser acessada com help() ou __doc__.

o cabecalho fica no inicio do arquivo, enquanto a docstring fica dentro de funcoes, classes e modulos, ela documenta em lugares especificos enquando o cabecalho no doc todo




# formate o cabeçalho deste arquivo após completar os exercícios abaixo:

def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    # TODO: retorne se n é par
    ...

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    # TODO: implemente de forma iterativa (sem recursão)
    ...

def maximo(nums):
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    # TODO: percorra a lista guardando o maior atual
    ...

import re

def limpa_texto(s: str) -> str:
    """Deixa minúsculo e remove pontuação comum."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """Conta vogais (a,e,i,o,u) em s (desconsidere acentos)."""
    # TODO: conte as vogais simples
    ...

def palindromo(s: str) -> bool:
    """Retorna True se s é palíndromo ignorando espaços e pontuação."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso
    ...

def total_por_vendedor(vendas):
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    # TODO: inicialize um dict e vá somando
    ...

def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)
    ...
