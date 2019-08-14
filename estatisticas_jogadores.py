jogador = {}
lista_jogadores = []
lista_gols = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    tot = int(input('Digite o número de partidas: '))
    lista_gols.clear()
    for i in range(1, tot+1):
        lista_gols.append(int(input(f'Quantos gols na partida {i}: ')))
    jogador['Gols'] = lista_gols[:]
    jogador['Total de gols'] = sum(lista_gols)
    lista_jogadores.append(jogador.copy())
    while True:
        cont = str(input('Deseja continuar? S-Sim, N-Não: ')).upper()[0]
        if cont in 'SN':
            break
        print('Opção Inválida!')
    if cont == 'N':
        break

print(lista_jogadores)

print('-=' * 20)
print('Cód ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)
for k, v in enumerate(lista_jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40) 

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(lista_jogadores):
        print('Opção inválida!')
    else:
        print(f'\nESTATÍSTICAS DO JOGADOR: {lista_jogadores[busca]["Nome"]}')
        for i, g in enumerate(lista_jogadores[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gol(s)')
    print('-' * 40)
print('Programa Finalizado!')
