# apu coreboot update
<!-- date: 2019-12-12 00:00:00 -->
<!-- category: apu -->
<!-- tags: apu,pcengines,coreboot -->

###Links
- Home: <a href="https://www.pcengines.ch">pcengines.ch</a><br>
- CH Shop: <a href="https://www.pcengines.ch/newshop.php?c=48881">https://www.pcengines.ch/newshop.php?c=48881</a><br>
- Howto: <a href="https://pcengines.ch/howto.htm">https://pcengines.ch/howto.htm</a><br>
- Github rom releases: <a href="https://pcengines.github.io">https://pcengines.github.io</a><br>

###Update coreboot rom
Install flushrom on your device:<br>

for CentOS
    <pre>yum -y install flashrom</pre>
    <br>
    FreeBSD / Opnsense
    <pre>pkg install flushrom</pre>
    <br>
    Check APU Version
    <pre>dmidecode |less 
> BIOS Information        Vendor: coreboot        Version: 4.0.7 
> System Information        Manufacturer: PC Engines        Product Name: APU3        Version: 1.0</pre>
Find current coreboot release:<br>

<a href="https://pcengines.github.io" target="_blank">https://pcengines.github.io</a><br>
<a href="https://3mdeb.com/open-source-firmware/pcengines/" target="_blank">https://3mdeb.com/open-source-firmware/pcengines/</a>
<br><br>
Download to your device:
<br>
e.g.
<pre>wget https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.1.rom</pre>
Install
<pre>flashrom -w /tmp/apu2_v4.11.0.1.rom -p internal</pre>
*Output*
<pre>flashrom -w apu3_v4.11.0.1.rom -p internal flashrom v1.0.1 on Linux 3.10.0-957.27.2.el7.x86_64 (x86_64) flashrom is free software,<br>get the source code at https://flashrom.org Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns). coreboot table found <br>at 0xdffae000. Found chipset "AMD FCH". Enabling flash write... OK. Found Winbond flash chip "W25Q64.V" (8192 kB, SPI) mapped at <br>physical address 0x00000000ff800000. This coreboot image (PC Engines:apu3) does not appear to be correct for the detected mainboard 
    (PC Engines:PCEngines apu3). Aborting. You can override this with -p internal:boardmismatch=force.</pre>

bash

<pre>flashrom -w /tmp/apu2_v4.11.0.1.rom -p internal:boardmismatch=force</pre>
