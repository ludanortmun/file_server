#Necessary for reading directories, files, establishing socket connections and getting console args
import os, socket, sys

#The server IP and port are given as console args
address = sys.argv[1]
port = int(sys.argv[2])

#init socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((address,port))

#accept connections
s.listen(1)
client, clientIp = s.accept()
print ("Got a connection from " + clientIp[0])

#Handle input
msg = ''
while msg != 'quit':
    print ('Waiting input')
    msg = client.recv(1024).decode('ascii')
    print ('Got ' + msg + ' from ' + clientIp[0])

    #Send list of files
    if msg == 'ls':
        files = os.listdir('./files')
        strFiles = ''
        for f in files:
            strFiles += f + '\n'
        client.send(strFiles.encode('ascii'))

    #Send a file
    elif msg.split(' ')[0] == 'gimme':
        fname = 'files/'+msg.split(' ')[1]
        #Check if file exists
        if not os.path.isfile(fname):
            #If not, send text instead
            client.send(('NO SUCH FILE').encode())
            continue
        #Read file and send it
        with open(fname, 'rb') as f:
            data = f.read(1024)
            client.send(data)

#Close connection and exit
client.close()
s.close()
