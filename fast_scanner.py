import asyncio
import socket
import termcolor
from ascii import print_port_scanner_ascii

async def scan_port(target_ip, port):
    try:
        reader, writer = await asyncio.open_connection(target_ip, port)
        service_name = socket.getservbyport(port)
        
        banner = await asyncio.wait_for(reader.read(1024), timeout=1)
        try:
            banner_str = banner.decode('utf-8').strip()
        except UnicodeDecodeError:
            banner_str = "Non-UTF-8 data (binary)"

        banner_lines = banner_str.split('\n')

        formatted_output = "[+] {:>6} {:>12} {:>14} {:>12}         {}".format(
            "Port", port, service_name, termcolor.colored("      Opened", "green"), banner_lines[0]
        )
        print(formatted_output)

        for line in banner_lines[1:]:
            print("{:>54} {}".format("", line))

        writer.close()
    except (socket.error, asyncio.TimeoutError):
        pass

async def scan_target(target_ip, ports):
    print('[+] {:>6} {:>12} {:>14} {:>12} {:>15}'.format("Port", "Port", "Service", "State", "Version"))
    print('-' * 70)  # Separator line
    print('\n' + ' Starting Scan For ' + str(target_ip))

    tasks = [scan_port(target_ip, port) for port in range(1, ports + 1)]
    await asyncio.gather(*tasks)



target_ip = input("\n[*] Enter target IP to scan: ")
ports = int(input("[*] How many ports do you want to scan: "))


asyncio.run(scan_target(target_ip, ports))
