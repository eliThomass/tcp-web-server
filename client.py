from sys import argv
from socket import socket, AF_INET, SOCK_STREAM

def start_client_http():
    if len(argv) != 4:
        print("Incorrect argv amount")
        return

    server_host = argv[1]
    server_port = int(argv[2])
    filename = argv[3]
    
    # Set up socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    try:
        # Connect to our server and send an HTTP request
        clientSocket.connect((server_host, server_port))
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\nConnection: close\r\n\r\n"
        clientSocket.send(request.encode())
        print(f"Requesting {filename} from {server_host}:{server_port}\n")
        
        # The response of the server is handled and decoded
        response = bytes()
        while True:
            data = clientSocket.recv(4096)
            if not data:
                break
            response += data
        print(response.decode())

    # Error handling
    except ConnectionRefusedError:
        print("Server not running or incorrect info")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # We need to close the socket after everything
        clientSocket.close()

if __name__ == "__main__":
    start_client_http()
