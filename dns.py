import socket
def ip_to_url(ip_addr):
    hostname=socket.gethostbyaddr(ip_addr)
    print(hostname)
def url_to_ip(url):
    ip_address=socket.gethostbyname(url)
    print(ip_address)
while True:
    print("Enter Choice For DNS Lookup")
    print("1. IP to URL")
    print("2. URL to IP")
    ch=int(input())
    if(ch==1):
        ip_addrs=input("Enter an IP Address : ")
        ip_to_url(ip_addrs)
        #print(hostname)
    elif(ch==2):
        domain_name=input("Enter a Domain Name : ")
        url_to_ip(domain_name)
        #print(ip_address)
