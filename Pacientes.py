import pickle
import os
from Validators import validarTelefone, validarNome


def listarPacientes():
    if os.path.exists('pacientes.bin') and os.path.getsize('pacientes.bin') > 0:
        with open('pacientes.bin', 'rb') as arq:
            pacientes = pickle.load(arq)
    else:
        pacientes = []
    return pacientes


def validarPacientes(pacientes):
    if len(pacientes) == 0:
        return False

    for index, paciente in enumerate(pacientes):
        print(
            f'{index + 1} || Nome: {paciente["nome"]} || Telefone: {paciente["telefone"]}')
    return True


def cadastrarPaciente():
    print('Para sair, DIGITE 0 em qualquer um dos campos')
    while True:
        nome = input('Digite o nome do paciente: ')
        if nome == '0':
            return
        if validarNome(nome=nome) == True:
           break
    while True:
        telefone = input('Digite o telefone do paciente: ')
        if telefone == '0':
            return
        if validarTelefone(telefone=telefone):
            break

    if verificarTelefone(telefone=telefone):
        print("\nTelefone já cadastrado! Tente novamente!")
        return

    if os.path.exists('pacientes.bin') and os.path.getsize('pacientes.bin') > 0:
        with open('pacientes.bin', 'rb') as arq:
            pacientes = pickle.load(arq)
    else:
        pacientes = []

    pacientes.append({'nome': nome, 'telefone': telefone})

    with open('pacientes.bin', 'wb') as arq:
        pickle.dump(pacientes, arq)
    print('\nPaciente cadastrado com sucesso!')


def verificarTelefone(telefone):
    try:
        with open('pacientes.bin', 'rb') as arq:
            pacientes = pickle.load(arq)

            for paciente in pacientes:
                if 'telefone' in paciente and paciente['telefone'] == telefone:
                    return True
    except (EOFError, FileNotFoundError) as e:
        pass

    return False


