#!/bin/bash
echo "Wireless_Network_Name Password\n--------------------- --------" > /media/$(hostname)/$1/wifi_pass.txt

for FILE in /etc/NetworkManager/system-connections/*
do
    echo "$(cat "$FILE" | grep -oP '(?<=ssid=).*') \t\t\t\t  $(cat "$FILE" | grep -oP '(?<=psk=).*')"
done >> /media/$(hostname)/$1/wifi_pass.txt