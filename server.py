import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('192.168.0.123',123))
server_socket.listen(10)
print("Server is listening......")
client_socket,client_address=server_socket.accept()
print(f"connected with {client_address} successfully")

while True:
    client_msg=client_socket.recv(1024).decode()
    if client_msg.lower()=="bye":
        print("client left chat")
        break
    print("client",client_msg)
    server_msg=input("You:")
    client_socket.send(server_msg.encode())
    if server_msg.lower()=="bye":
        break
server_socket.close()
client_socket.close()
