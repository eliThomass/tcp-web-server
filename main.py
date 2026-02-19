from socket import socket, AF_INET, SOCK_STREAM
import sys # In order to terminate the program


serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
#Fill in start
port = 4567
serverSocket.bind(('', port))
serverSocket.listen(1)
#Fill in end

# I wrapped in try/except block so that I can CTRL-C out of program
try:
    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() # Fill in end
        try:
            message = connectionSocket.recv(1024).decode() # Fill in end
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read() #Fill in end
            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()
        except IOError:
            pass
            #Send response message for file not found
            #Fill in start 
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
            connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
            #Fill in end
            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end
except KeyboardInterrupt:
    print("\nShutting down the server...")
    serverSocket.close()
    # Terminate the program after sending the corresponding data 
    sys.exit()
