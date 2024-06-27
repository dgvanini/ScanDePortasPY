import socket

ports = [21,22,80,443,445,3306]
site = ".com.br"

for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	client.settimeout(0.1)
	code = client.connect_ex((site, port))
	if code == 0:
		print(port, "OPEN")
