from datetime import datetime, date 

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


def validarHora(hora):
    if len(hora) > 2 or len(hora) < 1:
        return False
    for caracter in hora:
        if caracter.isdigit() == False:
            return False
    hora = int(hora)
    if hora < 0 or hora > 23:
        return False
    return True


def validarData(data):
    if data.count("/") < 2:
        return False
    [dia, mes, ano] = (data.split("/"))

    for caracter in dia:
        if caracter.isdigit() == False:
            return False
    dia = int(dia)

    for caracter in mes:
        if caracter.isdigit() == False:
            return False
    mes = int(mes)

    for caracter in ano:
        if caracter.isdigit() == False:
            return False
    ano = int(ano)

    try:
        datetime(ano, mes, dia)
    except ValueError:
        return False

    if ano < datetime.now().year:
        return False
    if ano == datetime.now().year:
        if mes < datetime.now().month:
            return False
        if mes == datetime.now().month:
            if dia < datetime.now().day:
                return False
    
    return True


def validarUsuario(usuario):
    for caracter in usuario:
            if caracter.isdigit() == False:
                print('Erro! Digite um número válido!')
                return False
    return True
    