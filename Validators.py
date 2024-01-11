def validarNome():
    while True:
        nome = input('Digite o nome do paciente: ')
        if (len(nome) < 5):
            print(
                '\nNome muito curto! Insira um nome que contenha ao menos 5 caracteres!')
        else:
            return nome


def validarTelefone():
    while True:
        telefone = input('Digite o telefone do paciente: ')
        if (len(telefone) < 11):
            print(
                '\nTelefone muito curto! Insira um telefone que contenha ao menos 11 caracteres!')
        else:
            ehValido = True
            for digito in telefone:
                if (digito.isdigit() == False):
                    print('\nTelefone Inválido! Insira apenas números!')
                    ehValido = False
            if (ehValido):
                return telefone