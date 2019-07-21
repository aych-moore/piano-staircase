# piano-staircase
Piano staircase created for Unleash Space. Raspberry pi + Arduino

## Specs
Pi: Rasberry Pi 3 model A+

OS: Rasbian buster lite

Arduino: ATMEGA328p (nano form factor)


## SD setup for headless opperation
File name 'ssh' placed in root boot directory to activate ssh. No file extension, no content.

Network setup with wpa_supplicant.conf file:
```
country=NZ
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}
```

## Enviroment setup

```
sudo apt-get install git
git clone https://github.com/htmoor/piano-staircase.git
sudo apt-get install python3
sudo apt-get install python-pip
sudo pip install pygame
```






## Power saving

Disable HDMI hardware

Disable WiFi
