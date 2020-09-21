import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1',5090))

server_socket.listen(10)
print("[+] Listening for connections on 127.0.0.1:5090..")

while True:

    conn, addr = server_socket.accept()

    print("[+] Got a connection from {}".format(addr))

    while True:

        data = conn.recv(1024)
        if(data.decode() == 'bye'): break
        print("[+] Client sent:",data.decode())

        server_data = input("Enter data to send:")
        conn.send(server_data.encode())

    conn.close()
    print("[+] Client disconnected.")



