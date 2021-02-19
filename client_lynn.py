import socket
import time


host_IP="127.0.0.1"
port=65534 #got this number from a site because of an error
buffer_size=1024
message="EECE350"
my_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #using DGRAM because UDP
server_address=(host_IP , port)
RTT=0.0 #initializing RTT to zero

for i in range (0,5):
        current_time=time.time()
        my_message = my_socket.sendto(str.encode(message), server_address) #(found the idea online)
        data = my_socket.recvfrom(buffer_size)
        RTT= RTT+ (time.time())- current_time
        print("the RTT is:", RTT)


Average=RTT/5 #average rtt
print("Average RTT is:", Average)
my_socket.close()

#https://subscription.packtpub.com/book/networking_and_servers/9781786463999/1/ch01lvl1sec16/writing-a-simple-udp-echo-client-server-application
#port number: https://help.socketlabs.com/docs/how-to-fix-error-only-one-usage-of-each-socket-address-protocolnetwork-addressport-is-normally-permitted
# the encoding idea: http://melardev.com/eng/blog/2017/12/08/python-youtube-playlist/
