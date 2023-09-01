# Network Topology Mapper

This is a Python-based utility for network topology mapping. It uses Nmap for scanning and is designed to identify hosts in a given IP range or a single IP address. This utility is useful for network administrators and cybersecurity professionals for preliminary network reconnaissance.

## Features

- Scan a range of IP addresses or a single IP address.
- Uses Nmap for ping scans to identify hosts that are up.
- Prints hostnames along with IP addresses.
- Terminal spinner for scan progress.

## Prerequisites

You need to have Python 3.x installed and a couple of Python packages which you can install using `pip`:

```bash
pip install python-nmap
pip install halo
pip install netifaces
````

## Usage

1. Clone this repository or download the script.
2. Run the script in your terminal:

    \```bash
    python network-topology-mapper.py
    ````

3. Follow the on-screen prompts to choose between a range of IPs or a single IP.
4. Wait for the scan to complete. The identified hosts will be printed on the terminal.

## Important Note

Make sure you have the proper permissions to scan the target network. Unauthorized scanning is illegal and unethical.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.