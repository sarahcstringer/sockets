import socket
server_port = 12000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print 'Server ready to receive'
while 1:
    connection_socket, add = server_socket.accept()
    sentence = connection_socket.recv(1024)
    print 'received data'
    capitalized_sentence = sentence.upper()
    connection_socket.send(capitalized_sentence)
    connection_socket.close()