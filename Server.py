import argparse
from sys import argv
import socket

# First we use the argparse package to parse the arguments
parser = argparse.ArgumentParser(description="""This is a very basic client program""")
parser.add_argument('port', type=int, help='This is the port to connect to the server on', action='store')

args = parser.parse_args(argv[1:])

googleIP = '8.8.8.8'
localPort = 24569

try:
    sockk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('Socket open error: {} \n'.format(err))
    exit()
SERVER = ('', args.port)
sockk.bind((SERVER))
sockk.listen(1)

connection, address = sockk.accept()

#create Socket to communicate with Google
try:
    UDP_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_Socket.bind((googleIP, localPort))
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()


with connection:
    while True:
        data = connection.recv(512)
        data = data.decode('utf-8')
        try:
            UDP_Socket.connect(server_addr2)
            UDP_Socket.sendall(data.encode('utf-8'))
        except:
            UDP_Socket.sendall(line.encode('utf-8'))
        answer = UDP_Socket.recv(512)
        answer = answer.decode('utf-8')



# now we need to open both files
with open(args.out_file, 'w') as write_file:
    for line in open(args.in_file, 'r'):
        # trim the line to avoid weird new line things
        line = line.strip()
        # now we write whatever the server tells us to the out_file
        if line:
            client_sock.sendall(line.encode('utf-8'))
            answer = client_sock.recv(512)

            # decode answer
            answer = answer.decode('utf-8')

            # if hostname wasn't found in RS, string needs to be sent to TS
            if 'NS' in answer:
                server_addr2 = (args.rshost_name, args.tsListen_port)
                try:
                    client_sock2.connect(server_addr2)
                    client_sock2.sendall(line.encode('utf-8'))
                except:
                    client_sock2.sendall(line.encode('utf-8'))
                answer = client_sock2.recv(512)
                answer = answer.decode('utf-8')
                pass

            write_file.write(answer + '\n')


# close the socket (note this will be visible to the other side)
client_sock.close()

for line in open(args.out_file, 'r+'):
    if 'NS' in line:
        line = 'Replace'
    print(line)