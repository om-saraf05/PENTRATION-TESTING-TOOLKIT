import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    Attempts to connect to a given port on the target host.
    Returns True if the port is open, False otherwise.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            return result == 0
    except socket.error:
        return False

def run_port_scanner(host: str, ports: list[int], threads: int = 10):
    """
    Scans a list of ports on the target host using multithreading.
    """
    print(f"[+] Starting port scan on {host}...")
    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda p: (p, scan_port(host, p)), ports)

    for port, is_open in results:
        if is_open:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

    print(f"[+] Scan complete. Open ports: {open_ports}")
    return open_ports
