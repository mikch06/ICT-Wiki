#  Homeassistant config
<!-- date: 2023-02-01 00:00:00 -->
<!-- category: homeassistant -->
<!-- tags: homeassistant -->

# Add-ons
## deConz add-on
deConz -> config

Options:

use serial connection:
/dev/serial/by-id/usb-dresden_elektronik_ingenieurtechnik_GmbH_ConBee_II_DE2651844-if00

## NGINX Home Assistant SSL proxy add-on

no special config needed

but

upload cert and privkey file

-> that's why you have to use the 
Terminal&SSH add-on


# Geräte&Dienste / Integration

- Integration hinzufügen
- deConz
- Take ipaddress and port -> for that check API information in deConz Gateway (go by add-on)

![deconz-gateway-config.png](https://kissel.ch/ict/images/deconz-gateway-config.png)