import os
import pickle


def listarConsultas():
    if os.path.exists('consultas.bin') and os.path.getsize('consultas.bin') > 0:
        with open('consultas.bin', 'rb') as arq:
            consultas = pickle.load(arq)
    else:
        consultas = []
    return consultas
