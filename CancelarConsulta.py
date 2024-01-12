from ListarConsulta import listarConsultas
from Validators import validarNumero
import pickle


def cancelarConsulta():
    consultas = listarConsultas()
    if len(consultas) == 0:
        print('Não há consultas ativas.')
        return

    for index, consulta in enumerate(consultas):
        print(
            f'{index + 1} || Data: {consulta["data"].strftime("%d/%m/%Y")} || Hora: {consulta["hora"]} || Espec: {consulta["especialidade"]} || Usuário: {consulta["usuario"]}')

    while True:
        numero = input("Digite o número da consulta: ")
        if validarNumero(numero) == True:
            numero = int(numero)
            if numero <= len(consultas) and numero > 0:
                break
            print('\nErro! Digite um número válido!')

    print('\nConsulta encontrada!')
    consulta = consultas[numero - 1]
    print(
        f'Data: {consulta["data"].strftime("%d/%m/%Y")} || Hora: {consulta["hora"]} || Especialidade: {consulta["especialidade"]}')
    while True:
        opc = input('Deseja realmente cancelar a consulta? (S/N): ')
        if opc == 'S' or opc == 's':
            consultas.pop(numero - 1)

            with open('consultas.bin', 'wb') as arq:
                pickle.dump(consultas, arq)
            arq.close()
            print('\nConsulta deletada com sucesso!')
            break
        elif opc == 'n' or opc == 'N':
            break
