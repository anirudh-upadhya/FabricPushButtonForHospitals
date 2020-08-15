import cv2
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('192.168.1.249', serverPort))
serverSocket.listen(50)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    while True:
        rcv = connectionSocket.recv(1024).decode()
        #print(rcv) #debug instruction
        if rcv == str("Emgency"):
            img = cv2.imread("C:/Users/Anirudh/Documents/SIC/Sem2/InteractiveSystems/Project/Pi/Py/Request.png")
            cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('screen', img)
            cv2.waitKey(1)

        else:
            img = cv2.imread("C:/Users/Anirudh/Documents/SIC/Sem2/InteractiveSystems/Project/Pi/Py/Background.jpg")
            cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('screen', img)
            cv2.waitKey(1)

