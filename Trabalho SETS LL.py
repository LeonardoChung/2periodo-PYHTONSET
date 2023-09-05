print("BCC - 2B")
print("Leonardo Min Woo Chung")
print("Lucas Fernandes de Oliveira")
print()
print()


def opera_fazer(operacao, conjunto1, conjunto2):
    if operacao == 'U':
        return conjunto1.union(conjunto2), 'União'
    elif operacao == 'I':
        return conjunto1.intersection(conjunto2), 'Intersecção'
    elif operacao == 'D':
        return conjunto1.difference(conjunto2), 'Diferença'
    elif operacao == 'C':
        produto_cartesiano = {(a, b) for a in conjunto1 for b in conjunto2}
        return produto_cartesiano, 'Produto cartesiano'
    else:
        return set(), 'Operação errada. Tente novamente'

resultados = []

while True:
    operacao = input("Digite a operação (U = União, I = Intersecção, D = Diferença, C = Produto Cartesiano): ").strip().upper()

    lista1 = set(input("Digite os elementos do conjunto 1 separados por vírgula: ").strip().split(','))
    lista2 = set(input("Digite os elementos do conjunto 2 separados por vírgula: ").strip().split(','))

    resultado, resultado_opera = opera_fazer(operacao, lista1, lista2)
    resultados.append((resultado_opera, lista1, lista2, resultado))

    print()
    print(f'Operação: {resultado_opera}')
    print(f'Conjunto 1: {lista1}')
    print(f'Conjunto 2: {lista2}')
    print(f'Resultado: {resultado}')
    print()

    continuar = input("Deseja realizar outra operação? (S para sim, qualquer outra tecla para sair): ")
    if continuar.lower() != 's':
        break
