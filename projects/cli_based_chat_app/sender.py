import socket
try:
    ## creating socket
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  ## DGRAM(datagram) ---> sends the msg through network
    ## AF_INET ---> Use IPv4 addresses for the network connection.
    print("Socket created")
    ip_add = "192.168.8.110"
    port =  8888                ## range from 0 - 65535
    target_add = (ip_add,port)
    message = input("Enter the message : 😂😊🤣😒😁(❁´◡`❁)(●'◡'●)╰(*°▽°*)╯☆*: .｡. o(≧▽≦)o .｡.:*☆(*/ω＼*)(^///^)")
    encoded_msg = message.encode("ascii")
    s.sendto(encoded_msg,target_add)
    print("Message sent successfully")
    s.close()
    
except Exception as e:
    print("An error occurred",e)