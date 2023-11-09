import ipaddress

def subnet_calculator(ip_address, subnet_prefix_length):
    ip=ipaddress.IPv4Address(ip_address)
    subnet_mask=ipaddress.IPv4Network(f'{ip}/{subnet_prefix_length}', strict=False).netmask
    network_address=ipaddress.IPv4Network(f'{ip}/{subnet_mask}', strict=False).network_address
    first_host=network_address+1
    last_host=network_address+(2**(32-subnet_prefix_length))-2
    broadcast_address=network_address+(2**(32-subnet_prefix_length))-1

    first_octet=int(ip_address.split(".")[0])
    if 1<=first_octet<=126:
        ip_class="Class A"
    elif 128<=first_octet<=191:
        ip_class="Class B"
    elif 192<=first_octet<=223:
        ip_class="Class C"
    else:
        ip_class="Reserved Class"
    #Results
    print(f"\nIP Address: {ip}")
    print(f"IP Class: {ip_class}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Network Address: {network_address}")
    print(f"Usable IP Range: {first_host}-{last_host}")
    print(f"Broadcast Address: {broadcast_address}")


def main_menu():
    while True:
        print("Subnetting Menu:")
        print("1.Calculate subnet mask and network inifo")
        print("2.Quit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            ip_address=input("Enter an IP address:")
            subnet_prefix_length=int(input("Enter subnet prefix length:"))
            if 0<=subnet_prefix_length<=32:
                subnet_calculator(ip_address, subnet_prefix_length)
            else:
                print("Invalid subnet prefix length, it should be between0 and 32")
        elif choice==2:
            print("Exiting the program")
            break
        else:
            print("Invalid option")


if __name__=="__main__":
    main_menu()
