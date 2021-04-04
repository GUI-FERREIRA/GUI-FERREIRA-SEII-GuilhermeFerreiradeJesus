import socket
import threading
import sys

if len(sys.argv) != 2:
    print('Argumentos esperados: Porta')
    sys.exit(-1)

host = 'localhost'
port = int(sys.argv[1])

# Criando servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', port)
server.bind(server_address)
server.listen()

# Lista para os clients e os nomes
clients = []
nomes = []


# Mandar msg para todos o clients conectados
def broadcast(message):
    for client in clients:
        client.send(message)


# trantando as mensagens dos clientes
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # removendo clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nome = nomes[index]
            broadcast('{} left!'.format(nome).encode('ascii'))
            nomes.remove(nome)
            break


def receive():
    while True:
        # Conexão aceita
        client, address = server.accept()
        print("Conectado com: {}".format(str(address)))

        # Solicitar e armazenar o nome
        client.send('NOME'.encode('ascii'))
        nome = client.recv(1024).decode('ascii')
        nomes.append(nome)
        clients.append(client)

        # Printar nome
        print("Nome: {}".format(nome))
        broadcast("{} Entrou!".format(nome).encode('ascii'))
        client.send('Conectado ao servidor!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
