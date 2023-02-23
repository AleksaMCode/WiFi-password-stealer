<img width="150" align="right" src="./resources/wifi-stealer_logo.png"></img>
# WiFi password stealer
> **Disclaimer**: All content in this project is intended for security research purpose only.
<p align="justify">Have you ever watched a film where a hacker would plug-in, seemingly ordinary, USB drive into a victim's computer and steal data from it? - A proper wet dream for some.

## Table of contents
- [WiFi password stealer](#wifi-password-stealer)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Requirements - What you'll need](#requirements---what-youll-need)
  - [Exfiltration](#exfiltration)
  - [Keystroke injection tool](#keystroke-injection-tool)
    - [Keystroke injection](#keystroke-injection)
    - [Delays](#delays)
  - [USB Mass Storage Device Problem](#usb-mass-storage-device-problem)
  - [Sending stolen data over email](#sending-stolen-data-over-email)
    - [Exfiltrated WiFi data](#exfiltrated-wifi-data)
  - [Limitations/Drawbacks](#limitationsdrawbacks)
  - [To-Do List](#to-do-list)

## Introduction
<p align="justify">During the summer of 2022, I decided to do exactly that, to build a device that will allow me to steal data from a victim's computer. So, how does one deploy malware and exfiltrate data? In the following text I will explain all of the necessary steps, theory and nuances when it comes to building your own keystroke injection tool. While this project/tutorial focuses on WiFi passwords, payload code could easily be altered to do something more nefarious than stealing stored WiFi passwords. You are only limited by your imagination (and your technical skills).</p>

## Setup
<p align="justify">After creating pico-ducky, you only need to copy the modified payload (adjusted for your SMTP details) to the RPi Pico.</p>

## Prerequisites
<ul>
<li>Physical access to victim's computer.</li>
<li>Unlocked victim's computer.</li>
<li>Computer has to have internet access in order to send stolen data to your email.</li>
</ul>

## Requirements - What you'll need
<p align="justify"><img src="./resources/RPi-pico.png?raw=true" width="150" title="RPi pico illustration" align="left" hspace="5" vspace="5">
<br><br>
<ul>
<li>Raspberry Pi Pico (RPi Pico)</li>
<li>Micro USB to USB Cable</li>
<li>Jumper Wire (optional)</li>
<li>pico-ducky - Transformed RPi Pico into a USB Rubber Ducky</li>
</ul></p><br><br>

> **Note**:
> <ul><li><p align="justify">It is possible to build this tool using Rubber Ducky, but keep in mind that <a href="https://www.raspberrypi.com/products/raspberry-pi-pico/">RPi Pico</a> costs $4.00 and the <a href="https://shop.hak5.org/products/usb-rubber-ducky">Rubber Ducky</a> costs $80.00.</p></li>
> <li><p align="justify">In order to use Ducky Script to write the payload on your RPi Pico you first need to convert it to a pico-ducky. Follow these <a href="https://github.com/dbisu/pico-ducky">simple steps</a> in order to create pico-ducky.</p></li>
> </ul>

## Exfiltration
<p align="justify">Data exfiltration is an unauthorized transfer of data from a computer/device. Once the data is collected, adversary can package it to avoid detection while sending data over the network, using encryption or compression. Two most common way of exfiltration are:
<ul>
<li>Exfiltration over network medium.</li>
<li>Exfiltration over a physical medium.</li>
</ul>

## Keystroke injection tool
<p align="justify">Keystroke injection tool, once connected to a host machine, executes malicious commands by running code that mimics keystrokes entered by a user. While it looks like a USB drive, it acts like a keyboard that types in a preprogrammed payload. Tools like Rubber Ducky can type over 1,000 words per minute. Once created, anyone with physical access can deploy this payload with ease.</p>

### Keystroke injection
<p align="justify">The payload uses <code>STRING</code> command processes keystroke for injection. It accepts one or more alphanumeric/punctuation characters and will type the remainder of the line exactly as-is into the target machine. The <code>ENTER</code>/<code>SPACE</code> will simulate a press of keyboard keys.</p>

### Delays
<p align="justify">We use <code>DELAY</code> command to temporarily pause execution of the payload. This is useful when a payload needs to wait for an element such as a Command Line to load. Delay is useful when used at the very beginning when a new USB device is connected to a targeted computer. Initially, the computer must complete a set of actions before it can begin accepting input commands. In the case of <a href="https://en.wikipedia.org/wiki/Human_interface_device">HIDs</a> setup time is very short. In most cases, it takes a fraction of a second, because the drivers are built-in. However, in some instances, a slower PC may take longer to recognize the pico-ducky. The general advice is to adjust the delay time according to your target.</p>

## USB Mass Storage Device Problem
<p align="justify">One of the advantages of Rubber Ducky over RPi Pico is that it doesn't show up as a USB mass storage device once plugged in. Once plugged into the computer, all the machine sees it as a USB keyboard. This isn't a default behavior for RPi. If you want to prevent your RPi Pico from showing up as a USB mass storage device when plugged in, you need to connect a jumper wire between pin 18 (<code>GND</code>) and pin 20 (<code>GPIO15</code>).</p>

> **Note**:
> <ul>
> <li>Upload your payload to RPi Pico before you connect the pins.</li>
> <li>Don't solder the pins because you will probably want to change/update the payload at some point.</li>
> </ul>

## Sending stolen data over email
<p align="justify">Once the passwords have been exported to the <code>.txt</code> file, payload will send the data to the appointed email over the Yahoo SMTP. Check out this <a href="https://github.com/AleksaMCode/university-notices-email-notifier#yahoo-smtp">link</a> to see how to set up Yahoo SMTP. Also, the payload needs to be updated with proper SMTP information.</p>

https://github.com/AleksaMCode/WiFi-password-stealer/blob/d99f11cd630e91d7e9a409bfed175ca46e899c14/payload.dd#L28

<p align="justify">After sending data over email, the <code>.txt</code> file is deleted.</p>

> **Note**: 
> <ul>
> <li><p align="justify">You can also use some an SMTP from another email provider, but you should be mindful of SMTP server and port number you will write in the payload.</p></li>
> <li><p align="justify">Keep in mind that some networks could be blocking usage of an unknown SMTP at the firewall.</p></li>
> </ul>
> </p>

### Exfiltrated WiFi data
<p align="justify">Below is an example of exfiltrated and formatted data from a victim's machine in a <code>.txt</code> file.<p>

https://github.com/AleksaMCode/WiFi-password-stealer/blob/f5b3b11328764eb07d765a210fbf25db3a828455/resources/wifi_pass.txt#L1-L5

## Limitations/Drawbacks
<ul>
<li><p align="justify">This pico-ducky currently works only on Windows OS.</p></li>
<li><p align="justify">This attack requires physical access to an unlocked device in order to be successfully deployed.</p></li>
<li><p align="justify">Machine's firewall or network's firewall may prevent stolen data from being sent over the network medium.</p></li>
<li><p align="justify">Payload delays could be inadequate due to varying speeds of different computers used to deploy an attack.</p></li>
<li><p align="justify">This device isn't really stealthy, actually it's quite the opposite, it's really bulky.</p></li>
<li><p align="justify"><s>If the <code>Caps Lock</code> is ON, some of the payload code will not be executed and the exploit will fail.</p></s></li>
<li><p align="justify">If the computer has a non-English Environment set, this exploit won't be successful.</p></li>
</ul>

## To-Do List
- [x] Fix `Caps Lock` bug.
- [ ] Fix non-English Environment bug.
- [ ] Obfuscate the command prompt.
- [ ] Implement exfiltration over a physical medium.
- [ ] Create a payload for Linux.
- [ ] Encode/Encrypt exfiltrated data before sending it over email.
- [ ] Implement indicator of successfully completed exploit.