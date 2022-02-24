from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    printToggle = 0

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    recv = clientSocket.recv(1024).decode()
    # Fill in end

    # You can use these print statement to validate return codes from the server.
    if printToggle == 1:
        print(recv)
        if recv[:3] != '220':
            print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if printToggle == 1:
        print(recv1)
        if recv1[:3] != '250':
            print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = 'Mail From:<rikeen.patel@gmail.com>\r\n'
    clientSocket.send(mailFrom.encode())
    recvFrom = clientSocket.recv(1024).decode()
    if printToggle == 1:
        print(recvFrom)
        if recv1[:3] != '250':
            print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTo = "RCPT TO: testcase@nyu.edu\r\n"
    clientSocket.send(rcptTo.encode())
    recv2 = clientSocket.recv(1024).decode()
    if printToggle == 1:
        print(recv2)
        if recv2[:3] != '250':
            print('250 reply not received from server.\r\n')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    sendData = "DATA\r\n"
    clientSocket.send(sendData.encode())
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send("To: foo@bar\r\n".encode())
    clientSocket.send("From: foo@bar\r\n".encode())
    clientSocket.send("Subject: My Subject\r\n".encode())
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    if printToggle == 1:
        print(recv5)
        if recv5[:3] != '250':
            print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    clientSocket.send("QUIT\r\n".encode())
    recv6 = clientSocket.recv(1024).decode()
    if printToggle == 1:
        print(recv6)
        if recv6[:3] != '221':
            print('221 reply not received from server.')

    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
