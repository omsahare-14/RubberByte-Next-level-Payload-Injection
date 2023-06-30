import socket

def reverse_tcp(LHOST_IP, LPORT_NUM):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the remote host
        sock.connect((LHOST_IP, LPORT_NUM))
        print(f"Connected to {LHOST_IP}:{LPORT_NUM}!")

        # Start a loop to receive and send data
        while True:
            # Receive data from the remote host
            data = sock.recv(4096)

            if len(data) > 0:
                # Process the received data
                print(f"Received: {data.decode()}")

                # Send a response back to the remote host
                response = "This is a response from the server."
                sock.sendall(response.encode())
    except ConnectionRefusedError:
        print("Connection refused. Make sure the host and port are correct and the server is running.")
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Connection closed.")
    finally:
        # Close the socket
        sock.close()

# # Specify the target host and port
# target_host = '192.168.65.131'
# target_port = 1234

# # Call the function to establish a reverse TCP connection
# reverse_tcp(target_host, target_port)
