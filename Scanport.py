import socket


def port_scann(target, ports):
    clcoding = socket.gethostbyname(target)
    print(f"Scanning {target} ({clcoding})")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((clcoding, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()


# Example usage
target = "google.com"
ports = [22, 80, 443, 8080]
port_scann(target, ports)
