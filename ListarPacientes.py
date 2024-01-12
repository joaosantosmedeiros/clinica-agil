import pickle
import os


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