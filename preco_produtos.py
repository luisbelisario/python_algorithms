total = mais_mil = menor_preco = cont = 0
mais_barato = ''
continua = True

while continua:
    nome = str(input('Digite o nome do produto: ')).upper()
    preco = float(input('Digite o preço em R$: '))
    cont += 1
    while preco <= 0:
        print('Valor inválido!')
        preco = float(input('Digite o preço em R$: '))
    if preco > 1000:
        mais_mil += 1
    if cont == 1:
        menor_preco = preco
        mais_barato = nome
    else:
        if preco < menor_preco:
            menor_preco = preco
            mais_barato = nome
    total += preco
    novo_cadastro = str(input('Deseja cadastrar um novo produto? \
Digite S para Sim ou N para Não: ')).upper()
    while novo_cadastro not in 'SN':
        print('Escolha inválida!')
        novo_cadastro = str(input('Deseja cadastrar um novo produto? \
Digite S para Sim ou N para Não: ')).upper()
    if novo_cadastro == 'S':
        continua = True
    else:
        continua = False


print(f'O total gasto em compras foi: R$ {total:.2f}')
print(f'{mais_mil} produto(s) com preço maior que R$ 1000,00')
print(f'O produto mais barato foi {mais_barato} \
que custou R$ {menor_preco:.2f}')
