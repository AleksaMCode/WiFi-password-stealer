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
  - [Fetching stored WiFi passwords](#fetching-stored-wifi-passwords)
  - [Sending stolen data over email](#sending-stolen-data-over-email)
  - [Setup](#setup)
  - [Protection](#protection)
  - [To-Do List](#to-do-list)


## Prerequisites
<ul>
<li>Physical access to victims computer.</li>
<li>Unlocked victims computer.</li>
<li>Computer has to have internet access in order to send stolen data to your email.</li>
</ul>

## Requirements - What you'll need
<p align="justify"><img src="./resources/RPi-pico.png?raw=true" width="150" title="RPi pico illustration" align="left" hspace="5" vspace="5">
<br><br>
<ul>
<li>Raspberry Pi Pico</li>
<li>Micro USB to USB Cable</li>
<li>Jumper Wire (optional)</li>
<li>Transform RPi Pico into a USB Rubber Ducky (pico-ducky). <a href="https://github.com/dbisu/pico-ducky">Follow these simple steps.</a></li>
</ul></p><br><br>

> **Note**:
> <p align="justify">
> <ul><li>It is possible to build this tool using Rubber Ducky, but keep in mind that <a href="https://www.raspberrypi.com/products/raspberry-pi-pico/">RPi Pico</a> costs $4.00 and the <a href="https://shop.hak5.org/products/usb-rubber-ducky">Rubber Ducky</a> costs $80.00.</li>
> <li>In order to use Ducky Script to write the payload on your RPi Pico you first need to convert it to a pico-ducky.

## Keystroke injection
<p align="justify">Keystorke injection tool, once connected to a host machine, executes malicious commands by running code that mimics keystrokes enterned by a user. While it looks like a USB drive, it acts like a keyboard that types in a preprogrammed payload. Tools like Rubber Ducky can type over 1,000 words per minut. Once created, anyone with physical access can deploy these payloads with ease.</p>

### USB Mass Storage Device Problem
<p align="justify">One of the advantages of Rubber Ducky over RPi Pico is that it doesn't show up as a USB mass storage device once plugged in. This isn't a default behaviour for RPi. If you want to prevent your RPi Pico from showing up as a USB mass storage device when plugged in, you need to connect jumper wire between pin 18 (<code>GND</code>) and pin 20 (<code>GPIO15</code>).</p>

> **Note**:
> <ul>
> <li>Upload your payload to RPi Pico before you connect the pins.</li>
> <li>Don't solder the pins because you will probably want to change/update the payload at some point.</li>
> </ul>

## Fetching stored WiFi passwords
## Sending stolen data over email
<p align="justify">Once the passwords have been exportet to the <code>.txt</code> file, payload will send the data to the appointed email over the Yahoo SMTP. Check out this <a href="https://github.com/AleksaMCode/university-notices-email-notifier#yahoo-smtp">link</a> to see how to setup Yahoo SMTP. Also, the payload needs to be updated with a proper SMTP information.</p>

https://github.com/AleksaMCode/WiFi-password-stealer/blob/d99f11cd630e91d7e9a409bfed175ca46e899c14/payload.dd#L28

<p align="justify">After adding SMTP password, receiver and send email you need to copy the payload.dd to a RPi Pico.</a>

> **Note**: <p align="justify">You can also use some other email provider SMTP, but you should be mindful of SMTP server and port number you will write in the payload.</p>

## Setup
<p align="justify">After creating pico-ducky, you only need to copy the modified payload (adjusted for your SMTP information) to the RPi Pico.</p>

## Protection

## To-Do List
- [ ] Fix `Caps Lock` bug.
- [ ] Fix  non-English Environment bug.
- [ ] Obfuscate the command prompt.
