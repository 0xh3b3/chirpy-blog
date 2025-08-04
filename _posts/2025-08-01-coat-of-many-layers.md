---
title: "Coat Of Many Layers"
date: 2025-08-01
categories: [CTF, mmuCTF, Forensics]
tags: [forensics]
---

# Challenge
>***Points:** 100*

>To be good at forensics is enough to solve this chall? Yes. Base knowledge is needed..
>**Attachment:** [keepGoin.zip](/assets/file/chall.bin)
>
>***Author:** mburk4*
---

## Solution
Well I can say that this was more of a misc than a forensics challenge ...
So I went ahead did some strings

`strings chall.bin`


I got some binary data so I uploaded the file to Cyber Chef and decoded it but got wierd strings [chall.txt](/assets/file/chall.txt) which from my experience with ciphers I could tell it was ROT47, so I decoded it and the rest cyberchef magic functionality (the little wand on the decode area) did its thing by automaticall identifying and decoding the output `Binary` => `ROT47` => `Base32` => `Hex` => FileTypeDetected(`7zip`)

I downloaded the file, a 7z, [chall.7z](/assets/file/chall.7z), lucky enough cyberchef has a functionality for that, ***NB:** *Download the file before filie detect**.

It is password protected, Time to use john the ripper with [rockyou.txt](https://github.com/zacheller/rockyou), both pre-installed in Linux

`7z2john chall.7z > chall.hash`

`john --wordlist=/usr/share/wordlists/rockyou.txt chall.hash`

`john --show chall.hash`

**PASSWORD*: kupal* 

Lets now unzip with 7z

`7z x download.7z`

I got a file called flag.txt and __cat__

> `mmuctf{0ni0n_l4y3r}`






