nome= input('Insira seu nome:')
idade= int(input('Insira sua idade:'))
if(idade==1):
    print(f'{nome}, você tem {idade} ano e não pode ir pra cadeia.')
else:
    while(idade<0):
        idade= int(input('Não dá pra ter idade negativa, parça. Bota sua idade de verdade:'))
    if(1<idade<18):
        print(f'{nome}, você tem {idade} anos e não pode ir pra cadeia.')
    else:
        print(f'{nome}, você tem {idade} anos e já pode ir pra cadeia, cuidado.')