# **AXTOOLKIT**
### *Security Tools Installer for Debian/Ubuntu/Kali Linux*
> *Inspired by Katoolin3, reborn with Python3 — cleaner, modular, extensible*

---

### *✨ Features*

- 🗂️ **12 categories** of security tools (100+ tools)
- ✅ Install / remove individual tools or entire categories
- 🔍 Real-time install status check per tool
- 🌐 Add/Remove Kali Linux APT repositories safely
- 🖥️ Beautiful terminal UI with colors and icons
- 🧩 Fully modular — easy to add new categories/tools
- 📋 System information panel
- 🔄 System update support (apt update & upgrade)

---

### *📋 Requirements*

- Python 3.6+
- Debian / Ubuntu / Kali Linux (or any apt-based distro)
- Root privileges (`sudo`)

---

### *🚀 Usage*

```bash
sudo python3 AXToolkit.py
```

---

### *📁 Project Structure*

```
AXToolkit/
├── AXToolkit.py          # Entry point
├── core/
│   ├── app.py           # Main application controller
│   ├── ui.py            # Terminal UI / colors
│   ├── installer.py     # apt-get wrapper + repo management
│   └── system.py        # System checks and info
├── categories/
│   └── registry.py      # All tool categories and definitions
└── README.md
```

---

### *🗂️ Tool Categories*

| # | Category               | Tools |
|---|------------------------|-------|
| 1 | Information Gathering  | 10    |
| 2 | Vulnerability Analysis | 7     |
| 3 | Web Application        | 10    |
| 4 | Password Attacks       | 7     |
| 5 | Wireless Attacks       | 7     |
| 6 | Exploitation Tools     | 6     |
| 7 | Sniffing & Spoofing    | 8     |
| 8 | Post Exploitation      | 5     |
| 9 | Forensics              | 7     |
|10 | Social Engineering     | 3     |
|11 | Reporting Tools        | 3     |
|12 | Reverse Engineering    | 7     |

---

### *🧩 Adding New Tools*

*Edit `categories/registry.py` and add to the `CATEGORIES` list:*

```python
{
"name": "My Category",
"description": "My custom tools",
"tools": [
{"name": "MyTool", "pkg": "apt-package-name", "desc": "Short description"},
]
}
```

---

### *⚠️ Disclaimer*

*This tool is for ***educational and ethical security testing*** only.*
*Only use on systems you own or have explicit permission to test.*
*The authors are not responsible for any misuse.*

---

### *📜 License*

MIT Indonesia License — Use freely, contribute back!