---
title: "Speak My Language"
date: 2025-08-01
categories: [CTF, mmuCTF, Stego]
tags: [stego]
---

# Challenge
>***Points:** 150*

>I’m the reason esoteric is in the dictionary. You’re welcome.
>
>**Attachment:** [echoesofwar.png](/assets/file/mmu.png)
>
>***Author:** mburk4*
---

## Solution
After trying several steg tools, I finaly got something with stegseek, actually its a cap, I started with stegseek and I didn't have to waste my time on other tools

`stegseek --crack -sf mmu.png -wl /usr/share/wordlists/rockyou.txt -xf file.txt`

the results had a bunch of random strings that I visually identified as base64, because of the many characters I will not display here but instead I have linked a downloadable below: [file.txt](/assets/file/file.txt)

I ran the base64 decode command, you can use cyberchef or dcode.fr though if you are not too familiar with these command.

`cat flag.txt | base64 -d | tee > file1.txt`

The result was a morse code: [file1.txt](/assets/file/file1.txt). I uploaded the file to cyberchef and decoded from Morse and it gave me a results with a bunch of random "!", "?" and "." symbols which I was not familiar with and neither was CyberChef

I saved the output into a file, as cyberchef has an option to do that: [file2.txt](/assets/file/file2.txt) 

I went directly to my side chick for decoding cipers, . It quickly identified the text as not a cipher but a Programming Language. Called __Ook! Programming language__ which is a parody of BrainFuck.js

We call such programming languages that do not use the regular Arabic let[dcode.fr Cipher Identifier Utility](https://www.dcode.fr/cipher-identifier)ters, __Esoteric Programming Languages__

A quick google search for Ook! Deobsuficator and I got this site [Brainfuck/Text/Ook! Deobsuficator](https://stuff.splitbrain.org/ook/). After deobsufication I still got a cipher which was more close to the flag, 
`Pg rmzpf rxmsqf: yygofr{zg_fmxqd_hu_emyyq_ebdas}`
I quickly identified it as ROT13, I itterated through the rotations and I landed on the 14th rotation which had the flag format. But it was not a language I was familiar with

`Du fandt flaget: mmuctf{nu_taler_vi_samme_sprog}`

I tried translating it with Google Translate and it identified it as Danish, to English `mmuctf{now_we_speak_the_same_language}`. Interestingly, the Dannish version was the one that accepted as the flag.

> ```mmuctf{nu_taler_vi_samme_sprog}```

## Learning Resources

Wikipedia: [Esoteric Programming Languages](https://en.wikipedia.org/wiki/Esoteric_programming_language)</br>
TryHackMe: [Linux Modules](https://tryhackme.com/room/linuxmodules)</br>
TryHackMe: [Practice 1](https://tryhackme.com/room/ctfcollectionvol1)</br>
TryHackMe: [Practice 2](https://tryhackme.com/room/ctfcollectionvol2)</br>
TryHackMe: [CryptoForDummies](https://tryhackme.com/room/cryptographyfordummies)</br>

My Top Steganography Tools:</br>
`Strings`
`File`
`ExifTool`
`Binwalk`
`Zsteg`
`Stegsnow`
`Stegsolve`
`Steghide`
`Sonic Visualizer`
`Stegseek`
`Stegoveritas`
`OpenStego`
`DeepSound`
`Sonic-Visualiser`
`Audacity`



