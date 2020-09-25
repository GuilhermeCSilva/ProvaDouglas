palavra = 'guilherme camargo silva'

index = 0
palavranova = ''

while index < len(palavra):
    if index % 2:
        palavranova += palavra[index]
    index = index + 1
print(f'letras pares:  {palavranova}')