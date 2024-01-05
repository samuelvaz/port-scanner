#! /bin/python

import sys
import socket 
from datetime import datetime

if len(sys.argv) == 4:
    target = socket.gethostbyname(sys.argv[1])
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    print("-" * 50)
    print("Scanning Target Host: {} from port {}-{}".format(target, start_port, end_port))
    time_started = datetime.now()
    print("Time started: " + str(time_started) + "\n")
    
    try: 
        total_open_ports = 0
        for port in range(start_port, end_port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                print("Port {}: Open".format(port))
                total_open_ports = total_open_ports + 1
            s.close()
        time_end = datetime.now()
        time_difference = (time_end - time_started).total_seconds()
        print("\nFound {} open ports".format(total_open_ports))
        print("Scanned \"{}\" in {} seconds".format(target, time_difference))
        print("-" * 50)
        sys.exit()
    
    except KeyboardInterrupt:
        print("\nKeyboard Interrupted: Exiting Program")
        print("-" * 50)
        sys.exit()
    
    except socket.gaierror:
        print("\nHostname Error: Hostname couldn\'t be resolved")
        print("-" * 50)
        sys.exit()
    
    except socket.error:
        print('\nCouldn\'t connect to ther sever')
        sys.exit()
    print("-" * 50)
    
else:
    print("-" * 50)
    print("Error: Invalid arguments")
    print("Valid format: scanner.py <ip_address> <start_port> <end_port> \n >> scanner.py 127.0.0.1 1 999")
    print("Time: " + str(datetime.now()))
    print("-" * 50)





    