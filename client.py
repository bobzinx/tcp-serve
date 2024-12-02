import socket


host = input("writing the host (ex: localhost ou 192.168.1.1): ")
port = int(input("writing the number of port (ex: 81): "))

try:

    tcp_socket = socket.create_connection((host, port))
    print(f"connecting in serve: {host}:{port}")
    
    try:
        while True:
          
            message = input("Writing message or exit to close : ")
            if message.lower() == 'exit':
                print("closing the cliente.")
                break

         
            data = message.encode('utf-8')
            tcp_socket.sendall(data)
            print("Mensagem send!")
    finally:
        print("Close the socket")
        tcp_socket.close()

except Exception as e:
    print(f"Error at connected in serve {host}:{port}: {e}")
