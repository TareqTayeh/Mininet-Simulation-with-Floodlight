"""iPerf UDP QoS Metrics Extract - Tareq Tayeh

Code that reads a iPerf UDP output file and extracts all QoS metrics
Inputs: Requires iPerf UDP output file in same directoy
Outputs: Packet Loss, Jitter, Throughput

Command line to run this: 
python "iPerf_UDP_metrics_decode.py"
"""
#!/usr/bin/python




#To read PING output file
mylines = []                                                                          	   # Declare an empty list.
with open ("iPerf_UDP_Request_Results.txt", 'rt') as myfile:    						   # Open iPerf_UDP_Request_Results.txt for reading text.
	for myline in myfile:                                                             	   # For each line in the file,
		mylines.append(myline.rstrip('\n'))                                           	   # Strip newline and add to list.

#Function to find the line of specific substring. 
#Input: Substring to search for in file. 
#Output: Entire line in file.
def findString(substr):
	for line in mylines:
		index = 0
		prev = 0                              # Previous index: last character compared
		while index < len(line):              # While index has not exceeded string length,
			index = line.find(substr, index)  # Set index to first occurrence of "e"
			if index == -1:                   # If nothing was found,
				break                         # Exit the while loop.
			return line                       # Match, return line.

			prev = index + len(substr)        # Remember this position for next loop.
			index += len(substr)              # Increment the index by the length of substr.


#Same substring to search for across all desired QoS Metrics
substr = "0.0-100.0 sec"                           				  		# "0.0-100.0 sec" substring to search for.
line = findString(substr)

#Packet Loss Metric	  
datagramsTotal = (line.split('(')[0].split('/')[-1])					# Split accordingly to find the total datagrams value looking for
print("Datagrams Total = %s" % datagramsTotal)
datagramsLost = (line.split('(')[0].split('/')[-2].split('ms ')[1])		# Split accordingly to find the lost datagrams value looking for
print("Datagrams Lost = %s" % datagramsLost)
packetloss = (line.split('%')[0].split(' ')[-1].split('(')[-1])   		# Split accordingly to find the packet loss % value looking for
print("Packet Loss is %s%%" % packetloss)

#Throughput Metric
throughput = (line.split('Mbits/sec')[0].split('MBytes  ')[-1])			# Split accordingly to find the throughput value looking for
print("\nThroughput is %sMbits/sec" % throughput)

#Jitter Metric
jitter = (line.split('Mbits/sec   ')[1].split(' ms')[0])				# Split accordingly to find the jitter value looking for
print("\nJitter is %sms" % jitter)