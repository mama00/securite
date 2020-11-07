
import socket
import time
port = 6332 
max_hops = 40

def Traceroute(dest_name):  
    dest_addr = socket.gethostbyname(dest_name)
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1
    while True:
        receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) 
        sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp) 

        sending_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl) 
        receiving_socket.bind(("", port)) 
        sending_socket.sendto("testing", (dest_name, port)) 
        
        current_hop = None
        curr_name = None

        try:
            data, current_hop = receiving_socket.recvfrom(512) 
            current_hop = current_hop[0]
            try:
                curr_name = socket.gethostbyaddr(current_hop)[0] 
            except socket.error:
                curr_name = current_hop
        except socket.error: 
            print('timeout error')
        finally:
            sending_socket.close() 
            receiving_socket.close()

        if current_hop is not None: 
            curr_host = "%s (%s)" % (curr_name, current_hop)
        else:
            curr_host = "*" 
        print "%d\t%s" % (ttl, curr_host)

        ttl += 1

        if current_hop == dest_addr or ttl > max_hops: 
            break

if __name__ == "__main__":
    dest_name = raw_input('Enter the destination : ')
    print('Traceroute to {} ({}) on port : {}, {} hops max'.format(dest_name,socket.gethostbyname(dest_name),port,max_hops))
    startTime = time.time() 
    Traceroute(dest_name)