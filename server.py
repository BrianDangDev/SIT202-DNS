import socket
dns_table = {"www.google.com": "192.168.1.1",
             "www.deakin.com": "192.168.1.2",
             "www.instagram.com": "192.168.1.3",
             "www.linkedin.com": "192.168.1.4"}

cname_record={"www.google.com": "host.google.com",
              "www.deakin.com": "host.deakin.com",
              "www.instagram.com": "host.instagram.com",
              "www.linkedin.com": "host.linkedin.com"}
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server is running")
clientSocket.bind(("127.0.0.1", 1234))
while True:
    data, address = clientSocket.recvfrom(1024)
    message = format(address) + " request to fetch data "
    print(message)
    data = data.decode()
    ip = dns_table.get(data, "Data not found").encode()
    cname = cname_record.get(data,"none").encode()
    send = clientSocket.sendto(ip, address)
    send1 = clientSocket.sendto(cname,address)
