import socket
import time

# Port Scanner Function
def port_scanner():
    target = input("Enter target IP address (e.g. 127.0.0.1): ")
    start_port = int(input("Enter start port (e.g. 1): "))
    end_port = int(input("Enter end port (e.g. 1024): "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        s.close()

    print("\nScan complete.\n")

# Brute-Force Password Tester Function
def brute_force():
    username = input("Enter username to test: ")
    real_password = input("Set the correct password (for testing): ")

    # A small test password list
    passwords = ["admin", "1234", "password", "admin123", "letmein", real_password]

    print(f"\nStarting brute-force on username '{username}'...\n")

    for pwd in passwords:
        print(f"Trying password: {pwd}")
        time.sleep(0.5)
        if pwd == real_password:
            print(f"\n✅ Password found: '{pwd}' for user '{username}'\n")
            return
    print("\n❌ Password not found in the list.\n")

# Main Toolkit Menu
def main():
    while True:
        print("==== Penetration Testing Toolkit ====")
        print("1. Port Scanner")
        print("2. Brute-Force Tester")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            port_scanner()
        elif choice == "2":
            brute_force()
        elif choice == "3":
            print("Exiting Toolkit.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
