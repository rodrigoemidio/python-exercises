<<<<<<<< HEAD:idadeCondicional.py
nome= input('Insira seu nome:')
idade= int(input('Insira sua idade:'))
if(idade==1):
    print(f'{nome}, você tem {idade} ano e não pode ir pra cadeia.')
else:
    while(idade<0):
        idade= int(input('Não é possível ter idade negativa. Insira sua idade:'))
    if(1<idade<18):
        print(f'{nome}, você tem {idade} anos e não pode ir pra cadeia.')
    else:
        print(f'{nome}, você tem {idade} anos e já pode ir pra cadeia, cuidado.')
========
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
>>>>>>>> 0cfa9d996e1b2a1811ddb559578a352e06623ff7:python-ex/Ex3.py
