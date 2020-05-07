import socket
import select
import errno
from UserIdentify_dic import UserIdentify_dic
userdic = UserIdentify_dic()

HEADER_LENGTH = 100

IP = "127.0.0.1"
PORT = 1234
choose = input("login or register: ")
my_username = input("Username: ")
my_password = input("Password: ")
if choose == "register":
    userdic.add_user(my_username, my_password)
elif choose == "login":
    userdic.verify(my_username, my_password)
    
    # Create a socket
    # socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
    # socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # Connect to a given ip and port
    client_socket.connect((IP, PORT))


    # Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
    client_socket.setblocking(False)


    username = my_username.encode('utf-8')
    username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')

    client_socket.send(username_header + username)


    #userdic = UserIdentify_dic()

    #if userdic.verify(my_username, my_password):


    while True:

        # Wait for user to input a message
        message = input(f'{my_username} > ')

        # If message is not empty - send it
        if message:
            # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)

        try:
            # Now we want to loop over received messages (there might be more than one) and print them
            while True:

                # Receive our "header" containing username length, it's size is defined and constant
                username_header = client_socket.recv(HEADER_LENGTH)

                # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
                if not len(username_header):
                    print('Connection closed by the server')
                    sys.exit()

                # Convert header to int value
                username_length = int(username_header.decode('utf-8').strip())

                # Receive and decode username
                username = client_socket.recv(username_length).decode('utf-8')

                # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length).decode('utf-8')

                # Print message
                input(f'COMD: Register | Login: > {message}')
                if message == "Register":
                    input("userName: ")
                    input("userName: ")
                elif message == "Login":
                    input("userName: ")
                    input("userName: ")
                else:
                    input(f'{username} COMD: Register | Login: > {message}')
                print(f'{username} > {message}')




        except IOError as e:

            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

            continue

        except Exception as e:
            print('Reading error: '.format(str(e)))
            sys.exit()

    #    else:
    #        False
