import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...\n")

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is closed")

        s.close()

if __name__ == "__main__":
    target = "127.0.0.1"
    ports = [21, 22, 80, 443]

    scan_ports(target, ports)