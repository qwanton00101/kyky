import socket

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.0.10', 12345))

    while True:
        data = client_socket.recv(1024)
        print(data.decode())
        
        message = input("Введите сообщение (или 'exit' для выхода): ")
        if message.lower() == 'exit':
            break

        client_socket.sendall(message.encode())

    client_socket.close()

if __name__ == "__main__":
    client_program()


