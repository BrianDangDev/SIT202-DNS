import socket
clientAddr = "127.0.0.1"
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (clientAddr, 1234)
userDecision = "Y"
while userDecision.upper() == "Y":
    domain_input = input("Enter domain name for which the IP is needed:")
    send = clientSocket.sendto(domain_input.encode(), addr)
    data, address = clientSocket.recvfrom(1024)
    cname, address = clientSocket.recvfrom(1024)
    server_reply = data.decode().strip()
    cname_reply = cname.decode().strip()
    message = "The IP for the " + format(cname_reply)+" server is " + format(server_reply)
    print(message)
    userDecision = (input("Continue?(y/n)"))
clientSocket.close()
