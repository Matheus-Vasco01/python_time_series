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



"""
Nome do arquivo: exercicios_funcoes.py
Autor:          Matheus
Data:           10/11/2025
Versão:         1.0
Descrição:      Módulo de exercícios Python com funções utilitárias
                para matemática, processamento de texto e análise
                de dados simples.
"""

import re

def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    return n % 2 == 0

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    if n == 0:
        return 1
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def maximo(nums: list) -> int | float:
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    # Assume que a lista não está vazia, conforme a docstring.
    # Se estivesse vazia, nums[0] levantaria um IndexError.
    maior_atual = nums[0]
    for num in nums[1:]:
        if num > maior_atual:
            maior_atual = num
    return maior_atual

def limpa_texto(s: str) -> str:
    """Deixa minúsculo e remove pontuação comum."""
    # Converte para minúsculo
    s_lower = s.lower()
    # Remove os caracteres de pontuação especificados
    s_limpo = re.sub(r'[,\.;:!?\'"()-_]', '', s_lower)
    return s_limpo

def conta_vogais(s: str) -> int:
    """Conta vogais (a,e,i,o,u) em s (desconsidere acentos)."""
    vogais = 'aeiou'
    contador = 0
    for char in s.lower():
        if char in vogais:
            contador += 1
    return contador

def palindromo(s: str) -> bool:
    """Retorna True se s é palíndromo ignorando espaços e pontuação."""
    # Normalizar: minúsculo e remove tudo que não for letra ou número
    normalizado = re.sub(r'[^a-z0-9]', '', s.lower())
    # Compara a string com o seu reverso
    return normalizado == normalizado[::-1]

def total_por_vendedor(vendas: list) -> dict:
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    totais = {}
    for nome, valor in vendas:
        # Usa dict.get() para pegar o valor atual ou 0 se o nome não existir
        totais[nome] = totais.get(nome, 0) + valor
    return totais

def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    if not totais:
        raise ValueError("O dicionário de totais está vazio.")

    # Inicializa com o primeiro item (ou float('-inf') se preferir)
    # Iterar pelos itens é mais direto que pegar as chaves primeiro
    
    melhor_nome = None
    maior_total = float('-inf') # Garante que qualquer valor será maior

    for nome, total in totais.items():
        if total > maior_total:
            maior_total = total
            melhor_nome = nome
            
    return (melhor_nome, maior_total)
