import socket
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Socket created")
    ## should be same network of file 
    ## sender m ip address receiver ka jaega 
    ## or reciever m khud ka aaega 
    ip_add = "192.168.8.197"
    port = 8887
    complete_add = (ip_add,port)
    s.bind(complete_add)
    
    while True:
        message, sender_address = s.recvfrom(1024)  ## 1024 - in general bytes and limit od message 
        
        print("Raw message", message)
        print("sender address", sender_address)
        
        decoded_msg = message.decode("ascii")
        print("Message", decoded_msg)
        
except Exception as e:
    print("An error occurred",e)
