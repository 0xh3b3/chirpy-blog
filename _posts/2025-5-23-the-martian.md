---
title: "The Martian"
date: 2025-05-23
categories: [CTF, NahamCon2025, Warmups]
tags: [warmups,misc]
---

- **Category:** Miscellaneous 
- **Points:** 50
- **Solves:** 647

---

## Challenge

> Wow, this file looks like it's from outta this world!
> 
> **Attachment:** [challenge.martian](https://ctf.nahamcon.com/files/b760e9f6a2e40670cb3aabd0c1d7c429/challenge.martian?token=eyJ1c2VyX2lkIjo1ODksInRlYW1faWQiOjE3NywiZmlsZV9pZCI6NDh9.aDWx7w.0_paKkP3-uSH8ziV_Dk_0bKlo2Y)
>
> ***Author:** John Hammond*

---

## Solution
The first step was enumeration and finding out what kind of file the eliens use, I ran file challenge.martian command and discovered that it was a data file

next I ran binwalk to extract hidden data
```binwalk -e challenge.martian```

Several files were extracted, I ran ```file *``` command to identify their file type, one file stood up in particular called `34` and `957D`, they were both images and they contained the flag 

![flag image](/assets/img/34.png)

I added the file type prefix, scaled the image using magick convert tool
```convert 957D.png -resize 200% flag.png```

and then extracted the text using tesseract
```tesseract 957D.png flag```

> `flag{Odb031ac265b3e6538aff0d9f456004f}`
