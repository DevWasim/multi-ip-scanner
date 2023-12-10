import socket
import termcolor
import os
from tqdm import tqdm
import time
from ascii import print_port_scanner_ascii

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def scan(target, port, progress_bar):
    if output_type == 1:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((target, port))
            
            service_name = socket.getservbyport(port)
            
            banner = sock.recv(1024)
            
            try:
                banner_str = banner.decode('utf-8').strip()
            except UnicodeDecodeError:
                banner_str = "Non-UTF-8 data (binary)"

            banner_lines = banner_str.split('\n')

            formatted_output = "[+] {:>6} {:>12} {:>14} {:>12}         {}".format("Port", port, service_name, termcolor.colored("      Opened", "green"), banner_lines[0])
            print(formatted_output)

            for line in banner_lines[1:]:
                print("{:>54} {}".format("", line))

            sock.close()
        except socket.error:
            formatted_output = "[+] {:>6} {:>12} {:>12}".format("Port", port, termcolor.colored("      Closed", "red"))
            print(formatted_output)
    else:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((target, port))

            service_name = socket.getservbyport(port)

            banner = sock.recv(1024)
            
            try:
                banner_str = banner.decode('utf-8').strip()
            except UnicodeDecodeError:
                banner_str = "Non-UTF-8 data (binary)"

            banner_lines = banner_str.split('\n')

            formatted_output = "[+] {:>6} {:>12} {:>14} {:>12}         {}".format("Port", port, service_name, termcolor.colored("      Opened", "green"), banner_lines[0])
            print(formatted_output)

            for line in banner_lines[1:]:
                print("{:>54} {}".format("", line))

            sock.close()
        except socket.error:
            pass

    progress_bar.update(1)

def scan_target(target, ports):
    print('[+] {:>6} {:>12} {:>14} {:>12} {:>15}'.format("Port", "Port", "Service", "State", "Version"))
    print('-' * 70)  # Separator line
    print('\n' + ' Starting Scan For ' + str(target))
    
    progress_bar = tqdm(total=ports, unit='port', position=0, leave=True, bar_format='{l_bar}{bar}{r_bar}', colour='green')

    for port in range(1, ports + 1):
        scan(target, port, progress_bar)

    progress_bar.close()

clear_terminal()



print_port_scanner_ascii()


targets = input("\n[*] Enter targets to scan (split by comma ,): ")
ports = int(input("[*] How many ports do you want to scan: "))
output_type = int(input(f"{termcolor.colored('[1]', 'red','on_white' , attrs=['bold'])} Scan All Open and Closed Ports  {termcolor.colored('[2]', 'red','on_white', attrs=['bold'])} Scan All Open Ports : "))

if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple targets", 'red'))
    for ip_addr in targets.split(','):
        scan_target(ip_addr.strip(' '), ports)
else:
    scan_target(targets, ports)
