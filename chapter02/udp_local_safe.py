import socket
import argparse
from datetime import datetime


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Escuchando en: {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(65535)
        text = data.decode('ascii')
        print('Cliente: {}, dice {!r}'.format(address, text))
        text = 'Longitud de bytes: {}'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('127.0.0.1', port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))

    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')
    sock.send(data)

    data = sock.recv(65535)
    print('The server replied {!r}'.format(data.decode('ascii')))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Protocolo UDP')
    parser.add_argument('role', choices=choices, help='Rol a ejecutar')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port default 1060')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
