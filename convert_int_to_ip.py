#!/usr/bin/python3
def convert_int_to_ip(number):
    ip=""
    for i in range(4):
            ip1 = ""
            for j in range(8):
                    ip1 = str(number % 2) +ip1
                    number = number >> 1
            ip = str(int(ip1,2)) + "." + ip
    print(ip.strip("."))

convert_int_to_ip(3232235521)
