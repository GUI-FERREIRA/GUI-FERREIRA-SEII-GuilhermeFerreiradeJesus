#!/usr/bin/python3
import sys
import socket
from threading import Thread

if len(sys.argv)!= 3:
	print('Argumentos esperados: Porta nome_do_arquivo_original')
	sys.exit(-1)

port = int(sys.argv[1])
file_name = sys.argv[2]

# Criando servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', port)
sock.bind(server_address)
sock.listen()

#Lendo arquivo
try:
	dados = open(file_name,'rb').read()
	len_dados = len(dados)
	len_dados = len_dados.to_bytes(length=4, byteorder='big', signed=False)
except Exception as error:
	print(error)
	sys.exit(-1)

def envia_arquivos(conection, client):
	global dados, len_dados
	# enviando arquivo
	conection.send(len_dados)
	conection.send(dados)
	# encerrando a conexão
	conection.close()


def Clients():
	while True:
		conection, client = sock.accept()
		Thread(target=envia_arquivos, args=(conection, client)).start()

Thread(target=Clients,daemon=True).start()


while True:
	saida = input()
	if saida == 'exit':
		break
print('digite "exit" para encerrar')

