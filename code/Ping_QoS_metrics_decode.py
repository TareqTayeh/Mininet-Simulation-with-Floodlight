"""Ping QoS Metrics Extract - Tareq Tayeh

Code that reads a PING output file and extracts all QoS metrics
Inputs: Requires PING output file in same directoy
Outputs: Packet Loss, Total/Min/Avg/Max Latency, Total/Avg Jitter, Throughput parameters and calculations

Command line to run this: 
python "Ping_QoS_metrics_decode.py"
"""
#!/usr/bin/python




#To read PING output file
mylines = []                                                                          # Declare an empty list.
with open ("Ping_Request_Results.txt", 'rt') as myfile:    							  # Open Ping_Request_Results.txt for reading text.
	for myline in myfile:                                                             # For each line in the file,
		mylines.append(myline.rstrip('\n'))                                           # Strip newline and add to list.

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

	
#Packet Loss Metric	  
substr = "packet loss"                                          # "packet loss" substring to search for.
line = findString(substr)
packetsTransm = (line.split('p')[0])                            # Split accordingly to find the packets transmitted value looking for
print("Packets Transmitted = %s" % packetsTransm)
packetsRcvd = (line.split('transmitted, ')[1].split('r')[0])    # Split accordingly to find the packets received value looking for
print("Packets Received = %s" % packetsRcvd)
packetloss = (line.split('%')[0].split(' ')[-1])                # Split accordingly to find the % value looking for
print("Packet Loss is %s%%" % packetloss)

#Latency (Total) Metric
substr = "time "                                   # "time" substring to search for.
line = findString(substr)
latencytotal = (line.split(' ')[-1].split('m')[0]) # Split accordingly to find the total time/latency value looking for
print("\nTotal Latency is %s ms" % latencytotal)

#Latency (Min, Avg, Max) Metric
substr = "rtt"                                     # "rtt" substring to search for.
line = findString(substr)  
latencymin = (line.split('/')[-4].split(' ')[-1])  # Split accordingly to find the min latency value looking for
print("Min RTT Latency is %s ms" % latencymin)
latencyavg = (line.split('/')[-3])                 # Split accordingly to find the avg latency value looking for
print("Avg RTT Latency is %s ms" % latencyavg)     
latencymax = (line.split('/')[-2])                 # Split accordingly to find the max latency value looking for
print("Max RTT Latency is %s ms" % latencymax)     

#Jitter Metric
jitterList = [] #To keep track of all latencies
substr4 = "time="		                           		  # "time=" substring to search for.
for line in mylines:                               		  # Similar to findString function, but without a break if desired line found as we need ALL latency values across all lines, loops keep on executing till exhausted
    index = 0                   
    prev = 0                    
    while index < len(line):
        index = line.find(substr4, index)  
        if index == -1:           
            break                   
        time = float(line.split('=')[-1].split(' ')[-2])  # Split accordingly to find the latency value looking for
        jitterList.append(time)                           # Append latency value to list
        prev = index + len(substr4)       
        index += len(substr4)      
jitter = 0
for i in range(len(jitterList)):                          # To calculate jitter
	jitter += abs(i - i+1)                                # Absolute (Value 1 - Value 2) + Absolute (Value 2 - Value 3) + ... till before last value
print("\nTotal Jitter is %s ms" % jitter)
jitteravg = jitter / len(jitterList)
print("Avg Jitter is %s ms" % jitteravg)

#Throughput (Pre Calculation) Metric
print("\nThroughput is calculated as (Packet Bit Size * Number of Packets) / Total Time")
substr = "bytes from"                                     									# "bytes from" substring to search for.
line = findString(substr)  
packetSize = (line.split(' ')[0])                         									# Split accordingly to find the packet size value looking for
print("Packet Size is %s bytes" % packetSize)
packetBitSize = int(packetSize) * 8                       									# 1 Byte = 8 Bits
print("That is equivalent to %s bits" % packetBitSize)

#Throughput Metric
substr = "packets transmitted"                                                  			# "packets transmitted" substring to search for.
line = findString(substr)		
packetsNumber = (line.split('transmitted, ')[1].split('r')[0])                  			# Split accordingly to find the packets received value looking for
print("Number of packets transmitted is %spackets" % packetsNumber) 
totalTime = int(latencytotal)/1000                                              			# 1000ms = 1s
print("Total time is %s s" % totalTime)
throughput = (float(packetBitSize) * float(packetsNumber)) / float(totalTime)   			# Throughput (bits/s) = (Packet Bit Size * Number of Packets) / Total Time
print("Throughput is %s bits/sec" % throughput)