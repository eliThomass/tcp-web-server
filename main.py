from socket import socket, AF_INET, SOCK_STREAM
import sys # In order to terminate the program
import threading as th

def handle_request(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode() # Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        with open(filename[1:], "r") as f: # <- extra line added to auto close file
            outputdata = f.read() #Fill in end
        
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
    except (IOError, IndexError):
        #Send response message for file not found
        #Fill in start 
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())
        #Fill in end
    finally:
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end


# This is for the optional threading exercise
def start_server():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a server socket
    #Fill in start
    port = 4567
    serverSocket.bind(('', port))
    serverSocket.listen(5) # up to 5 connections can listen
    #Fill in end

    print("Listening...\n")

    try:
        while True:
            # Main thread blocks here waiting for a new connection
            connectionSocket, addr = serverSocket.accept()
            print(f"Accepted connection from {addr}")

            # New thread to handle the client
            client_thread = th.Thread(target=handle_request, args=(connectionSocket, addr))
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\nShutting down the server...")
    finally:
        serverSocket.close()
        sys.exit()


if __name__ == "__main__":
    start_server()
