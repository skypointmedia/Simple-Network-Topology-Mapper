# Network Topology Mapper

This is a Python-based utility for network topology mapping. It uses Nmap for scanning and is designed to identify hosts in a given IP range or a single IP address. This utility is useful for network administrators and cybersecurity professionals for preliminary network reconnaissance.

## Features

- Scan a range of IP addresses or a single IP address.
- Uses Nmap for ping scans to identify hosts that are up.
- Prints hostnames along with IP addresses.
- Terminal spinner for scan progress.
## 🛠️ Setup

Alright, you're gonna need Python 3.x for this. Don't have it yet? Go get it, champ! Also, make sure you've got `pip` handy. Open your terminal and just blast these commands:

\```bash
pip install python-nmap
pip install halo
pip install netifaces
\```
## 🚀 How to Use

1. Download the script by either cloning this repo or just nabbing the necessary files. No judgment here!
2. Get that terminal window up and run:

\```bash
python3 network-topology-mapper.py
\```

3. Just follow along with the prompts. We'll ask if you wanna scan a bunch of IPs or just focus on one. We got you.
4. Sit back, relax, and watch as we find out who's on your network.
## 🛡️ Be Cool, Be Legal

Listen up, scanning networks you don't have permission for is not cool. Make sure you've got the go-ahead before you start.
## 📜 License

We're under the MIT License. Basically, feel free to do whatever, but don't point fingers at us if something goes south. Check the [LICENSE.md](LICENSE.md) file if you wanna get all formal about it.
