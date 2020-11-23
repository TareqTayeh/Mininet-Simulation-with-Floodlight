# Mininet + Floodlight

Mininet network simulations with a Software-Defined Networks (SDN) Floodlight controller in a Floodlight VM. The topology created is based on the figure "Topology" found in the figures directory. The ping application, utilizing ICMP, can be used to utilize the sender-to-receiver connection between hosts. The iperf application can generate real-time traffic via TCP or UDP probe packets to collect statistical parameters. There are 3 code files under the code directory:

1. "Custom_topology_code.py" : Code to create the Mininet topolgy with the Floodlight controller.
2. "Ping_QoS_metrics_decode.py" " Code to extract QoS metrics from the output file produced from a ping command.
3. "iPerf_UDP_metrics_decode.py" : Code to extract QoS metrics from the output file produced from a iperf UDP command.