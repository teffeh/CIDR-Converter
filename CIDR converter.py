import ipaddress
import csv
import os.path
import time

os.path.isfile('data_input_IPV4.csv')
os.path.isfile('data_input_IPV6.csv')

## IPV4 Processing
addresses_v4 = []
addresses_cidr_IPV4 = []
if os.path.isfile('data_input_IPV4.csv'):
    print('IPV4 Running')
    with open('data_input_IPV4.csv','r') as csv_file:
        data = csv.reader(csv_file)
        for line in data:
            ip_address = str(line).strip("'[]")
            for ip in ipaddress.IPv4Network(str(ip_address),False):
                addresses_v4.append(ip)
            first_item = str(addresses_v4[0]).strip("\"'[]")
            last_item = str(addresses_v4.pop()).strip("\"'[]")
            addresses_cidr_IPV4.append(['---RANGE-BEGIN---'])
            addresses_cidr_IPV4.append([first_item])
            addresses_cidr_IPV4.append([last_item])
            addresses_cidr_IPV4.append(['---RANGE-END---'])

            addresses_v4.clear()

            with open ('data_output_IPV4.csv','w',newline='') as new_file:
                csv_writer = csv.writer(new_file,delimiter=',')
                for range in addresses_cidr_IPV4:
                    csv_writer.writerow([str(range).strip("\"'[]")])
    
    print('IPV4 Finished')
addresses_v6 = []
addresses_cidr_IPV6 = []

## IPV6 Processing
if os.path.isfile('data_input_IPV6.csv'):
    print('IPV6 Running')
    with open('data_input_IPV6.csv','r') as csv_file:
        data = csv.reader(csv_file)
        for line in data:
            ip_address = str(line)
            addresses_v6.append(ip_address)
            sanitised = str(addresses_v6[0]).split(":")
            if sanitised[len(sanitised)-1] == "/32']":
                first_item = str(sanitised[0] + ":" + sanitised[1] + ":" + "0000:0000:0000:0000:0000:0000")
                last_item = str(sanitised[0] + ":" + sanitised[1] + ":" + "ffff:ffff:ffff:ffff:ffff:ffff")
            elif sanitised [len(sanitised)-1] == "/64']":
                first_item = str(sanitised[0] + ":" + sanitised[1] + ":" + "0000:0000:0000:0000:0000:0000")
                last_item = str(sanitised[0] + ":" + sanitised[1] + ":" + "0000:0000:ffff:ffff:ffff:ffff")
            else:
                first_item = "invalid bitmask value"
                last_item = "invalid bitmask value"
            addresses_cidr_IPV6.append(['---RANGE-BEGIN---'])
            addresses_cidr_IPV6.append([first_item])
            addresses_cidr_IPV6.append([last_item])
            addresses_cidr_IPV6.append(['---RANGE-END---'])
            addresses_v6.clear()


            with open ('data_output_IPV6.csv','w',newline='') as new_file:
                csv_writer = csv.writer(new_file,delimiter=',')
                for range in addresses_cidr_IPV6:
                    csv_writer.writerow([str(range).strip("\"'[]")])
    print('IPV6 Finished')
