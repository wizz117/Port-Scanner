import socket
import  termcolor



def scan_port(ipaddress, port):
        try:
                sock = socket.socket()
                sock.connect((ipaddress, port))
                print("[+] Port Opened " + str(port))
                sock.close()
        except:
                pass


def scan(target, ports):
        print("\n" + " Starting scan for " + str(target))
        for port in range(1, ports):
                scan_port(target, port)



targets = input("[*] Enter Targets to Scan ( split using (,) ): ")
Port_Question = input("Do you want to scan a specific port ([Y] or [N]): ")
if Port_Question == "Y":
    port = int(input("Which port do you want to Scan: "))
    if ',' in targets:
        print("[*] Scanning Multiple Targets")
        for ip_addr in targets.split(','):
                scan_port(ip_addr.strip(' '),port)
    else:
        scan_port(targets,port)
else:
    ports = int(input("[*] Enter How Many Ports Do You Want to Scan: "))
    if ',' in targets:
        print("[*] Scanning Multiple Targets")
        for ip_addr in targets.split(','):
                scan(ip_addr.strip(' '),ports)
    else:
        scan(targets,ports)



