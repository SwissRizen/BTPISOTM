# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:42:35 2021

@author: Nils
"""
import bluetooth






def goright():
    print("I'm going right")
    
def goleft():
    print("I'm going left")
    
def forward():
    print("I'm vrroooming forward")
    
def back():
    print("BEEEP BEEEEEEP BEEEEEEEEP")
    


hostMACAddress = 'XX:XX:XX:XX:XX:XX' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 9
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        if data == 'GO-RIGHT':
            goright()
            client.send('Done Right')
        elif data == 'GO-LEFT':
            goleft()
            client.send('Done left')
        elif data == 'FORWARD':
            forward()
            client.send('Done forward')
        elif data == 'BACKWARD':
            back()
            client.send('Done back')
        else:
            print(data)
            client.send(data) # Echo back to client
except:	
    print("Closing socket")
    client.close()
    s.close(
