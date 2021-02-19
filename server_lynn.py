import socket
import datetime

host_IP="127.0.0.1"
port=65534 #port number found online to fix error
message="EECE350" #message to be echoed
server_address=(host_IP , port) #tuple containing ip address and port number
buffer_size=1024 
my_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #using DGRAM because UDP
my_socket.bind(server_address)#binding step with IP address and port number

while 1:
  data=my_socket.recvfrom(buffer_size)
  now=datetime.datetime.now()
  print("Message recieved at:")
  print(now) #prints the date and time
  if data:#online
      echoed=my_socket.sendto(str.encode(message),data[1])
            

#https://subscription.packtpub.com/book/networking_and_servers/9781786463999/1/ch01lvl1sec16/writing-a-simple-udp-echo-client-server-application
#port number:https://help.socketlabs.com/docs/how-to-fix-error-only-one-usage-of-each-socket-address-protocolnetwork-addressport-is-normally-permitted
#encoding message:http://melardev.com/eng/blog/2017/12/08/python-youtube-playlist/
      
      
      
