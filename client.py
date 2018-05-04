import socket
import sys

# First arg: server ip address
# Second arg: port
address = sys.argv[1]
port = int(sys.argv[2])

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create tuple and print info
server_address = (address, port)
print ('Connecting to server at: %s, port: %s...' % server_address)

# Connect socket
sock.connect(server_address)
print('-- CONNECTED --')

# Start program
while True:
	# Get command and send to server
	print ('Send a command (gimme + filename to copy):')
	message = raw_input()
	coded = message.encode('ascii')
	sock.send(coded)
	
	# Get list of files
	if message == 'ls':
		data = sock.recv(1024)
		print('-- Available files --')
		print(data)

	# Get file and write to local directory under files/
	elif message.split(' ')[0] == 'gimme':
		data = sock.recv(1024)
		name = message.split(' ')[1]
		f = open('files/' + name, "wb")
		f.write(data)
		f.close()

	# Close the socket and quit the program
	elif message == 'quit':
		print('-- CLOSED --')
		sock.close()
		break
    