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

## Script run on boot
```
sudo nano /etc/profile
```
Scroll to bottom and add:
```
sudo python3 /home/pi/piano-staircase/piano_script.py
```



## Power saving

Disable HDMI hardware
```
sudo nano /etc/rc.local
```
Add following lines above exit 0:
```
# Disable HDMI
/usr/bin/tvservice -o
```

Disable WiFi
