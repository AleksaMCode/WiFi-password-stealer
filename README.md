<img width="150" align="right" src="./resources/wifi-stealer_logo.png"></img>
# WiFi password stealer
[![License: GPL v2](https://img.shields.io/badge/license-GPL_v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
![](https://img.shields.io/github/v/release/AleksaMCode/WiFi-password-stealer)
![](https://img.shields.io/github/downloads/AleksaMCode/WiFi-password-stealer/total.svg)

<p align="justify">Have you ever seen a movie where a hacker plugs a seemingly ordinary USB drive into a computer and instantly steals data? Today, you'll be building a device that does exactly that.</p>

> :warning: **Disclaimer**: <p align="justify">All content in this project is intended for security research purposes only.</p>

## Table of contents
- [WiFi password stealer](#wifi-password-stealer)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
  - [Rubber Ducky attack](#rubber-ducky-attack)
    - [Requirements - What you'll need](#requirements---what-youll-need)
    - [Keystroke injection tool](#keystroke-injection-tool)
      - [Keystroke injection](#keystroke-injection)
      - [Delays](#delays)
    - [Exfiltration](#exfiltration)
      - [Windows exploit](#windows-exploit)
        - [Sending stolen data over email](#sending-stolen-data-over-email)
      - [Linux exploit](#linux-exploit)
        - [Storing stolen data to USB flash drive](#storing-stolen-data-to-usb-flash-drive)
        - [Bash script](#bash-script)
        - [Quick overview of the payload](#quick-overview-of-the-payload)
      - [Exfiltrated data formatting](#exfiltrated-data-formatting)
    - [USB Mass Storage Device Problem](#usb-mass-storage-device-problem)
    - [Payload Writer](#payload-writer)
  - [Bash Bunny attack](#bash-bunny-attack)
  - [Limitations/Drawbacks](#limitationsdrawbacks)
  - [References](#references)
  - [To-Do List](#to-do-list)

## Introduction
<p align="justify">In the summer of 2022, I set out to build a device capable of extracting data from a target computer. But how exactly does one deploy malware and exfiltrate information? In the following sections, I’ll walk through the essential steps, underlying concepts, and technical nuances involved in creating a custom keystroke injection tool. While this project specifically targets WiFi credentials, the payload can easily be modified for more advanced or malicious purposes—the only real limits are your creativity and technical expertise.</p>

## Setup
<p align="justify">Over time, the project has grown to include a wide variety of scripts and tools. It was originally created to demonstrate the capabilities of a Rubber Ducky—specifically, a cost-effective version using the Raspberry Pi Pico (RPi Pico). Currently, the two main components of the project are:

<ol>
  <li><b>Rubber Ducky attack</b></li>
  <li><b>Bash Bunny attack</b>
  </li>
</ol>
</p>

### Prerequisites
<ul>
<li><p align="justify">Physical access to the unlocked victim's computer.</p></li>
<li><p align="justify">The computer has to have internet access in order to send the stolen data using <a href="https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol">SMTP</a> for exfiltration over a network medium.</li></p>
<li><p align="justify">Knowledge of the victim's computer password for the Linux exploit.</p></li>
</ul>

## Rubber Ducky attack 

<p align="justify">After creating a pico-ducky, you only need to copy the modified payload (adjusted for your SMTP details for the Windows exploit and/or adjusted for the Linux password and a USB drive name) to the RPi Pico.</p>

### Requirements - What you'll need
<p align="justify"><img src="./resources/RPi-pico.png?raw=true" width="150" title="RPi pico illustration" align="left" hspace="5" vspace="5">
<br>
<ul>
<li>RPi Pico</li>
<li>Micro USB to USB Cable</li>
<li>Jumper Wire (optional)</li>
<li>pico-ducky: Transformed RPi Pico into a USB Rubber Ducky</li>
<li>USB flash drive (for the exploit over a physical medium only)</li>
</ul></p><br><br>

> [!NOTE]
> <ul><li><p align="justify">It is possible to build this tool using the Rubber Ducky, but keep in mind that <a href="https://www.raspberrypi.com/products/raspberry-pi-pico/">RPi Pico</a> costs about $4.00 and the <a href="https://shop.hak5.org/products/usb-rubber-ducky">Rubber Ducky</a> costs $80.00.</p></li>
> <li><p align="justify">However, while pico-ducky is a good and budget-friendly solution, Rubber Ducky does offer things like stealthiness and usage of the latest DuckyScript version.</p></li>
> <li><p align="justify">In order to use Ducky Script to write the payload on your RPi Pico, you first need to convert it to a pico-ducky. Follow these <a href="https://github.com/dbisu/pico-ducky">simple steps</a> in order to create pico-ducky.</p></li>
> </ul>

### Keystroke injection tool
<p align="justify">A keystroke injection tool, once connected to a host machine, executes malicious commands by running code that mimics keystrokes entered by a user. While it looks like a USB drive, it acts like a keyboard that types in a preprogrammed payload. Tools like Rubber Ducky can type over 1,000 words per minute. Once created, anyone with physical access can deploy this payload with ease.</p>

#### Keystroke injection
<p align="justify">The payload uses <code>STRING</code> command to processes injection keystrokes. It accepts one or more alphanumeric/punctuation characters and will type the remainder of the line exactly as-is into the target machine. The <code>ENTER</code>/<code>SPACE</code> will simulate a press of keyboard keys.</p>

#### Delays
<p align="justify">We use <code>DELAY</code> command to temporarily pause execution of the payload. This is useful when a payload needs to wait for an element, such as a Command Line, to load. Delay is useful when used at the very beginning, when a new USB device is connected to a targeted computer. Initially, the computer must complete a set of actions before it can begin accepting input commands. In the case of <a href="https://en.wikipedia.org/wiki/Human_interface_device">HIDs</a> setup time is very short. In most cases, it takes a fraction of a second because the drivers are built-in. However, in some instances, a slower PC may take longer to recognize the pico-ducky. The general advice is to adjust the delay time according to your target.</p>

### Exfiltration
<p align="justify">Data exfiltration is the unauthorized transfer of data from a computer/device. Once the data is collected, an adversary can package it to avoid detection while sending data over the network using encryption or compression. Two most common ways of exfiltration are:</p>
<ul>
<li>Exfiltration over the network medium.</li>
  <ul>
    <li><p align="justify">This approach was used for the Windows exploit. The whole payload can be seen <a href="https://github.com/AleksaMCode/WiFi-password-stealer/blob/main/payload/payload_windows.template.dd">here</a>.</li>
  </ul>
<li>Exfiltration over a physical medium.</li>
  <ul>
    <li><p align="justify">This approach was used for the Linux exploit. The whole payload can be seen <a href="https://github.com/AleksaMCode/WiFi-password-stealer/blob/main/payload/payload_linux.template.dd">here</a>.</li>
  </ul>
</ul>

#### Windows exploit
<p align="justify">In order to use the Windows payload (<code>payload1.dd</code>), you don't need to connect any jumper wire between pins.</p>

##### Sending stolen data over email
<p align="justify">Once passwords have been exported to the <code>.txt</code> file, payload will send the data to the appointed email using Yahoo SMTP. For more detailed instructions, visit the following <a href="https://github.com/AleksaMCode/university-notices-email-notifier#yahoo-smtp">link</a>. Also, the payload template needs to be updated with your SMTP information, meaning that you need to update <code>RECEIVER_EMAIL</code>, <code>SENDER_EMAIL</code>, and your email <code>PASSWORD</code>. In addition, you could also update the body and the subject of the email.</p>

https://github.com/AleksaMCode/WiFi-password-stealer/blob/25cf7c56a7df4a9811b4d3eab8d6e6dad4282055/payload/payload_windows.template.dd#L31

> [!NOTE]
> <ul>
> <li><p align="justify">After sending data over the email, the <code>.txt</code> file is deleted.</p></li>
> <li><p align="justify">You can also use an SMTP from another email provider, but you should be mindful of the SMTP server and port numbers you will write in the payload.</p></li>
> <li><p align="justify">Keep in mind that some networks could be blocking the usage of an unknown SMTP at the firewall.</p></li>
> </ul>
> </p>

#### Linux exploit
<p align="justify">In order to use the Linux payload (<code>payload2.dd</code>) you need to connect a jumper wire between <code>GND</code> and <code>GPIO5</code> in order to comply with the code in <a href="https://github.com/dbisu/pico-ducky/blob/main/duckyinpython.py"><code>code.py</code></a> on your RPi Pico. For more information about how to setup multiple payloads on your RPi Pico, visit this <a href="https://github.com/dbisu/pico-ducky#multiple-payloads">link</a>. 

<p align="center">
<img
src="./resources/linux-mint_exploit.gif"
alt="Exploit on Linux Mint"
width="100%"
class="center"
/>
<p align="center">
    <label><b>Fig. 1</b>: Exploit on Linux Mint</label>
    </p>
</p>


##### Storing stolen data to USB flash drive
<p align="justify">Once passwords have been exported from the computer, data will be saved to the designated USB flash drive. In order for this payload to function properly, it needs to be updated with the correct name of your USB drive, meaning you will need to replace <code>USBSTICK</code> with the name of your USB drive in two places.</p>

https://github.com/AleksaMCode/WiFi-password-stealer/blob/25cf7c56a7df4a9811b4d3eab8d6e6dad4282055/payload/payload_linux.template.dd#L3

https://github.com/AleksaMCode/WiFi-password-stealer/blob/25cf7c56a7df4a9811b4d3eab8d6e6dad4282055/payload/payload_linux.template.dd#L11

<p align="justify">In addition, you will also need to update the Linux <code>PASSWORD</code> in the payload in three places. As stated above, in order for this exploit to be successful, you will need to know the victim's Linux machine password, which makes this attack less plausible.</p>

https://github.com/AleksaMCode/WiFi-password-stealer/blob/a90ffb208e6a09d1b0ae44d1afe81d82248ba3fe/payload/payload_linux.template.dd#L7

https://github.com/AleksaMCode/WiFi-password-stealer/blob/a90ffb208e6a09d1b0ae44d1afe81d82248ba3fe/payload/payload_linux.template.dd#L9

##### Bash script
<p align="justify">In order to run the <a href="https://github.com/AleksaMCode/WiFi-password-stealer/blob/main/scripts/wifi_passwords_print.sh"><code>wifi_passwords_print.sh</code></a> script you will need to update the script with the correct name of your USB stick after which you can type in the following command in your terminal:</p>

```bash
echo PASSWORD | sudo -S sh wifi_passwords_print.sh USBSTICK
```

where `PASSWORD` is your account's password and `USBSTICK` is the name for your USB device.

##### Quick overview of the payload
<p align="justify"><b>NetworkManager</b> is based on the concept of connection profiles, and it uses plugins for reading/writing data. It uses <code>.ini-style</code> keyfile format and stores network configuration profiles. The <b>keyfile</b> is a plugin that supports all the connection types and capabilities that <b>NetworkManager</b> has. The files are located in <i>/etc/NetworkManager/system-connections/</i>. Based on the <b>keyfile</b> format, the payload uses the <code>grep</code> command with regex in order to extract data of interest. For file filtering, a modified positive lookbehind assertion was used (<code>(?<=keyword)</code>). While the positive lookbehind assertion will match at a certain position in the string, <a href="https://en.wikipedia.org/wiki/Viz.">sc.</a> at a position right after the <i>keyword</i> without making that text itself part of the match, the regex <code>(?<=keyword).*</code> will match any text after the <i>keyword</i>. This allows the payload to match the values after <b>SSID</b> and <b>psk</b> (<a href="https://en.wikipedia.org/wiki/Pre-shared_key">pre-shared key</a>) keywords.</p>

<p align="justify">For more information about <b>NetworkManager</b> here is some useful links:</p>

- [Manually creating NetworkManager profiles in keyfile format](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/assembly_networkmanager-connection-profiles-in-keyfile-format_configuring-and-managing-networking#proc_manually-creating-a-networkmanager-profile-in-keyfile-format_assembly_networkmanager-connection-profiles-in-keyfile-format)
- [Description of keyfile settings plugin](https://developer-old.gnome.org/NetworkManager/stable/nm-settings-keyfile.html)

#### Exfiltrated data formatting
<p align="justify">Below is an example of the exfiltrated and formatted data from a victim's machine in a <code>.txt</code> file.<p>

https://github.com/AleksaMCode/WiFi-password-stealer/blob/f5b3b11328764eb07d765a210fbf25db3a828455/resources/wifi_pass.txt#L1-L5

### USB Mass Storage Device Problem
<p align="justify">One of the advantages of Rubber Ducky over RPi Pico is that it doesn't show up as a USB mass storage device once plugged in. Once plugged into the computer, all the machine sees it as a USB keyboard. This isn't a default behavior for the RPi Pico. If you want to prevent your RPi Pico from showing up as a USB mass storage device when plugged in, you need to connect a jumper wire between pin 18 (<code>GND</code>) and pin 20 (<code>GPIO15</code>). For more details visit this <a href="https://github.com/dbisu/pico-ducky#usb-enabledisable-mode">link</a>.</p>

> :bulb: **Tip**:
> <ul>
> <li>Upload your payload to RPi Pico before you connect the pins.</li>
> <li>Don't solder the pins because you will probably want to change/update the payload at some point.</li>
> </ul>

### Payload Writer
<p align="justify">When creating a functioning payload file, you can use the <a href="https://github.com/AleksaMCode/WiFi-password-stealer/blob/main/payload/writer.py"><code>writer.py</code></a> script, or you can manually change the template file. In order to run the script successfully you will need to pass, in addition to the script file name, a name of the OS (<i>windows</i> or <i>linux</i>) and the name of the payload file (e.q. <i><a href="https://github.com/AleksaMCode/WiFi-password-stealer/releases/latest/download/payload1.dd">payload1.dd</a></i>). Below you can find an example how to run the <i>writer</i> script when creating a Windows payload.</p>

```bash
python3 writer.py windows payload1.dd
```

## Bash Bunny attack 

<p align="justify">With a few minor modifications, the previously used scripts can also be adapted to run on the Bash Bunny. The Bash Bunny works by emulating a trusted USB device [1]. For this project, we’ll configure it to emulate a flash storage device using the following command [1,2]:</p>

```
ATTACKMODE HID STORAGE
```

<p align="justify">Using the DuckyScript <code>ATTACKMODE</code> command, we can define which type of device the Bash Bunny should emulate [1]. Each attack mode registers with the system using a unique USB Vendor ID (VID) and Product ID (PID) [1]. It's also possible to combine multiple attack modes by chaining them together.</p>

<p align="center">
<img
src="./resources/bash_bunny.jpg?raw=true"
alt="Bash Bunny plugged in a PC"
width="100%"
class="center"
/>
<p align="center">
    <label><b>Fig. 2</b>: <i>Bash Bunny Mark I</i> plugged in a PC</label>
    </p>
</p>

<p align="justify">The Bash Bunny supports the original DuckyScript commands, which is why I was able to reuse the script from the Rubber Ducky section. To use these commands inline, we need to prefix them with the <code>QUACK</code> command [1]. For example, instead of writing <code>WINDOWS r</code>, we write <code>Q WINDOWS r</code>. 


To load payloads onto the Bash Bunny, the device must be set to <b>arming mode</b> (switch position 3—the one closest to the USB plug) [1]. Once connected, copy <code>payload.txt</code> and <code>exfil.txt</code> to either <code>payloads\switch1</code> or <code>payloads\switch2</code>, depending on which switch position you plan to use. Payloads must be named <code>payload.txt</code>, while any supporting files referenced by the payload can be named freely.

For reference, the Bash Bunny mass storage directory structure is as follows [2]:
</p>

```
BashBunny/
├── loot/
│   └── (data exfiltrated from payloads will be saved here)
└── payloads/
    ├── library/
    │   └── (reusable scripts or modules)
    ├── switch1/
    │   ├── payload.txt
    │   └── (optional files, e.g., exfil.txt, scripts, etc.)
    └── switch2/
        ├── payload.txt
        └── (optional files)
```
<p align="center">
    <label><b>Fig. 3</b>: Bash Bunny Mass Storage Directory Structure</label>
</p>

<p align="justify">Once the script has finished executing, the results will be saved in <code>loot\wifi_pass.txt</code>. If the target computer has no saved WiFi passwords, the file will be empty.</p>

> [!NOTE]
> <p align="justify">Since the Bash Bunny attack relies on a PowerShell script (<code>exfil.txt</code>), it can only be used on Windows systems. To use a similar approach on Linux, you'll need to modify the payload and replacing the PowerShell script with the Bash script referenced in the Linux section above. </p>

## Limitations/Drawbacks
<ul>
<li><p align="justify"><s>This pico-ducky currently works only on Windows OS.</p></s></li>
<li><p align="justify">This attack requires physical access to an unlocked device in order to be successfully deployed.</p></li>
<li><p align="justify">The Linux exploit is far less likely to be successful, because in order to succeed, you not only need physical access to an unlocked device, you also need to know the admins password for the Linux machine.</p></li>
<li><p align="justify">Machine's firewall or network's firewall may prevent stolen data from being sent over the network medium.</p></li>
<li><p align="justify">Payload delays could be inadequate due to varying speeds of different computers used to deploy an attack.</p></li>
<li><p align="justify">The pico-ducky device isn't really stealthy, actually it's quite the opposite, it's really bulky especially if you solder the pins.</p></li>
<li><p align="justify">Also, the pico-ducky device is noticeably slower compared to the Rubber Ducky running the same script.</p></li>
<li><p align="justify"><s>If the <code>Caps Lock</code> is ON, some of the payload code will not be executed and the exploit will fail.</p></s></li>
<li><p align="justify">If the computer has a non-English Environment set, this exploit won't be successful.</p></li>
<li><p align="justify">Currently, pico-ducky doesn't support DuckyScript 3.0, only DuckyScript 1.0 can be used. If you need the 3.0 version you will have to use the Rubber Ducky. <b>For this exploit version 3.0 isn't needed!</b></p></li>
</ul>

## References

1. [Bash Bunny by Hak5 Documentation](https://docs.hak5.org/bash-bunny/bash-bunny-by-hak5/)
2. [Bash Bunny Basics Wiki](https://wiki.bashbunny.com/#!index.md)

## To-Do List
- [x] Fix `Caps Lock` bug.
- [ ] Fix non-English Environment bug.
- [ ] Obfuscate the command prompt.
- [x] Implement exfiltration over a physical medium.
- [x] Create a payload for Linux.
- [ ] Encode/Encrypt exfiltrated data before sending it over email.
- [ ] Implement indicator of successfully completed exploit.
- [ ] Implement command history clean-up for Linux exploit.
- [ ] Enhance the Linux exploit in order to avoid usage of `sudo`.