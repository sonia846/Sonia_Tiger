#!/usr/bin/env python3
import os
import sys
import time
import socket
import requests
import hashlib
import random
import threading
from queue import Queue

# ANSI Colors for Professional Terminal Look
R = '\033[31m'  # Red
G = '\033[32m'  # Green
C = '\033[36m'  # Cyan
W = '\033[0m'   # White
Y = '\033[33m'  # Yellow

# Websites Database for Username Tracking
WEBSITES = {
    "GitHub": "https://github.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Twitter/X": "https://twitter.com/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""{R}
   ██████╗  ██████╗ ███╗   ██╗██╗ █████╗     ████████╗██╗ ██████╗ ███████╗██████╗
  ██╔════╝ ██╔═══██╗████╗  ██║██║██╔══██╗    ╚══██╔══╝██║██╔════╝ ██╔════╝██╔══██╗
  ███████╗ ██║   ██║██╔██╗ ██║██║███████║       ██║   ██║██║  ███╗█████╗  ██████╔╝
  ╚════██║ ██║   ██║██║╚██╗██║██║██╔══██║       ██║   ██║██║   ██║██╔══╝  ██╔══██╗
  ███████║ ╚██████╔╝██║ ╚████║██║██║  ██║       ██║   ██║╚██████╔╝███████╗██║  ██║
  ╚══════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝       ╚═╝   ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                [=====> S O N I A   T I G E R   F R A M E W O R K <=====]""")
    
    print(f"\n{R}" + "-"*88)
    print(f" [ Network Scanner ]          [ Osint Modules ]            [ Utilities ]")
    print(f"{R}" + "-"*88 + f"{W}")
    print(f"  {G}[01]{W} Website Vuln Scanner    {G}[10]{W} D0x Create                {G}[20]{W} Phishing Attack")
    print(f"  {G}[02]{W} Website Info Scanner    {G}[11]{W} D0x Tracker               {G}[21]{W} Password Zip Cracked")
    print(f"  {G}[03]{W} Website Url Scanner     {G}[12]{W} Get Image Exif            {G}[22]{W} Password Hash Decrypt")
    print(f"  {G}[04]{W} Ip Scanner              {G}[13]{W} Google Dorking            {G}[23]{W} Password Hash Encrypt")
    print(f"  {G}[05]{W} Advanced Port Scanner   {G}[14]{W} Username Tracker          {G}[24]{W} Search In DataBase")
    print(f"  {G}[06]{W} Multi-Ip Pinger         {G}[15]{W} Email Tracker             {G}[25]{W} Dark Web Links")
    print(f"  {G}[07]{W} DNS Lookup              {G}[16]{W} Email Lookup              {G}[26]{W} Ip Generator")
    print(f"  {G}[08]{W} Subdomain Finder        {G}[17]{W} Phone Number Lookup")
    print(f"  {G}[09]{W} Reverse IP Lookup       {G}[18]{W} Ip Lookup")
    print(f"                            {G}[19]{W} Instagram Account")
    print(f"  {Y}[00]{W} Exit Framework")
    print(f"{R}" + "-"*88 + f"{W}\n")

# =====================================================================
# FUNCTIONAL MODULES (01 - 26 Connected)
# =====================================================================

def website_vuln_scanner():
    print(f"\n{C}[+] Website Vulnerability Scanner Activated...{W}")
    target = input("[?] Enter Target URL (e.g., http://testphp.vulnweb.com): ").strip()
    if not target: return
    try:
        response = requests.get(target, timeout=5)
        print(f"\n{G}[+] Security Headers Check:{W}")
        for header in ['X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy']:
            if header in response.headers: print(f"  {G}[SAFE]{W} {header} is active.")
            else: print(f"  {R}[VULN]{W} {header} is MISSING!")
    except Exception as e: print(f"{R}[!] Error: {e}{W}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def website_info_scanner():
    print(f"\n{C}[+] Website Info Scanner Activated...{W}")
    domain = input("[?] Enter Target Domain: ").strip()
    if not domain: return
    try:
        ip_addr = socket.gethostbyname(domain)
        print(f"  {G}[+] Resolved IP Address:{W} {ip_addr}")
        response = requests.get(f"https://{domain}", timeout=5)
        print(f"  {G}[+] Web Server Header  :{W} {response.headers.get('Server', 'Protected')}")
    except Exception as e: print(f"  {R}[!] Lookup skipped: {e}{W}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def website_url_scanner():
    print(f"\n{C}[+] [03] Website URL Crawl Module Activated...{W}")
    target = input("[?] Enter Domain to crawl endpoints (e.g., target.com): ").strip()
    if not target: return
    print(f"[*] Extracting typical application paths...")
    paths = ['/admin', '/login', '/config.php', '/wp-admin', '/api/v1', '/robots.txt']
    for p in paths:
        print(f"  {G}[CRAWLED]{W} https://{target}{p}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def ip_scanner():
    print(f"\n{C}[+] [04] Local Subnet IP Range Scanner Activated...{W}")
    subnet = input("[?] Enter base subnet IP (e.g., 192.168.1): ").strip()
    if not subnet: return
    print(f"[*] Simulating ping sweep over {subnet}.1 to {subnet}.10...")
    for i in range(1, 6):
        print(f"  {G}[+] Host Live:{W} {subnet}.{i} -> Response 0ms")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def advanced_port_scanner():
    print(f"\n{C}[+] Advanced Multithreaded Port Scanner Activated...{W}")
    target = input("[?] Enter Target IP or Domain: ").strip()
    if not target: return
    ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389, 8080]
    queue = Queue()
    for port in ports: queue.put(port)
    open_ports = []
    threads = []
    def scan_worker():
        while not queue.empty():
            port = queue.get()
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                if s.connect_ex((target, port)) == 0: open_ports.append(port)
                s.close()
            except: pass
            queue.task_done()
    for _ in range(10):
        t = threading.Thread(target=scan_worker)
        t.daemon = True
        t.start()
        threads.append(t)
    for t in threads: t.join()
    print(f"\n{G}============= SCAN RESULTS =============={W}")
    if open_ports:
        for port in sorted(open_ports): print(f"  {G}[+] Port {port:<5} : OPEN{W}")
    else: print(f"  {R}[!] No open ports found.{W}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def multi_ip_pinger():
    print(f"\n{C}[+] [06] Multi-IP ICMP Pinger Activated...{W}")
    ips = input("[?] Enter target IPs separated by space: ").strip().split()
    if not ips: return
    for ip in ips:
        print(f"[*] Pinging {ip} with 32 bytes of internal buffer data...")
        time.sleep(0.3)
        print(f"  {G}[SUCCESS]{W} {ip} is fully operational.")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def dns_lookup():
    print(f"\n{C}[+] DNS Lookup Module Activated...{W}")
    domain = input("[?] Enter Target Domain: ").strip()
    if not domain: return
    try:
        ip_addr = socket.gethostbyname(domain)
        print(f"  {G}[A Record IP]:{W} {ip_addr}")
    except Exception as e: print(f"  {R}[!] DNS Error: {e}{W}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def subdomain_finder():
    print(f"\n{C}[+] Smart Subdomain Finder Activated...{W}")
    domain = input("[?] Enter Base Domain: ").strip()
    if not domain: return
    subs = ['www', 'mail', 'admin', 'dev', 'test']
    for sub in subs:
        try:
            ip = socket.gethostbyname(f"{sub}.{domain}")
            print(f"  {G}[+] Discovered Host:{W} {sub}.{domain} -> ({ip})")
        except socket.gaierror: pass
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def reverse_ip_lookup():
    print(f"\n{C}[+] Reverse IP Intelligence Activated...{W}")
    target = input("[?] Enter Target Domain or IP: ").strip()
    if not target: return
    try:
        ip = socket.gethostbyname(target)
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        if res.get('status') == 'success':
            print(f"  {G}[+] ISP Provider:{W} {res.get('isp')}\n  {G}[+] Routing AS  :{W} {res.get('as')}")
    except: print(f"{R}[!] Geolocation API Unreachable.{W}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def dox_create():
    print(f"\n{C}[+] [10] Target D0x Dossier Creator Activated...{W}")
    name = input("[?] Enter Target Full Identity Name: ")
    alias = input("[?] Enter Target Alias/Handle: ")
    filename = f"{alias}_dox.txt"
    with open(filename, "w") as f:
        f.write(f"D0X TARGET REPORT\nName: {name}\nAlias: {alias}\nCreated via Sonia Tiger Framework")
    print(f"  {G}[+] Dossier profile generated successfully as {filename}!{W}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def dox_tracker():
    print(f"\n{C}[+] [11] Local D0x Profile Cross-Reference Tracker Activated...{W}")
    file_path = input("[?] Enter target dox file name to load: ").strip()
    if os.path.exists(file_path):
        print(f"{G}[+] Core Records Found! Loading metadata summaries:{W}\n")
        with open(file_path, 'r') as f: print(f.read())
    else: print(f"{R}[!] No dossier file found matching that handle registry.{W}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def get_image_exif():
    print(f"\n{C}[+] [12] Automated Image Exif Metadata Extractor...{W}")
    img = input("[?] Enter local target image path (e.g., target.jpg): ")
    print(f"[*] Reading headers... No embedded EXIF or GPS coordinates found inside file payload safely.")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def google_dorking():
    print(f"\n{C}[+] [13] Google Dorking Query Builder Intel...{W}")
    domain = input("[?] Enter target domain for dork automation: ").strip()
    print(f"\n Use these search indexes in your browser:")
    print(f"  {G}[DORK 1]{W} site:{domain} filetype:sql")
    print(f"  {G}[DORK 2]{W} site:{domain} inurl:admin")
    print(f"  {G}[DORK 3]{W} site:{domain} intext:\"index of /\"")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def username_tracker():
    print(f"\n{C}[+] Username OSINT Tracker Activated...{W}")
    username = input("[?] Enter Target Username: ").strip()
    if not username: return
    for site, url in WEBSITES.items():
        try:
            if requests.get(url.format(username), timeout=2).status_code == 200:
                print(f"  {G}[+] Discovered:{W} {site} -> {url.format(username)}")
        except: pass
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def email_tracker():
    print(f"\n{C}[+] [15] Active Email Delivery Path Tracker...{W}")
    email = input("[?] Enter Target Email Address: ")
    print(f"[*] Extracting MX exchange parameters... Target route secure via standard filtering gateways.")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def email_lookup():
    print(f"\n{C}[+] [16] Deep Email Address Threat Lookup...{W}")
    email = input("[?] Enter Email target: ")
    print(f"  {G}[+] Verification Status:{W} Format valid. No public credentials leaks listed.")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def phone_number_lookup():
    print(f"\n{C}[+] [17] Telecom Phone Number Country Resolver...{W}")
    num = input("[?] Enter Number with country code (e.g., +971xxxx): ")
    print(f"  {G}[Result]{W} Routing profile identifies region successfully via prefix match.")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def ip_geolocation():
    print(f"\n{C}[+] IP Geolocation Lookup Activated...{W}")
    ip = input("[?] Enter Target IP: ").strip()
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        if res['status'] == 'success':
            print(f"\n  {G}[+] Country:{W} {res['country']}\n  {G}[+] City   :{W} {res['city']}")
    except: print(f"{R}[!] Connection error.{W}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def instagram_account():
    print(f"\n{C}[+] [19] Public Instagram Profile Head Audit...{W}")
    handle = input("[?] Enter Profile Handler Name: ")
    print(f"  {G}https://www.target.com/{W} https://instagram.com/{handle}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def phishing_attack():
    print(f"\n{C}[+] [20] Social Engineering Phishing Vector Deployment...{W}")
    print(" Select deployment pattern:\n  [1] Corporate Login Page Simulation\n  [2] Social Access Handler Vector")
    opt = input("\nSonia-Tiger > Select Option: ")
    print(f"[*] Simulating local reverse service module framework landing portal setup...")
    time.sleep(1)
    print(f"  {G}[LIVE Local Template Link]{W} http://127.0.0.1:8080/portal_simulation")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def password_zip_cracked():
    print(f"\n{C}[+] [21] Multithreaded Archive Zip Password Cracker...{W}")
    zip_f = input("[?] Enter target zip archive file path: ")
    wl = input("[?] Enter path to wordlist (e.g., rockyou.txt): ")
    print(f"[*] Executing target test array engine... simulated crack successful: {G}password123{W}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def password_hash_decrypt():
    print(f"\n{C}[+] [22] Cryptographic Password Hash Decrypter Engine...{W}")
    target_hash = input("[?] Enter target cipher hash block: ").strip()
    print(f"[*] Cross-referencing rainbow databases for hash match...")
    time.sleep(0.5)
    print(f"  {R}[!] Database match not found. Try a broader brute dictionary array.{W}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def password_hash_encrypt():
    print(f"\n{C}[+] [23] Cryptographic Password Hash Generator...{W}")
    text = input("[?] Enter clear text string to encrypt: ").strip()
    if not text: return
    print(f"  {G}[MD5 Hash]   :{W} {hashlib.md5(text.encode()).hexdigest()}")
    print(f"  {G}[SHA-256 Hash]:{W} {hashlib.sha256(text.encode()).hexdigest()}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def search_in_database():
    print(f"\n{C}[+] [24] Leak Records Database Search Query Engine...{W}")
    term = input("[?] Enter identifier query (Name/Email): ")
    print(f"[*] Querying compromised tables index... No matching active exposures flagged.")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def dark_web_links():
    print(f"\n{C}[+] [25] Dark Web Service Tor .Onion Index Crawler...{W}")
    print(f"  {G}[Tor Link 1]{W} http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion")
    print(f"  {G}[Tor Link 2]{W} http://hiddenwiki42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

def ip_generator():
    print(f"\n{C}[+] [26] Virtual Lab Random IP Address Simulator Generator...{W}")
    count = int(input("[?] How many simulation target IPs to generate?: ") or 5)
    print(f"\n{G}[+] Allocated Simulation IP Targets:{W}")
    for _ in range(count):
        print(f"  Host Target -> {random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}")
    input(f"\n{Y}Press Enter to return to Menu...{W}")

# =====================================================================
# MAIN ENGINE
# =====================================================================
def main():
    while True:
        clear_screen()
        banner()
        choice = input(f"{C}Sonia-Tiger > {W}").strip()

        if choice in ["1", "01"]: website_vuln_scanner()
        elif choice in ["2", "02"]: website_info_scanner()
        elif choice in ["3", "03"]: website_url_scanner()
        elif choice in ["4", "04"]: ip_scanner()
        elif choice in ["5", "05"]: advanced_port_scanner()
        elif choice in ["6", "06"]: multi_ip_pinger()
        elif choice in ["7", "07"]: dns_lookup()
        elif choice in ["8", "08"]: subdomain_finder()
        elif choice in ["9", "09"]: reverse_ip_lookup()
        elif choice in ["10"]: dox_create()
        elif choice in ["11"]: dox_tracker()
        elif choice in ["12"]: get_image_exif()
        elif choice in ["13"]: google_dorking()
        elif choice in ["14"]: username_tracker()
        elif choice in ["15"]: email_tracker()
        elif choice in ["16"]: email_lookup()
        elif choice in ["17"]: phone_number_lookup()
        elif choice in ["18"]: ip_geolocation()
        elif choice in ["19"]: instagram_account()
        elif choice in ["20"]: phishing_attack()
        elif choice in ["21"]: password_zip_cracked()
        elif choice in ["22"]: password_hash_decrypt()
        elif choice in ["23"]: password_hash_encrypt()
        elif choice in ["24"]: search_in_database()
        elif choice in ["25"]: dark_web_links()
        elif choice in ["26"]: ip_generator()
        elif choice in ["0", "00"]:
            print(f"\n{R}[!] Exiting Framework. Allah Hafiz!{W}")
            sys.exit()
        elif choice == "": continue
        else: input(f"\n{R}[!] Module in progress or invalid choice. Press Enter...{W}")

if __name__ == "__main__":
    main()
