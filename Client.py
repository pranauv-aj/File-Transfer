import socket as sock
import base64
import json

def receiveFile(sockObj):
	jsonData = ""
	while True:
		try:
			jsonData = jsonData + sockObj.recv(4096).decode()
			return json.loads(jsonData)
		except ValueError:
			continue

HOST = "192.168.29.176"
PORT = 9999
sockObj = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
sockObj.connect((HOST,PORT))
commonData = receiveFile(sockObj)
choice = input("Receiving an Image\n0.No\n1.Yes\n: ")
if(int(choice) == 1):
	data = base64.b64decode(commonData)
	with open("sample.jpg",'wb') as outFile:
		outFile.write(data)
else:
	data = commonData
	with open("sample.txt",'w') as outFile:
		outFile.write(data)