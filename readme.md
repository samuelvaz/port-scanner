
# Network Port Scanner

This Python script allows you to scan open ports on a target host within a specified port range. 

## Disclaimer
This network port scanning script is provided for educational purposes only. It is a basic port scanner with no advanced functionalities and should be used only for educational purposes. The author shall not be held responsible for any misuse or unauthorized access to computer systems. It is crucial to ensure that you have explicit permission to scan and test the security of any network or system.

**Usage of this script for malicious purposes is strictly prohibited.**
By using this script, you acknowledge that you are solely responsible for complying with applicable laws and regulations. The author disclaims any liability for any damages or legal consequences resulting from the misuse of this script.
Use it responsibly and in accordance with ethical standards.


## Usage

```bash
python scanner.py <ip_address> <start_port> <end_port>
```

Example:

```bash
python scanner.py 127.0.0.1 1 100
```

## Script Overview

The script uses the Python `socket` module to perform a port scan on the specified target host. It takes three command-line arguments:

1. `<ip_address>`: The IP address of the target host.
2. `<start_port>`: The starting port number for the scan.
3. `<end_port>`: The ending port number for the scan.

## How it works

1. Resolves the target hostname to an IP address using `socket.gethostbyname`.
2. Iterates over the specified port range and attempts to connect to each port using a TCP socket.
3. Prints information about open ports.
4. Handles exceptions for keyboard interrupts, hostname resolution errors, and general socket errors.

## Example

```bash
--------------------------------------------------
Scanning Target Host: 127.0.0.1
Time started: <current_timestamp>

Port 22: Open
Port 80: Open
...

Found 5 open ports

--------------------------------------------------
```

## Notes

- The script uses a default timeout of 1 second for each port connection attempt.
- It displays the total number of open ports found during the scan.



