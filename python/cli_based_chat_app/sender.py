import socket 

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip_address = "192.168.70.76"
    port_number = 5050                           ##0 - 65536

    target_add = (ip_address,port_number)
    message = input("Enter message here --->")
    encripted_message = message.encode("ascii")
    s.sendto(encripted_message,target_add)

except Exception as e:
    print("msg not sent ")