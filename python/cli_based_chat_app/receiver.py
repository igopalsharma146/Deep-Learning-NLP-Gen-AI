import socket 

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address = "172.20.10.4"               
##sender ke ander hamesha receiver ka ip add aayega aur 
#receiver me khud ka 
port_number = 4999
complete_add = (ip_address,port_number)
s.bind(complete_add)
while True:
    message = s.recv(1024)
    print(message)
    data = message[0]
    data = "\n"
    print(data.encode("ascii"))