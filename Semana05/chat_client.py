import socket
import threading
import sys

if len(sys.argv) != 4:
    print('Argumentos Esperados: IP Porta nome_do_usuario')
    sys.exit(-1)

ip = sys.argv[1]
port = int(sys.argv[2])
nome = sys.argv[3]

# Conectando ao server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_address = (ip, port)
client.connect(sever_address)


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NOME':
                client.send(nome.encode('ascii'))
            else:
                print(message)
        except:
            print("Ocorreu um erro")
            client.close()
            break


# Envia msg para o server
def write():
    while True:
        message = '{}: {}'.format(nome, input(''))
        client.send(message.encode('ascii'))


# Inicializando as threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
