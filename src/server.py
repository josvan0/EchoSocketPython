import socket


# creates TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binds socket to the address designed
address = ('localhost', 9000)
sock.bind(address)

# prepare socket to listen incoming connections
# number defines max number of connections at same time
sock.listen(1)
print('Listening on', address[0], ':', address[1])

while True:
    print('Waiting...')
    # waits for a connection
    connection, client_address = sock.accept()
    print('Connected:', client_address)

    try:
        while True:
            # receive data in small parts
            data = connection.recv(16)
            # data are received in bytes
            print('Received:', data.decode('utf-8'))
            if data:
                # send a response
                # data must be in bytes
                connection.sendall(data)
            else:
                # end of data
                break

    except Exception as ex:
        print(ex)
    finally:
        # remind always close connections
        connection.close()
