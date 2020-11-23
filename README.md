# Mininet + Floodlight

Mininet network simulations with a Software-Defined Networks (SDN) Floodlight controller in a Floodlight VM. The topology created is based on the figure "Topology" found below and in the figures directory. The ping application, utilizing ICMP, can be used to utilize the sender-to-receiver connection between hosts. The iperf application can generate real-time traffic via TCP or UDP probe packets to collect statistical parameters. There are 3 code files under the code directory:

<img src="https://github.com/TareqTayeh/Mininet-Simulation-with-Floodlight/blob/master/figures/Topology.png" width="400" align="center>

1. "Custom_topology_code.py" : Creates the Mininet topolgy with the Floodlight controller.
2. "Ping_QoS_metrics_decode.py" " Extracts QoS metrics from the output file produced from a ping command.
3. "iPerf_UDP_metrics_decode.py" : Extracts QoS metrics from the output file produced from a iperf UDP command.