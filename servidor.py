def main():
    cadastro = []
    usuario = {}
    cadastro = cadastraUsuario(cadastro, usuario)
    cadastro = converteBytes(cadastro)
    cadastro = porcentagem(cadastro)
    imprimeCadastro(cadastro)


def cadastraUsuario(cadastro, usuario):
    for i in range(6):
        usuario.clear()
        usuario['Nr.'] = i+1
        usuario['Nome'] = str(input(f'Digite o nome do {i+1}º \
usuário: '))
        usuario['Dados'] = float(input('Digite a quantidade de \
dados usada por esse usuário: '))
        cadastro.append(usuario.copy())
    return cadastro


def converteBytes(cadastro):
    for d in cadastro:
        d['Dados'] /= 1048576
        d['Dados'] = round(d['Dados'], 2)
    return cadastro


def porcentagem(cadastro):
    soma_dados = 0
    for d in cadastro:
        soma_dados += d['Dados']
    for i in range(len(cadastro)):
        cadastro[i]['Porcentagem'] = (cadastro[i]['Dados'] * 100) / soma_dados
        cadastro[i]['Porcentagem'] = round(cadastro[i]['Porcentagem'], 2)
        cadastro[i]['Porcentagem'] = str(cadastro[i]['Porcentagem']) + ' %'
    for d in cadastro:
        d['Dados'] = str(d['Dados']) + ' MB'
    return cadastro


def imprimeCadastro(cadastro):
    print('\nACME Inc', end='       ')
    print('Uso do espaço em disco pelos usuários')
    print('-' * 55)
    i = 0
    for k in cadastro[i].keys():
        print(f'{k:<15}', end='')
        i += 1
    print()

    for j in range(len(cadastro)):
        for v in cadastro[j].values():
            print(f'{v:<15}', end='')
        print()


main()
