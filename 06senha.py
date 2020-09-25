def validatePassword(senha):
    valida = 'Senha é Invalida'
    if (any(char.isdigit() for char in senha)) and ((any(not char.isalnum() for char in senha))):

        valida = 'Senha é valida'
    return valida

print(f'A senha é: {validatePassword("Guigo123@") }')