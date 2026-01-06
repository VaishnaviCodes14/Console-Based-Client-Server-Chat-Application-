import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('192.168.0.123',123))
print("Connected to sever")

while True:
    msg=input("You: ")
    client_socket.send(msg.encode())
    if msg.lower()=="bye":
        break
    server_msg=client_socket.recv(1024).decode()
    print("Server",server_msg)
    if server_msg.lower()=="bye":
        print("Server left the chat")
        break
client_socket.close()
