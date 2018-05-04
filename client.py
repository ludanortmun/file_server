import socket
import sys

address = '10.12.41.114'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (address, 3000)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)


message = 'Glass'
coded = message.encode('ascii')
    
sock.send(coded)

sock.close()
print ('closing socket')
    