def main():
    cadastro = []
    habitante = {}
    cadastro = cadastraHabitantes(cadastro, habitante)
    media_idade = mediaIdade(cadastro)
    if media_idade > 0:
        print(f'A média de idade de pessoa com olhos castanhos \
e cabelos pretos foi de {media_idade:.2f} anos')
    else:
        print(f'Não foram cadastrados habitantes com olhos \
castanhos e cabelos pretos')
    maior_idade, nome_maior_idade = maiorIdade(cadastro)
    print(f'A maior idade entre os habitantes foi \
de {nome_maior_idade} com {maior_idade} anos')
    qtd_mulheres = qtdMulheres(cadastro)
    if qtd_mulheres > 0:
        print(f'Foram cadastradas {qtd_mulheres} mulheres')
    else:
        print('Não foi cadastrada nenhuma mulher')


def cadastraHabitantes(cadastro, habitante):
    for _ in range(3):
        habitante.clear()
        habitante['Nome'] = str(input('Digite o nome do habitante: '))
        habitante['Sexo'] = str(input('Digite o sexo do \
habitante - M ou F: ')).upper()
        while habitante['Sexo'] not in 'MmFf':
            print('Sexo inválido!')
            habitante['Sexo'] = str(input('Digite o sexo do \
habitante - M ou F: ')).upper()
        habitante['Olhos'] = str(input('Digite a cor dos \
olhos do habitante: ')).lower()
        habitante['Cabelos'] = str(input('Digite a cor dos \
cabelos do habitante: ')).lower()
        habitante['Idade'] = int(input('Digite a idade do habitante: '))
        cadastro.append(habitante.copy())
    return cadastro


def mediaIdade(cadastro):
    soma_idade = 0
    total_pessoas = 0
    for h in cadastro:
        if h['Olhos'] == 'castanhos' and h['Cabelos'] == 'pretos':
            soma_idade += h['Idade']
            total_pessoas += 1
    if total_pessoas == 0:
        return 0
    else:
        media = soma_idade / total_pessoas
        return media


def maiorIdade(cadastro):
    maior_idade = cadastro[0]['Idade']
    nome_maior_idade = cadastro[0]['Nome']
    for i in cadastro:
        if i['Idade'] > maior_idade:
            maior_idade = i['Idade']
            nome_maior_idade = i['Nome']
    return maior_idade, nome_maior_idade


def qtdMulheres(cadastro):
    qtd_mulheres = 0
    for p in cadastro:
        if (p['Sexo'] == 'F'):
            qtd_mulheres += 1
    return qtd_mulheres


main()
