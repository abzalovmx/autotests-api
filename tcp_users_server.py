import socket


messages = []

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(10)  # Максимум 10 подключений в очереди
    print("Сервер запущен и ждет подключения клиентов на localhost:12345")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        data = client_socket.recv(1024).decode()
        if data:
            print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

            messages.append(data)

            client_socket.send('\n'.join(messages).encode())

        client_socket.close()

if __name__ == '__main__':
    server()
