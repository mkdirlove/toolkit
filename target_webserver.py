import sys
import os

# ! IMPORTANT !
# Nikto Package needs to be installed on system for this to work.

input_server = sys.argv[1]

def scan():
    cmd = 'nikto -h ' + input_server + ' -p 80'
    os.system(cmd) # no subprocess, as we want to see live output

def main():
    if len(sys.argv) <= 1:
        print('ARGUMENT ERROR:\nUsage: sudo python3 target_server.py -t\n-t targets IP Adress')
        exit(1)
    scan()


if __name__ == '__main__': 
    main()