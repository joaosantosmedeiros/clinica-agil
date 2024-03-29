from Pacientes import cadastrarPaciente
from Consultas import agendarConsulta, cancelarConsulta

print('________Clínica Ágil!________')
print('O que deseja fazer?')
print('1......... Cadastrar paciente')
print('2........... Agendar Consulta')
print('3........... Deletar consulta')
print('4....................... Sair')
opt = 0
while True:
    try:
        opt = int(input("\nDigite a sua opção: "))
        if (opt == 1):
            cadastrarPaciente()
        if (opt == 2):
            agendarConsulta()
        if (opt == 3):
            cancelarConsulta()
        if (opt == 4):
            break
    except ValueError as e:
        print("Insira um número válido!")
