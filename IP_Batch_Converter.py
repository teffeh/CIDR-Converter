import ipaddress
import csv
import os.path


## Define lists
addresses = []
addresses_converted = []
batches = []

## Get filename
print("Please provide full path to file to convert, e.g. \"C:/Users/<me>/Documents/myfile.csv\"\n\nIn Windows 11, right click on your target file, select Copy As Path OR left click the target file and press Ctrl+Shift+C:\n")
input_file = input()
input_file = input_file.strip("\"\'")

##Generate output file
def write_output(input):
        with open ('data_output_Full_List.txt','w') as new_file:
            new_file.write('\n'.join(input))

def parse_csv_and_convert_to_valid_ranges(input):
    data = csv.reader(input)
    for line in data:
        ip_input = str(line).strip("'[]")
        if not ip_input == "":
            # Check if individual IP or network
            try:
                ip_input_split = ip_input.split("-")
                addresses_converted.append(str(ip_input_split[0])+"	"+str(ip_input_split[1]))
            except:
                try:
                    ip_input = ipaddress.ip_network(ip_input,False)
                    if (ip_input.version) == 4:
                        addresses_converted.append(str(ip_input.network_address)+"	"+str(ip_input.broadcast_address))
                    if (ip_input.version) == 6:
                        network_address = str(ip_input.exploded).removesuffix("/"+str(ip_input.prefixlen))
                        addresses_converted.append(network_address+"	"+str(ip_input.broadcast_address))
                except:
                    print("Input contains invalid data: " + str(line))    

## IPV4 Processing
if os.path.isfile(input_file):
    print('Running...')
    with open(input_file,'r') as csv_file:
        parse_csv_and_convert_to_valid_ranges(csv_file)
        write_output(addresses_converted)
    print('Finished. Check script folder for output files')
else:
    print("File not found at \""+input_file+"\", please check path")

## Generate output files in chunks of up to 50 addresses
full_list = 'data_output_Full_List.txt'
hold_lines = []
with open (full_list,'r') as text_file:
    for row in text_file:
        hold_lines.append(row)
outer_count = 1
line_count = 0
sorting = True
while sorting:
    count = 0
    increment = (outer_count-1) * 50
    left = len(hold_lines) - increment
    file_name = "data_output_IP_Batch_" + str(outer_count) + ".txt"
    hold_new_lines = []
    if left < 50:
        while count < left:
            hold_new_lines.append(hold_lines[line_count])
            count += 1
            line_count += 1
        sorting = False
    else:
        while count < 50:
            hold_new_lines.append(hold_lines[line_count])
            count += 1
            line_count += 1
    outer_count += 1
    with open(file_name,'w') as next_file:
        for row in hold_new_lines:
            next_file.write(row)
os.remove('data_output_Full_List.txt')
final_input = input("Press any key to exit")