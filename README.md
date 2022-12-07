<img width="150" align="right" src="./resources/wifi-stealer_logo.png"></img>
# WiFi password stealer
> **Disclaimer**: All content in this project is intended for security research purpose only.
<p align="justify">Have you ever watched a film where a hacker would plug-in, seemingly ordinary, USB drive into a a victims computer and steal data from it? - A proper wet dream for some. <br><br>
This summer I decided to do exactly that, to build a device that will allow me to steel data from a victims computer. So, how does one deploy malware and exfiltrate data? In the following text I will explain all of the necessary steps, theory and nuances when it comes to building your own keystroke injection tool. While this project/tutorial focuses on stored WiFi passwords, payload and the code could easily be altered to steal absolutely anything. You are only limited by your imagination (and your technical skills).</p>

## Table of contents
- [WiFi password stealer](#wifi-password-stealer)
  - [Table of contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Requirements - What you'll need](#requirements---what-youll-need)
  - [Keystroke injection](#keystroke-injection)
    - [USB Mass Storage Device Problem](#usb-mass-storage-device-problem)
  - [Sending stolen data over email](#sending-stolen-data-over-email)
  - [Protection](#protection)
  - [To-Do List](#to-do-list)


## Prerequisites
<ul>
<li>Physical access to victims computer.</li>
<li>Unlocked victims computer.</li>
<li>Computer has to have internet access in order to send stolen data to your email.</li>
</ul>

## Requirements - What you'll need
<p align="justify"><img src="./resources/RPi-pico.png?raw=true" width="150" rotation="90" title="xkcd illustration" align="left" hspace="5" vspace="5">
<br><br>
<ul>
<li>Raspberry Pi Pico</li>
<li>Micro USB to USB Cable</li>
<li>Computer has to have internet access in order to send stolen data to an email.</li>
<li>Transform RPi Pico into a USB Rubber Ducky. <a href="https://github.com/dbisu/pico-ducky">Follow these simple steps.</a></li>
</ul></p><br><br>

> **Note**: <p align="justify">It is possible to build this tool using Rubber Ducky, which will make this whole process a bit easer but more expensive as <a href="https://www.raspberrypi.com/products/raspberry-pi-pico/">RPi Pico</a> costs $4.00 and the <a href="https://shop.hak5.org/products/usb-rubber-ducky">Rubber Ducky</a> costs $80.00.</p>

## Keystroke injection
<p align="justify">Keystorke injection tool, once connected to a host machine, executes malicious commands by running code that mimics keystrokes enterned by a user. While it looks like a USB drive, it acts like a keyboard that types in a preprogrammed payload. Tools like Rubber Ducky can type over 1,000 words per minut. Although this project is focosed on RPi Pico, I'm not sure what speed it can achieve. Once created, anyone with physical access can deploy these payloads with ease.</p>

### USB Mass Storage Device Problem
<p align="justify">One of the advantages of Rubber Ducky over RPi Pico is that it doesn't show up as a USB mass storage device once plugged in. This isn't a default behaviour for RPi. If you want to prevent your RPi from showing up as a USB mass storage device when plugged into the target computer you need to connect jumper wire between pin 18 (<code>GND</code>) and pin 20 (<code>GPIO15</code>).</p>

## Sending stolen data over email
## Protection

## To-Do List
- [ ] Fix `Caps Lock` bug.
- [ ] Fix  non-English Environment bug.
