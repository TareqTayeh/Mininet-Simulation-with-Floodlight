# Mininet + Floodlight

Mininet network simulations with a Software-Defined Networks (SDN) Floodlight controller in a Floodlight VM. The topology created is based on the figure `Topology` found below and in the figures directory.

<p align="center">
<img src="https://github.com/TareqTayeh/Mininet-Simulation-with-Floodlight/blob/master/figures/Topology.png" width="400">
</p>

The ping application, utilizing ICMP, can be used to test the sender-to-receiver connection between hosts. The iperf application can generate real-time traffic via TCP or UDP probe packets to collect statistical parameters. There are 3 code files under the code directory:
1. `Custom_topology_code.py`: Creates the Mininet topolgy with the Floodlight controller.
2. `Ping_QoS_metrics_decode.py`: Extracts QoS metrics from the output file produced from a ping command.
3. `iPerf_UDP_metrics_decode.py`: Extracts QoS metrics from the output file produced from a iperf UDP command.

I utilized the ping and iperf commands on each host node separately, after running `mininet> xterm hX hY`, where X and Y denotes the desired host numbers. <br /> <br />
Ping Example: <br />
• H1: ping -w 100 10.0.0.7 | tee Ping_Request_Results.txt <br />
o Ping h7 (10.0.0.7) for 100 s (-w). Output and store results in Ping_Request_Results.txt file (| tee) <br />
• H7: tcpdump host 10.0.0.1 <br />
o Sniff and capture traffic received from h1 (10.0.0.1) <br />
<br />
iPerf Example: <br />
• H1: iperf -c 10.0.0.7 -p 5001 -u -b 6m -t 100 <br />
o Start the UDP (-u) client (-c) at h1 with server ip address (10.0.0.7) and port (-p). Also, set the transmission duration (-t) to 100 seconds and bandwidth to 6Mbps (-b) <br />
• H7: iperf -s -p 5001 -u -i 1 | tee iPerf_UDP_Request_Results.txt <br />
o Start the UDP (-u) server (-s) at h7 with port 5001 (-p). Also, monitor the results every one second (-i). Port 5001 is also the default one from Mininet. Output and store results in iPerf_UDP_Request_Results.txt file (| tee) <br />