# CIDR, IP range and IP address batch converter

<h3>Prerequisities: Python 3.12.4</h3>

1.  Generate CSV file of values with one network address per row e.g.
<table>
<tr><td>192.168.0.1/24</td></tr>
<tr><td>2400:7aa0::/32</td></tr>
<tr><td>192.168.0.1</td></tr>
<tr><td>192.168.1.68-192.168.1.69</td></tr>
</table>
2. Run IP_Batch_Converter.py with Python (Right click > Open with > Python)<br>
3. Follow instructions in window to copy the path of the CSV file. Paste or type full path and press Enter.<br>
4. In the folder the script is stored in, observe at least one txt file of maximum 50 IP address ranges is generated. This amount of files will scale up to infinity depending on number of input network addresses.<br>
5. Delete/move/archive generated txt files to prevent confusion for next usage <br>


<h3>Download</h3>
<a href = https://github.com/teffeh/CIDR-Converter/releases/latest/download/IP_Batch_Converter.py>Click Here</a>
