import socket

#set up a tcp/ip server

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveAdress = ('localhost', 8000)

tcpSocket.bind(serveAdress)

tcpSocket.listen(1)

while True:
    print("waiting for connection")
    connection, client = tcpSocket.accept()

    try:
        print("Connected to client IP : {}".format(client))

        while True:
            data = connection.recv(1024)
            decodedData = data.decode('utf-8')
            print("Received data: {}" .format(decodedData))

            if not data:
                break
    finally:
        connection.close()

    
