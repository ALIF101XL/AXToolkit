#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
categories/registry.py - Tool category definitions
Each category: name, description, tools list
Each tool: name, pkg (apt package name), desc
"""

CATEGORIES = [
    {
        "name": "Information Gathering",
        "description": "Reconnaissance and OSINT tools",
        "tools": [
            {"name": "Nmap",         "pkg": "nmap",             "desc": "Network discovery and security auditing"},
            {"name": "Maltego",      "pkg": "maltego",          "desc": "OSINT and graphical link analysis"},
            {"name": "Recon-ng",     "pkg": "recon-ng",         "desc": "Full-featured web reconnaissance framework"},
            {"name": "theHarvester", "pkg": "theharvester",     "desc": "Email, domain, host OSINT gatherer"},
            {"name": "DNSRecon",     "pkg": "dnsrecon",         "desc": "DNS enumeration tool"},
            {"name": "Fierce",       "pkg": "fierce",           "desc": "DNS reconnaissance tool"},
            {"name": "Dmitry",       "pkg": "dmitry",           "desc": "Deep Magic Information Gathering Tool"},
            {"name": "Netdiscover",  "pkg": "netdiscover",      "desc": "ARP reconnaissance tool"},
            {"name": "Masscan",      "pkg": "masscan",          "desc": "Mass IP port scanner"},
            {"name": "Amass",        "pkg": "amass",            "desc": "In-depth attack surface mapping"},
        ]
    },
    {
        "name": "Vulnerability Analysis",
        "description": "Scanning and vulnerability assessment tools",
        "tools": [
            {"name": "OpenVAS",      "pkg": "openvas",          "desc": "Open Vulnerability Assessment Scanner"},
            {"name": "Nikto",        "pkg": "nikto",            "desc": "Web server scanner"},
            {"name": "Lynis",        "pkg": "lynis",            "desc": "Security auditing for Unix systems"},
            {"name": "Nessus",       "pkg": "nessus",           "desc": "Comprehensive vulnerability scanner"},
            {"name": "Wapiti",       "pkg": "wapiti",           "desc": "Web application vulnerability scanner"},
            {"name": "SQLMap",       "pkg": "sqlmap",           "desc": "Automatic SQL injection detection"},
            {"name": "Golismero",    "pkg": "golismero",        "desc": "Open source web security testing"},
        ]
    },
    {
        "name": "Web Application Analysis",
        "description": "Web hacking and testing tools",
        "tools": [
            {"name": "Burp Suite",   "pkg": "burpsuite",        "desc": "Web app security testing platform"},
            {"name": "OWASP ZAP",    "pkg": "zaproxy",          "desc": "Web app vulnerability scanner"},
            {"name": "Dirb",         "pkg": "dirb",             "desc": "Web content scanner"},
            {"name": "Gobuster",     "pkg": "gobuster",         "desc": "Directory/file brute-forcer"},
            {"name": "WFuzz",        "pkg": "wfuzz",            "desc": "Web fuzzer"},
            {"name": "Commix",       "pkg": "commix",           "desc": "Command injection exploitation"},
            {"name": "Skipfish",     "pkg": "skipfish",         "desc": "Active web app security recon"},
            {"name": "W3af",         "pkg": "w3af",             "desc": "Web application attack and audit framework"},
            {"name": "WhatWeb",      "pkg": "whatweb",          "desc": "Web fingerprinting tool"},
            {"name": "Wafw00f",      "pkg": "wafw00f",          "desc": "Web Application Firewall detector"},
        ]
    },
    {
        "name": "Password Attacks",
        "description": "Password cracking and brute-force tools",
        "tools": [
            {"name": "Hydra",        "pkg": "hydra",            "desc": "Network logon cracker"},
            {"name": "Hashcat",      "pkg": "hashcat",          "desc": "Advanced password recovery"},
            {"name": "John",         "pkg": "john",             "desc": "John the Ripper password cracker"},
            {"name": "Medusa",       "pkg": "medusa",           "desc": "Parallel password brute-forcer"},
            {"name": "CrackMapExec", "pkg": "crackmapexec",     "desc": "Swiss army knife for networks"},
            {"name": "Ophcrack",     "pkg": "ophcrack",         "desc": "Windows password cracker using rainbow tables"},
            {"name": "Wordlists",    "pkg": "wordlists",        "desc": "Collection of password wordlists"},
        ]
    },
    {
        "name": "Wireless Attacks",
        "description": "Wi-Fi and wireless security tools",
        "tools": [
            {"name": "Aircrack-ng",  "pkg": "aircrack-ng",     "desc": "Wi-Fi network security toolkit"},
            {"name": "Reaver",       "pkg": "reaver",           "desc": "WPS brute-force attack tool"},
            {"name": "Kismet",       "pkg": "kismet",           "desc": "Wireless network detector & sniffer"},
            {"name": "Fern Wifi",    "pkg": "fern-wifi-cracker","desc": "Wireless security auditing tool"},
            {"name": "Wash",         "pkg": "wash",             "desc": "WPS enabled AP scanner"},
            {"name": "Cowpatty",     "pkg": "cowpatty",         "desc": "WPA-PSK dictionary attack tool"},
            {"name": "Pixiewps",     "pkg": "pixiewps",         "desc": "Offline WPS brute-force tool"},
        ]
    },
    {
        "name": "Exploitation Tools",
        "description": "Exploitation frameworks and tools",
        "tools": [
            {"name": "Metasploit",   "pkg": "metasploit-framework", "desc": "World's most popular exploit framework"},
            {"name": "BeEF",         "pkg": "beef-xss",         "desc": "Browser Exploitation Framework"},
            {"name": "Armitage",     "pkg": "armitage",         "desc": "GUI cyber attack manager for Metasploit"},
            {"name": "Exploit-DB",   "pkg": "exploitdb",        "desc": "Exploit database and searchsploit"},
            {"name": "RouterSploit", "pkg": "routersploit",     "desc": "Router exploitation framework"},
            {"name": "Empire",       "pkg": "powershell-empire", "desc": "PowerShell post-exploitation agent"},
        ]
    },
    {
        "name": "Sniffing & Spoofing",
        "description": "Network sniffing and spoofing tools",
        "tools": [
            {"name": "Wireshark",    "pkg": "wireshark",        "desc": "Network protocol analyzer"},
            {"name": "tcpdump",      "pkg": "tcpdump",          "desc": "Command-line packet analyzer"},
            {"name": "Ettercap",     "pkg": "ettercap-graphical","desc": "MITM attack suite"},
            {"name": "Dsniff",       "pkg": "dsniff",           "desc": "Collection of sniffing tools"},
            {"name": "Arpwatch",     "pkg": "arpwatch",         "desc": "ARP traffic monitoring"},
            {"name": "Responder",    "pkg": "responder",        "desc": "LLMNR/NTB-NS poisoner"},
            {"name": "Scapy",        "pkg": "python3-scapy",    "desc": "Packet manipulation library"},
            {"name": "Macchanger",   "pkg": "macchanger",       "desc": "MAC address changer"},
        ]
    },
    {
        "name": "Post Exploitation",
        "description": "Post-exploitation and persistence tools",
        "tools": [
            {"name": "Mimikatz",     "pkg": "mimikatz",         "desc": "Windows credential dumper"},
            {"name": "Weevely",      "pkg": "weevely",          "desc": "PHP web shell manager"},
            {"name": "Backdoor Factory","pkg":"backdoor-factory","desc": "Patch binaries with shellcode"},
            {"name": "Veil",         "pkg": "veil",             "desc": "Antivirus evasion framework"},
            {"name": "Powersploit",  "pkg": "powersploit",      "desc": "PowerShell post-exploitation modules"},
        ]
    },
    {
        "name": "Forensics",
        "description": "Digital forensics and investigation tools",
        "tools": [
            {"name": "Autopsy",      "pkg": "autopsy",          "desc": "Digital forensics platform"},
            {"name": "Binwalk",      "pkg": "binwalk",          "desc": "Firmware analysis tool"},
            {"name": "Bulk Extractor","pkg":"bulk-extractor",   "desc": "High-performance digital forensics"},
            {"name": "Volatility",   "pkg": "volatility",       "desc": "Memory forensics framework"},
            {"name": "Foremost",     "pkg": "foremost",         "desc": "File recovery tool"},
            {"name": "Dc3dd",        "pkg": "dc3dd",            "desc": "Forensic version of GNU dd"},
            {"name": "Exiftool",     "pkg": "libimage-exiftool-perl","desc": "Read/write EXIF metadata"},
        ]
    },
    {
        "name": "Social Engineering",
        "description": "Social engineering and phishing tools",
        "tools": [
            {"name": "SET",          "pkg": "set",              "desc": "Social-Engineer Toolkit"},
            {"name": "Gophish",      "pkg": "gophish",          "desc": "Open-source phishing framework"},
            {"name": "MSFvenom",     "pkg": "metasploit-framework","desc": "Payload generator"},
        ]
    },
    {
        "name": "Reporting Tools",
        "description": "Report generation and documentation tools",
        "tools": [
            {"name": "Dradis",       "pkg": "dradis",           "desc": "Reporting and collab framework"},
            {"name": "Faraday",      "pkg": "python3-faradaysec","desc": "Collaborative penetration test IDE"},
            {"name": "MagicTree",    "pkg": "magictree",        "desc": "Pentest data management tool"},
        ]
    },
    {
        "name": "Reverse Engineering",
        "description": "Disassemblers, debuggers, and RE tools",
        "tools": [
            {"name": "Ghidra",       "pkg": "ghidra",           "desc": "NSA reverse engineering suite"},
            {"name": "Radare2",      "pkg": "radare2",          "desc": "Unix-like RE framework"},
            {"name": "GDB",          "pkg": "gdb",              "desc": "GNU debugger"},
            {"name": "OllyDbg",      "pkg": "ollydbg",          "desc": "x86 Windows debugger"},
            {"name": "Apktool",      "pkg": "apktool",          "desc": "Android APK reverse engineering"},
            {"name": "Jadx",         "pkg": "jadx",             "desc": "Android dex to Java decompiler"},
            {"name": "Strings",      "pkg": "binutils",         "desc": "Extract strings from binaries"},
        ]
    },
]

# Classic tools (like original Katoolin defaults)
CLASSIC_TOOLS = [
    "nmap", "aircrack-ng", "wireshark", "metasploit-framework",
    "burpsuite", "sqlmap", "john", "hydra", "nikto",
    "ettercap-graphical", "recon-ng", "theharvester",
    "dirb", "gobuster", "netdiscover", "tcpdump",
    "binwalk", "foremost", "macchanger", "wordlists",
]


class CategoryRegistry:

    def get_categories(self):
        result = []
        for cat in CATEGORIES:
            result.append({
                "name": cat["name"],
                "description": cat["description"],
                "tools": cat["tools"],
                "count": len(cat["tools"]),
            })
        return result

    def get_all_packages(self):
        pkgs = []
        for cat in CATEGORIES:
            for tool in cat["tools"]:
                pkgs.append(tool["pkg"])
        return list(set(pkgs))  # deduplicate
