import serial
from socket import*

serverName = '192.168.1.249'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.setblocking(1)

ser = serial.Serial("/dev/ttyACM0",9600)
ser.baudrate = 9600


while True:
    read_ser = ser.readline()
    decodedRead = read_ser.decode('utf-8')
    print(decodedRead)
    if decodedRead == str("1\r\n"):
        snd = "Emgency"
    else :
        snd = "NoEmgency"
    print(snd)
    clientSocket.send(str(snd).encode())
    

#clientSocket.close()


