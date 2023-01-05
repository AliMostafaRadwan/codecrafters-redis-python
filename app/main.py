# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    
    sock_cl, addr = server_socket.accept()
    while sock_cl:
        data = sock_cl.recv(1024)
        if not data:
            break
        sock_cl.send(data)

if __name__ == "__main__":
    main()
