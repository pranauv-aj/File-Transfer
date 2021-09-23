import socket as sock
import json
import mimetypes as m
import base64

HOST = "192.168.29.176"
PORT = 9999

sockObj = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
sockObj.setsockopt(sock.SOL_SOCKET,sock.SO_REUSEADDR,1)
sockObj.bind((HOST,PORT))
sockObj.listen(0)
while True:
	conn, addr = sockObj.accept()
	print("Connection Established with {IP}:{Backport}".format(IP=addr[0],Backport=addr[1]))
	path = input("Absolute Path: ")
	choice = input("Sending an Image \n0.No\n1.Yes\n: ")
	if(int(choice) == 1):
		with open(path,'rb') as outFile:
			data = outFile.read()
			imageData = base64.b64encode(data)
			jsonData = json.dumps(imageData)
			break
			
	else:
		with open(path,'r') as outFile:
			data = outFile.read()
			jsonData = json.dumps(data)
			break

conn.sendall(jsonData.encode())