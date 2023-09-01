import nmap
from itertools import product
from halo import Halo
import socket
import netifaces as ni

# Function to generate IP range based on start and end IPs
def generate_ip_range(start, end):
    start = start.split(".")
    end = end.split(".")
    ip_range = []
    for i in product(range(int(start[0]), int(end[0]) + 1),
                     range(int(start[1]), int(end[1]) + 1),
                     range(int(start[2]), int(end[2]) + 1),
                     range(int(start[3]), int(end[3]) + 1)):
        ip_range.append(f"{i[0]}.{i[1]}.{i[2]}.{i[3]}")
    return ip_range

# Function to get the local IP address of the machine
def get_local_ip():
    try:
        # Usually, the default network interface is 'eth0' or 'wlan0'
        local_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
    except:
        try:
            local_ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
        except:
            local_ip = '127.0.0.1'
    return local_ip

if __name__ == '__main__':
    # Get the local IP as the default IP to scan
    local_ip = get_local_ip()

    # Ask user what kind of scan they would like to perform
    scan_type = input("Would you like to scan a range or a single IP address? (Enter 'range' or 'single'): ").lower()

    if scan_type == 'single':
        target_ip = input(f"Enter the target IP address [Default: {local_ip}]: ") or local_ip
        ip_range = [target_ip]
    elif scan_type == 'range':
        start_ip = input("Enter the start IP address [Default: 192.168.1.1]: ") or '192.168.1.1'
        end_ip = input("Enter the end IP address [Default: 192.168.1.255]: ") or '192.168.1.255'
        ip_range = generate_ip_range(start_ip, end_ip)
    else:
        print("Invalid selection. Exiting.")
        exit(1)

    # Initialize terminal spinner
    spinner = Halo(text='Scanning', spinner='dots')
    spinner.start()

    # Initialize and configure nmap scanner
    nm = nmap.PortScanner()

    for ip in ip_range:
        try:
            nm.scan(hosts=ip, arguments='-sn')  # Perform a simple ping scan
            if nm.all_hosts():  # Check if any hosts are up
                for host in nm.all_hosts():
                    print(f"\nHost: {host}")
                    print(f"Hostname: {nm[host].hostname()}")
                    print(f"Hostnames: {nm[host].hostnames()}")
                    print("------------")
        except Exception as e:
            print(f"An error occurred: {e}")

    spinner.stop()

# Note: Make sure you have the proper permissions to scan the target network.
