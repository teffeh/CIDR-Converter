import ipaddress

import csv

 

addresses_v4 = []

addresses_cidr = []

with open('data_input.csv','r') as csv_file:

    data = csv.reader(csv_file)

    for line in data:

        ip_address = str(line).strip("'[]")

        for ip in ipaddress.IPv4Network(str(ip_address),False):

            addresses_v4.append(ip)

        first_item = str(addresses_v4[0])

        last_item = str(addresses_v4[len(addresses_v4)-1])

        addresses_cidr.append(first_item + "-" + last_item)

        addresses_v4.clear()

 

with open ('data_output.csv','w') as new_file:

    csv_writer = csv.writer(new_file)

    for range in addresses_cidr:

        csv_writer.writerow([range])

 

#print(addresses_cidr[0])