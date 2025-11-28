import sys
from modules import port_scanner, brute_forcer

# Example target function for brute-forcing (replace with real login logic)
def mock_login(username: str, password: str) -> bool:
    """
    Mock login function for demonstration.
    Replace with actual authentication logic for authorized testing.
    """
    return username == "admin" and password == "secret123"

def main():
    print("=== Python Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute-Forcer")
    choice = input("Select module: ").strip()

    if choice == "1":
        target = input("Enter target host (IP or domain): ").strip()
        ports = input("Enter ports to scan (comma-separated, e.g., 21,22,80): ").strip()
        try:
            ports = [int(p) for p in ports.split(",") if p.strip().isdigit()]
        except ValueError:
            print("[ERROR] Invalid port list.")
            sys.exit(1)
        port_scanner.run_port_scanner(target, ports)

    elif choice == "2":
        username = input("Enter username: ").strip()
        wordlist = input("Enter path to password list: ").strip()
        brute_forcer.run_brute_force(username, wordlist, mock_login)

    else:
        print("[ERROR] Invalid choice.")

if __name__ == "__main__":
    main()
