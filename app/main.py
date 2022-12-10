# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client_connection, client_address = server_socket.accept() # wait for client
    client_connection.recv(4096)
    client_connection.send(bytes('+PONG\r\n', 'UTF-8'))
    

if __name__ == "__main__":
    main()
