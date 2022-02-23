from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Fill in end

    recv = clientSocket.recv(1024).decode()

    # You can use these print statement to validate return codes from the server.
   # print(recv)
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
   #print(recv1)
   # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = 'rikeen.patel@gmail.com\r\n'
    clientSocket.send(mailFromCommand)
    recv1 = clientSocket.recv(1024)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    sendDataCommand = 'Lorem ipsum dolor sit amet.'
   # print(sendDataCommand)
    clientSocket.send(sendDataCommand)
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    messageData = 'Send message data.'
    #print(messageData)
    clientSocket.send(messageData)
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    messageEnd = '\r\n.\r\n'
    clientSocket.send(messageEnd)
    recv1 = clientSocket.recv(1024)
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    sendQuit = 'Quit\n'
    #print(sendQuit)
    clientSocket.send(sendQuit)
    recv1 = clientSocket.recv(1024)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    pass
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')