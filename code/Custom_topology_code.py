"""
Two sets of switches and hosts (8 hosts and 14 switches) connected as described figure.
Link bandwidth: 15 Mpbs
Link delay: 1ms
Link packet loss: 1%
Floodlight controller connected to all switches.

Adding the 'topos' dict with a key/value pair to generate our newly defined topology enables one to pass in '--topo=mytopo' from the command line.

Command line to run this: 
sudo mn --custom Custom_topology_code.py --topo=mytopo --controller=remote,ip=127.0.0.1,port=6653 --switch ovsk,protocols=OpenFlow13 --link=tc,bw=15,delay=1ms,loss=1 (--test pingall)
"""

from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts, name and numbers correspond exactly to the figure
        leftHost1 = self.addHost( 'h1' )
        leftHost2 = self.addHost( 'h2' )
        rightHost3 = self.addHost( 'h3' )
        rightHost4 = self.addHost( 'h4' )
        rightHost5 = self.addHost( 'h5' )
        rightHost6 = self.addHost( 'h6' )
        rightHost7 = self.addHost( 'h7' )
        rightHost8 = self.addHost( 'h8' )

        # Add switches, name and numbers correspond exactly to the figure
        leftSwitch1 = self.addSwitch( 's1' )
        leftSwitch2 = self.addSwitch( 's2' )
        leftSwitch3 = self.addSwitch( 's3' )
        leftSwitch4 = self.addSwitch( 's4' )
        leftSwitch5 = self.addSwitch( 's5' )
        leftSwitch6 = self.addSwitch( 's6' )
        rightSwitch7 = self.addSwitch( 's7' )
        rightSwitch8 = self.addSwitch( 's8' )
        rightSwitch9 = self.addSwitch( 's9' )
        rightSwitch10 = self.addSwitch( 's10' )
        rightSwitch11 = self.addSwitch( 's11' )
        rightSwitch12 = self.addSwitch( 's12' )
        rightSwitch13 = self.addSwitch( 's13' )
        rightSwitch14 = self.addSwitch( 's14' )

        # Add links
        #Host1 --- Switch1
        self.addLink( leftHost1, leftSwitch1 )
        #Switch1 --- Switch2 & Switch4
        self.addLink( leftSwitch1, leftSwitch2 )
        self.addLink( leftSwitch1, leftSwitch4 )
        #Switch2 --- Switch3 & Switch7
        self.addLink( leftSwitch2, leftSwitch3 )
        self.addLink( leftSwitch2, rightSwitch7 )
        #Switch3 --- Switch5
        self.addLink( leftSwitch3, leftSwitch5 )
        #Switch5 --- Switch6
        self.addLink( leftSwitch5, leftSwitch6 )
        #Switch6 --- Host2
        self.addLink( leftSwitch6, leftHost2 )
        #Switch7 --- Switch8 & Switch9
        self.addLink( rightSwitch7, rightSwitch8 )
        self.addLink( rightSwitch7, rightSwitch9 )
        #Switch8 --- Host3
        self.addLink( rightSwitch8, rightHost3 )
        #Switch9 --- Switch10 & Switch13
        self.addLink( rightSwitch9, rightSwitch10 )
        self.addLink( rightSwitch9, rightSwitch13 )
        #Switch10 --- Switch11 & Host5
        self.addLink( rightSwitch10, rightSwitch11 )
        self.addLink( rightSwitch10, rightHost5 )
        #Switch11 --- Switch12
        self.addLink( rightSwitch11, rightSwitch12 )
        #Switch12 --- Host4
        self.addLink( rightSwitch12, rightHost4 )
        #Switch13 --- Switch14 & Host6
        self.addLink( rightSwitch13, rightSwitch14 )
        self.addLink( rightSwitch13, rightHost6 )
        #Switch14 --- Host7 & Host8
        self.addLink( rightSwitch14, rightHost7 )
        self.addLink( rightSwitch14, rightHost8 )


topos = { 'mytopo': ( lambda: MyTopo() ) }