---
title: "Echoes Of War"
date: 2025-08-01
categories: [CTF, mmuCTF, Stego]
tags: [stego]
---

# Challenge
>***Points:** 150*

>My image was quite good but i cant really know what has happened it seems off. 
>Can you see through the extensions of steg and get the flag underneath.
>
>**Attachment:** [echoesofwar.png](/assets/file/echoesofwar.png)
>
>***Author:** 0xdeadBeef*
---

## Solution
I downloaded the image but upon viewing it with __eog__ linux utility/command

```eog echoesofwar.png```

I was met with an error indicating that either the the extention was not an image or it was an image but with corrupt headers.</br>

To verify this I ran file command and iterestingly it brought me the type as __data__</br>

My conclusion to this was: the file was indeed an image but had corrupt hex values in it, also the challenge description clearly stated that it was an image and I dont think the author had any intentions to trick or deceive us

My first approach to this was to investigate the hex values and verify the file signatures, every file extension has distinct bytes that identifies them as that file extention called magic bytes or file signatures

I viewed the hex bytes using hexeditor and this is where I stumbled across my first challenge, according to the bytes (check the ASCII Offset), it could be either PNG or JPG, lol! the auther clearly had intentions to trick us!!

I headed to the Wikipedia page for [List of File Signature](https://en.wikipedia.org/wiki/List_of_file_signatures) hit CTRL+F to filter/find jpg and png respectfully. note that I also used this page to compare the bytes.

Here is a break down of what I discovered, the first 8 magic bytes were PNG while the next 8 were JPG which was not right.

What was better than trying to change the bytes to JPG and PNG in different files called echoesofwar_fixed.(png and jpg) since the probability was 1/2? so I Tried first making all 16 header bytes to PNG then to JFIF, only JFIF showed an image

![flag image](/assets/img/echoesofwar_fixed.jpg)

This was clearly not the end for I didnt had a flag yet, I ran different steg tool and I was able to recover a file with stegseek with the command, (check with --help)

```stegseek --crack -sf echoesofwar_fixed.jpg -wl /usr/share/wordlists/rockyou.txt -xf flag.txt```

on `cat flag.txt` I got some gibberish

```w@H 2>2K:?8 E9:D :D =DP *@F 8@E J@FC 7=28 >>F4E7L$Eb80`?0%9b09bIb0s`%_#N```

I headed over to cyberchef and pasted it I could tell through experience that this was ROT47 and indeed it was.

For anyone who cannot identify this cypher, they can use dcode.fr's cypher identifier utility since cyberchefs magic utility cannot identify this.

The output text
`How amazing this is ls! You got your flag mmuctf{St3g_1n_Th3_h3x3_D1T0R}`

>`mmuctf{St3g_1n_Th3_h3x3_D1T0R}`

## Learning Resources

Wikipedia: [JFIF](https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format)</br>
TryHackMe: [Cyberchef Basics](https://tryhackme.com/room/cyberchefbasics)</br>


    WRITERS COMMENTS:

    "At this point, from the few ctf-writeup I have written you should have realised how understanding hexadecimals is very important not just in CTFs but in Ethical Hacking and Cyber Security in general, I challenge the reader to go and research and understand more about hexadecimal numbers. I have encountered Hexadecimals in Forensics, Programming, Cryptography, etc. both in CTFs and real world scenarios"

    ~0xh3b3


