def main():
    print('Esse programa recebe dois valores inteiros e executa \
a operação que você escolher.')
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    op = operacao(num1, num2)
    executa_operacao(num1, num2, op)


def operacao(num1, num2):
    op = int(input('''Escolha a operação que deseja executar
[1] - Soma
[2] - Multiplicação
[3] - Maior
[4] - Novos números
[5] - Sair do Programa
Digite aqui a opção: '''))
    while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print('Opção inválida!')
        op = int(input('''Escolha a operação que deseja executar
[1] - Soma
[2] - Multiplicação
[3] - Maior
[4] - Novos números
[5] - Sair do Programa
Digite aqui a opção: '''))
    return op


def executa_operacao(num1, num2, op):
    if op == 1:
        soma = num1 + num2
        print(f'A soma dos números é {soma}')
    elif op == 2:
        mult = num1 * num2
        print(f'O produto dos números é {mult}')
    elif op == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        elif num1 < num2:
            print(f'{num2} é maior que {num1}')
        else:
            print('Os números são iguais')
    elif op == 4:
        main()
    else:
        print('Fim do programa!')


main()
