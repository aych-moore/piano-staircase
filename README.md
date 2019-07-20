# piano-staircase
Piano staircase created for Unleash Space. Raspberry pi + Arduino

## Specs
Pi: Rasberry Pi 3 model A+
OS: Rasbian buster lite
Arduino: ATMEGA328p (nano form factor)

## SD setup for headless opperation
ssh file place in root boot directory to activate ssh.

Network setup with wpa_supplicant.conf file.
```
country=NZ
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}
```
