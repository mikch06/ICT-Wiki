# Init7 - Hybrid7 connection with Opnsense Firewall
<!-- date: 2020-07-17 00:00:00 -->
<!-- category: opnsense -->
<!-- tags: Init7, Hybrid7 -->
***

If you're using <a href="https://www.init7.net">Init7</a> - Hybrid7 you have to configure pppoe Authentication and VLAN tagging:<br><br>
<b>Opnsense config step by step:</b>
1) VLAN (11) Interface creation:<br><br>
Interfaces → Other Types → VLAN<br><br>
![](https://kissel.ch/ict/images/hybrid7_vlan.png)
2) Interface Assignment:
![](https://kissel.ch/ict/images/hybrid7_interfaces.png)
3) Assign new Interface to WAN:<br>
![](https://kissel.ch/ict/images/hybrid7_wan.png)
4) Configure WAN Interface:<br>
Interfaces → [WAN]
![](https://kissel.ch/ict/images/hybrid7_advancedoptions.png)
(rest is equal)
5) Finally check if you are "up":
![](https://kissel.ch/ict/images/hybrid7_overview.png)
