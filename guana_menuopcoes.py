def main():
    valor_1 = int(input('Primeiro valor: '))
    valor_2 = int(input('Segundo valor: '))
    operacao = 0
    while operacao != 5:
        print('Digite:\n [1] - Somar\n [2] - Multiplicar\n [3] - Maior\n\
 [4] - Novos números\n [5] - Sair\n  ')
        operacao = int(input('Qual a sua opção? '))
        if operacao == 1:
            result = valor_1 + valor_2
            print(f'{result}')
        elif operacao == 2:
            result = valor_1 * valor_2
            print(f'{result}')
        elif operacao == 3:
            if valor_1 > valor_2:
                print(f'{valor_1} é maior')
            elif valor_2 > valor_1:
                print(f'{valor_2} é maior')
            else:
                print('Os números são iguais')
        elif operacao == 4:
            valor_1 = int(input('Primeiro valor: '))
            valor_2 = int(input('Segundo valor: '))
        elif operacao == 5:
            print('Finalizando...')
        else:
            print('Opção inválida!')
    print('Seu programa foi finalizado!')

main()
