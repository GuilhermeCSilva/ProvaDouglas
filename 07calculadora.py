primeironum = int(input('insira um numero: '))
op = input('escolha uma opcao  + somar - subtrair * multiplicar / dividir')
segundonum = int(input('insira o proximo numero:'))

if op == '+':
    print(f'Soma:{primeironum}+{segundonum} =  {primeironum + segundonum}')

elif op == '-':
    print(f'Subtracao: {primeironum} - {segundonum} = {primeironum - segundonum}')

elif op == '*':
    print(f'Multiplicação: {primeironum} * {segundonum} = {primeironum * segundonum}')

elif op == '/':
    print(f'Divisão: {primeironum} / {segundonum} = {primeironum / segundonum}')

else:
    print('Selecione uma operacao valida')