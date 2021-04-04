#!/usr/bin/python3
import sys
import socket

if len(sys.argv)!= 4:
	print('Argumentos esperados: IP Porta nome_do_arquivo_destino')
	sys.exit(-1)

ip = sys.argv[1]			 #Endereco IP
port = int(sys.argv[2])		 #Porta do Servidor
file_name = sys.argv[3]



# Cria um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Dados para a conexão com o servidor
sever_address = (ip, port)
sock.connect(sever_address)


# receber dados
len_dados = sock.recv(4)
len_dados = int.from_bytes(len_dados, byteorder='big', signed=False)
dados = sock.recv(len_dados)

# Tentando salvar arquivos
try:
	open(file_name, 'wb').write(dados)
except Exception as erro:
	print(erro)
	sys.exit(-1)

print('finalizando a conexão...')
sock.close()
