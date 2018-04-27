from socket import *
#Creat Socket and Port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6699
serverSocket.bind(("127.0.0.1", serverPort))
serverSocket.listen(1)

#Main Server works
while True:
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	print(connectionSocket)
	try:
		message =  connectionSocket.recv(1024)
		#Analyse the request
		print (message)
		filename = message.split()[1]
		#Open the file in local
		f = open(filename[1:],'rb')
		outputdata = f.read()
		f.close()
		#Analyse the type of the file
		name=filename.split("/")[-1]
		type=name.split(".")[1]
		if type== 'html':
			contenttype='text/html;charset=utf-8'
		if type== 'css' :
			contenttype='text/css'
		if type== 'png' :
			contenttype='image/png'
		#Creat the package
		header=('HTTP/1.1 200 OK \r\n Content-Type:'+contenttype+'\r\n\r\n').encode('utf-8')
		#Combine the header and data
		context = header + outputdata
		connectionSocket.sendall(context)

		connectionSocket.close()
	#Error response
	except IOError:

		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")

		connectionSocket.close()
