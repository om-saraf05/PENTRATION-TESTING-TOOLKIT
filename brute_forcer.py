import time

def run_brute_force(username: str, password_list_path: str, target_function):
    """
    Attempts to brute-force a login function using a password list.
    target_function(username, password) should return True if login is successful.
    """
    try:
        with open(password_list_path, "r", encoding="utf-8") as file:
            passwords = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[ERROR] Password list file not found: {password_list_path}")
        return None

    print(f"[+] Starting brute-force attack on user '{username}' with {len(passwords)} passwords...")

    for attempt, password in enumerate(passwords, start=1):
        if target_function(username, password):
            print(f"[SUCCESS] Password found: '{password}'")
            return password
        else:
            print(f"[{attempt}/{len(passwords)}] Tried: {password}")
        time.sleep(0.1)  # Prevent overwhelming the target

    print("[!] Password not found in list.")
    return None
