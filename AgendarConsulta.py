from datetime import datetime, date
import pickle
import os
from Validators import validarData, validarHora, validarNumero
from ListarPacientes import listarPacientes, validarPacientes


def agendarConsulta():
    pacientes = listarPacientes()
    if validarPacientes(pacientes=pacientes) == False:
        print('Não é possível cadastrar consultas caso não existam pacientes cadastrados.')
        return

    while True:
        usuario = input("\nDigite o número do usuário: ")
        if validarNumero(numero=usuario) == True:
            usuario = int(usuario)
            if usuario <= len(pacientes) and usuario > 0:
                break
        print('Erro! Insira um número de usuário válido!')

    while True:
        hora = input("Digite o horário da consulta no formato XX: ")
        if validarHora(hora=hora):
            hora = int(hora)
            break
        print("Digite uma hora válida entre 00 e 23!\n")

    while True:
        data = input("Digite a data da consulta: ")
        ehValida = validarData(data)
        if (ehValida):
            especialidade = input("Digite a especialidade da consulta: ")
            data = formatarData(data=data)

            if os.path.exists('consultas.bin') and os.path.getsize('consultas.bin') > 0:
                with open('consultas.bin', 'rb') as arq:
                    consultas = pickle.load(arq)
                arq.close()
            else:
                consultas = []

            if verificarConsulta(hora=hora, data=data):
                print("Horário já preenchido! Tente novamente.\n")
                return

            consultas.append(
                {'data': data, 'especialidade': especialidade, 'hora': hora, 'usuario': usuario})

            with open('consultas.bin', 'wb') as arq:
                pickle.dump(consultas, arq)

            print('\nConsulta cadastrado com sucesso!')
            arq.close()
            break
        print('Insira uma data válida!\n')


def verificarConsulta(hora, data):
    try:
        with open('consultas.bin', 'rb') as arq:
            consultas = pickle.load(arq)

            for consulta in consultas:
                if consulta['hora'] == hora and consulta['data'] == data:
                    return True
    except (EOFError, FileNotFoundError) as e:
        pass

    return False


def formatarData(data):
    [dia, mes, ano] = (data.split("/"))
    return datetime(int(ano), int(mes), int(dia))
