# Mininet + Floodlight

Mininet network simulations with a Software-Defined Networks (SDN) Floodlight controller in a Floodlight VM. The topology created in this repo is based on the figure `Topology` found below and in the `figures` directory.

<p align="center">
<img src="https://github.com/TareqTayeh/Mininet-Simulation-with-Floodlight/blob/master/figures/Topology.png" width="400">
</p>

The Python code `Custom_topology_code.py` to create this topology is found under the `code` directoy. The command to run this `sudo mn --custom Custom_topology_code.py --topo=mytopo --controller=remote,ip=127.0.0.1,port=6653 --switch ovsk,protocols=OpenFlow13 --link=tc,bw=15,delay=1ms,loss=1`. <br />
--custom Assignment_4_topology_code.py: Runs the custom Mininet topology python code. <br />
--topo=mytopo: Topology name to be built and created. Name specified in my python code (last line). <br />
--controller=remote,ip=127.0.0.1,port=6653: Specifies the use of a remote controller with that IP address and port, which is Floodlight in our case. <br />
--switch ovsk,protocols=OpenFlow13: Specifies the use of the OVSKernel switch and OpenFlow v1.3 switch protocol. <br />
--link=tc,bw=15,delay=1ms,loss=1: Makes links TCLinks with every link having a bandwidth of 15Mpbs, delay of 1ms, and a packet loss of 1%. <br />

### Ping + iPerf
The ping application, utilizing ICMP, can be used to test the sender-to-receiver connection between hosts. The iperf application can generate real-time traffic via TCP or UDP probe packets to collect statistical parameters. I utilized the ping and iperf commands on each host node separately when the network is created and is fully functional, after running `mininet> xterm hX hY`, where X and Y denotes the desired host numbers. <br /> <br />
Ping Example: <br />
h1 will ping h7, and h7 will tcdump. tcpdump is a unix command-line tool for packet sniffing and capturing, we will use it to capture traffic in the emulated network for stats and verification. <br />
• H1: ping -w 100 10.0.0.7 | tee Ping_Request_Results.txt <br />
o Ping h7 (10.0.0.7) for 100 s (-w). Output and store results in Ping_Request_Results.txt file (| tee) <br />
• H7: tcpdump host 10.0.0.1 <br />
o Sniff and capture traffic received from h1 (10.0.0.1) <br />
<br />
iPerf Example: <br />
H1 will act as the client, and H7 will act as the server. <br />
• H1: iperf -c 10.0.0.7 -p 5001 -u -b 6m -t 100 <br />
o Start the UDP (-u) client (-c) at h1 with server ip address (10.0.0.7) and port (-p). Also, set the transmission duration (-t) to 100 seconds and bandwidth to 6Mbps (-b) <br />
• H7: iperf -s -p 5001 -u -i 1 | tee iPerf_UDP_Request_Results.txt <br />
o Start the UDP (-u) server (-s) at h7 with port 5001 (-p). Also, monitor the results every one second (-i). Port 5001 is also the default one from Mininet. Output and store results in iPerf_UDP_Request_Results.txt file (| tee) <br />

There are 2 code files under the code directory that can help with extracting the QoS metrics from those output files:
1. `Ping_QoS_metrics_decode.py`: Extracts QoS metrics from the output file produced from a ping command.
2. `iPerf_UDP_metrics_decode.py`: Extracts QoS metrics from the output file produced from a iperf UDP command.