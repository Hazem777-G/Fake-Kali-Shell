#This file is Safe
#It's for educational purposes
#It's a simulation for kali Linux Terminal
#Still underwork!
#Under Testing!
import sys
import time
import os
import random
import getpass
pkg = ["Soon"]
open_portsG = ["HTTP", "HTTPS", "FTP", "SSH", "Telnet", "SMTP", "DNS", "POP3", "IMAP", "MySQL", "RDP", "HTTP Proxy"]
users = ["normal", "owner", "root"]
errors = ["That's not valid", "Try again commander", "404: Command not found", "Enter a valid command"]
chd = ["Home", "Documents", "Downloads", "Desktop", "Music", "Pictures", "Public", "Templates", "Videos"]
wordlists = ["amas", "brutespray", "dirb", "dirbuster"] #Soon

current_dir = "Home"
file_system = {d: {} for d in chd}
file_system["Desktop"] = {"game.py": "print('Hello World')", "notes.txt": "Important meeting at 3 PM"}

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def download():
    for D in range(1, 101):
        print(f"Downloading[{D}%/100%]")
        time.sleep(0.05)

def nmapW():
    print("#Soon")

def Hydra():
    global cmd 
    parts = cmd.split()

    if "-l" in parts:
        user_index = parts.index("-l") + 1
        if user_index < len(parts):
            user = parts[user_index]
        else:
            print("Missing username after -l")
            return

    elif "-L" in parts:
        users_index = parts.index("-L") + 1
        if users_index < len(parts):
            user_file = parts[users_index]
            print(f"Will read usernames from: {user_file}")
        else:
            print("Missing username file after -L")
            return
    else:
        print("Missing -l or -L for username")
        return

    if "-p" in parts:
        pass_index = parts.index("-p") + 1
        if pass_index < len(parts):
            password = parts[pass_index]
        else:
            print("Missing password after -p")
            return
    elif "-P" in parts:
        pass_file_index = parts.index("-P") + 1
        if pass_file_index < len(parts):
            password_file = parts[pass_file_index]
            print(f"Will read passwords from: {password_file}")
        else:
            print("Missing password file after -P")
            return
    else:
        print("Missing -p or -P for password")
        return

    target = None
    for part in parts:
        if "://" in part:
            target = part
            break
    if not target:
        print("Missing target (e.g. ftp://127.0.0.1)")
        return

    print("Launching Hydra attack simulation...")
    time.sleep(2)

    if "-l" in parts and "-p" in parts:
        print(f"Trying {user}:{password} on {target}... [Success ✅]")
    elif "-L" in parts and "-P" in parts:
        print(f"Brute-forcing multiple usernames and passwords on {target}... [Done ✅]")
    elif "-L" in parts and "-p" in parts:
        print(f"Trying many users with same password '{password}' on {target}... [Done ✅]")
    elif "-l" in parts and "-P" in parts:
        print(f"Trying user '{user}' with many passwords on {target}... [Done ✅]")

ter = input("root or normal?: ").lower().strip()

if ter in users:
    if ter == "root":
        while True:
            password = getpass.getpass("Enter root password: ")
            if password == "KALI":
                break
            else:
                print("Enter the correct password to gain root access.")
elif ter not in users:
    print(f"Access denied. (Invalid user type: {ter})")
    sys.exit()

while True:
    try:
        if ter == "root":
            cmd = input("root@kali:~# ").strip()

            if cmd.startswith("apt install "):
                pkg_name = cmd[11:].strip() or input("Enter pkg name: ")
                download()
                print(f"Package {pkg_name} installed successfully!")

            elif cmd == "exit":
                print("Exiting....")
                time.sleep(0.5)
                sys.exit()

            elif cmd.startswith("nmap www."):
                nmapW()

            elif cmd == "clear":
                clean()
                print("Screen cleared!")
                time.sleep(0.9)
                clean()

            elif cmd == "dirb":
                dom = input("Enter the domain: ").strip()
                if dom.startswith(("http://www.", "https://www.")):
                    txt = input("Enter the txt file path: ").strip()
                    if txt == "/usr/share/wordlists/dirb/common.txt":
                        print("Testing.....")
                        time.sleep(4.5)
                        print(f"Found!\n{dom}/admin")
                    else:
                        print(f"Dictionary not found at {txt}")
                else:
                    print("Invalid domain format. Use http://www. or https://www.")

            elif cmd.startswith("cd "):
                folder = cmd[3:].strip()
                if folder in chd:
                    current_dir = folder
                    print(f"Now you are in {folder}")
                else:
                    print(f"Directory not found: {folder}")

            elif cmd == "Owner?":
                print("The owner is master, Hazem\nThe great")
 
            elif cmd == "ls":
                files = list(file_system.get(current_dir, {}).keys())
                if files:
                    print("\n".join(files))
                else:
                    print(f"{current_dir} is empty.")

            elif cmd.startswith("ls "):
                folder = cmd[3:].strip()
                if folder in chd:
                    files = list(file_system.get(folder, {}).keys())
                    if files:
                        print("\n".join(files))
                    else:
                        print(f"{folder} is empty.")
                else:
                    print(f"No such directory: {folder}")

            elif cmd == "mkdir":
                while True:
                    Ndir_N = input("Enter dir name: ").strip()
                    if Ndir_N:
                        chd.append(Ndir_N)
                        file_system[Ndir_N] = {}
                        print(f"Directory '{Ndir_N}' created.")
                        break
                    else:
                        print("Please enter a valid directory name.")

            elif cmd == "date":
                print(time.ctime())

            elif cmd.startswith("rm -r"):
                delete = cmd[5:].strip()
                if delete in chd:
                    chd.remove(delete)
                    if delete in file_system:
                        del file_system[delete]
                    time.sleep(0.6)
                    print(f"Deleted {delete}.")
                else:
                    print(f"Directory not found: {delete}")

            elif cmd.startswith("hydra"):
                Hydra()

            elif cmd == "ping":
                host = input("Enter host to ping: ").strip()
                print(f"PING {host} (127.0.0.1) 56(84) bytes of data.")
                for i in range(1, 5):
                    print(f"64 bytes from {host}: icmp_seq={i} ttl=64 time={random.uniform(0.1, 1.0):.1f} ms")
                    time.sleep(0.7)
                print(f"\n--- {host} ping statistics ---")
                print("4 packets transmitted, 4 received, 0% packet loss, time 3001ms")
                
            elif cmd == "ifconfig":
                print("eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500")
                print("        inet 192.168.1.100  netmask 255.255.255.0  broadcast 192.168.1.255")
                print("        ether 00:11:22:33:44:55  txqueuelen 1000  (Ethernet)")
                print("        RX packets 1000  bytes 100000 (100.0 KB)")
                print("        TX packets 800  bytes 80000 (80.0 KB)")
                
            elif cmd == "whoami":
                print(f"Current user: {ter}")

            elif cmd == "uname -a":
                print("Linux kali 5.10.0-kali3-amd64 #1 SMP Debian 5.10.13-1kali1 (2021-02-08) x86_64 GNU/Linux")
                
            elif cmd == "pwd":
                print(f"/{current_dir}")
                
            elif cmd.startswith("touch "):
                filename = cmd[6:].strip()
                if filename:
                    file_system[current_dir][filename] = ""
                    print(f"File '{filename}' created in {current_dir}.")
                else:
                    print("Please specify a filename.")

            elif cmd.startswith("cat "):
                filename = cmd[4:].strip()
                if filename in file_system.get(current_dir, {}):
                    content = file_system[current_dir][filename]
                    print(f"Contents of {filename}:\n{content if content else '<EMPTY FILE>'}")
                else:
                    print(f"File not found: {filename}")

            elif cmd.startswith("echo "):
                text = cmd[5:].strip().strip('"')
                if ' > ' in text:
                    parts = text.split(' > ', 1)
                    message = parts[0]
                    filename = parts[1].strip()
                    if filename:
                         file_system[current_dir][filename] = message
                         print(f"Text written to {filename}")
                else:
                    print(text)

            elif cmd.startswith("mv "):
                parts = cmd[3:].split()
                if len(parts) == 2:
                    src, dest = parts
                    if src in file_system.get(current_dir, {}):
                        file_system[current_dir][dest] = file_system[current_dir].pop(src)
                        print(f"Moved {src} to {dest}")
                    else:
                        print(f"Source file not found: {src}")
                else:
                    print("Usage: mv <source> <destination>")

            elif cmd.startswith("cp "):
                parts = cmd[3:].split()
                if len(parts) == 2:
                    src, dest = parts
                    if src in file_system.get(current_dir, {}):
                        file_system[current_dir][dest] = file_system[current_dir][src]
                        print(f"Copied {src} to {dest}")
                    else:
                        print(f"Source file not found: {src}")
                else:
                    print("Usage: cp <source> <destination>")

            else:
                print(random.choice(errors))

        elif ter == "normal":
            cmd = input("user@kali:~$ ").strip()
            if not cmd.startswith("sudo "):
                print("Permission denied. Use 'sudo' for root commands.")
            elif cmd.startswith("sudo apt install "):
                download()
                print("installing...")
                time.sleep(3.2)
                print("installation completed")

        elif ter == "owner":
            cmd = input("Yes, Master:~# ").strip()
            if cmd == "whoami":
                print("You are the master. Hazem")
            elif cmd.startswith("turnmeinto "):
                into = cmd[11:].strip()
                if into in users:
                    ter = into
                    print(f"You are now a {into}")
                else:
                    print("Invalid user type.")

    except KeyboardInterrupt:
        print("\nUse 'exit' command to quit properly.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")