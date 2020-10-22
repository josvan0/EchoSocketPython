import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 9000)
# connect to a socket in address designed
sock.connect(address)
print('Connecting to', address[0], 'on port', address[1])

try:
    data = 'Hello World'
    # encode data to send in bytes
    sock.sendall(data.encode('utf-8'))
    print('Sent:', data)

    received = 0
    expected = len(data)

    while received < expected:
        # receive response from server
        response = sock.recv(16)
        received += len(response)
        print('Response:', response.decode('utf-8'))
finally:
    sock.close()
