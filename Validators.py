from datetime import datetime


def validarNome(nome):
    if (len(nome) < 5):
        print(
            '\nNome muito curto! Insira um nome que contenha ao menos 5 caracteres!')
        return False
    return True


def validarTelefone(telefone):
    if len(telefone) < 11:
        print(
            '\nTelefone muito curto! Insira um telefone que contenha ao menos 11 caracteres!')
        return False
    for digito in telefone:
        if digito.isdigit() == False:
            print('\nTelefone Inválido! Insira apenas números!')
            return False
    return True


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


def validarNumero(numero):
    for caracter in numero:
        if caracter.isdigit() == False:
            print('\nErro! Digite um número válido!')
            return False
    return True
