import cv2
import socket
import pickle
import struct
from time import sleep


# Configura o endereço e a porta do servidor de destino
host = '35.188.222.230'  # Substitua pelo IP público ou nome de domínio do computador de destino
port = 10629

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

RTSP_URL = f'rtsp://admin:DataAmbient777@192.168.88.11:554/cam/realmonitor?channel=1&subtype=0'
cap = cv2.VideoCapture(RTSP_URL)

while True:
    ret, frame = cap.read()
    data = pickle.dumps(frame)
    message = struct.pack("Q",len(data))+data
    
    client_socket.sendall(message)
    sleep(0.5)

cap.release()
client_socket.close()
