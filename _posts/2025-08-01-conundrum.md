---
title: "KeepGoin"
date: 2025-08-01
categories: [CTF, mmuCTF, Forencics]
tags: [forensics]
---

# Challenge
>***Points:** 100*

>Interns and important files don’t always mix well, they deleted it
>**Attachment:** [keepGoin.zip](/assets/file/keepGoin.zip)
>
>***Author:** mburk4*
---

## Solution
Lets fire up our favourite forensic tool `autopsy`, must run with sudo. It has a web interactivity

Using autopsy requires alot of forensics knowledge which I might advice the reader to go through the THM forensics module if they have are not yet familiar with it.

Keep in mind `file systems` in this case since its a usb it is most likely to be __fat32__

