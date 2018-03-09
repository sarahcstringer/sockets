from socket import *
server_name = 'localhost'
server_port = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
sentence = raw_input('input lowercase sentence: ')
client_socket.send(sentence)
modifiedSentence = client_socket.recv(1024)
print 'from server: ', modifiedSentence
client_socket.close()
