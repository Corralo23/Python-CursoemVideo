#Crie um programa que leie NOME, SEXO E IDADE de várias pessoas, guardando os dados em um dicionario e todos os dicionários em uma lista. No final mostre:
# a) Quantas pessoas cadastradas; b) A media de idade; c) Uma lista com mulheres; d) Uma lista com idade acima da média
pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear() #funcionalidade ==> para não ficar lista duplicada
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]')).upper()
        if pessoa['sexo'] in 'MmFf':
            break
        print('ERRO!!! Digite apenas M ou F).')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!!! REsponda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(galera)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ,', end='')
for p in galera:
    if p['sexo'] in 'Ff': # por ser ==> if p['sexo'] == F:
        print(f'{p["nome"]} ,', end='')
print()
print('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<ENCERRADO>>>')
