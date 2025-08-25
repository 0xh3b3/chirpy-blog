---
title: "Phantom Partition"
date: 2025-08-23
categories: [CTF, SANReN, Forensics]
tags: [forensics]
---

# Challenge
>***Points:** 15*
>
>You are presented with disk image that contains a hidden partition.
>
>Are you able to recover the file hidden in the partition holding the flag?
>
>Flag format: CSC{...}
>
>**Attachment:** [hidden_layers.png](/assets/file/hidden_layers.png)
>

---

## Solution
Wea are represented with an image

![hidden_layers.png](/assets/file/hidden_layers.png)
>

I tried running zsteg and I found some two interesting data

    meta Comment        .. text: "CTFkey123"
    b2,rgba,lsb,xy      .. text: "d2VsY29tZV90b19zdGVnYW5vX2xhbmQ=\n"

I decoded the second string to base 64

    echo d2VsY29tZV90b19zdGVnYW5vX2xhbmQ= |base64 -d

>welcome_to_stegano_land

Trying to see if there are embedded files with binwalk.

    binwalk -e hidden_layers.png 
 
 I got a passphrase protected zip file, I tried bruteforcing it with zip2john but nothing
so I tried using the data I found using zsteg as the passphrase
    
    welcome_to_stegano_land

it opened and I got a file with some hex values

    \x00\x07\x05\x10\x0a\x17\x58\x5d\x5d\x30\x0b\x2e\x0a\x13\x1c\x6e\x5e\x52\x3a\x31\x34\x18\x18

I thougth of every possible decryption that require a key and I landed on XOR, so I came up with a simple python decription script.

python3 solver.py
```
ciphertext_hex = "000705100a17585d5d300b2e0a131c6e5e523a31341818"
key = "CTFkey123"

# Convert the hex string to a bytes object
ciphertext = bytes.fromhex(ciphertext_hex)
key_bytes = key.encode('utf-8')

# Prepare the key for XORing by repeating it
key_repeated = (key_bytes * (len(ciphertext) // len(key_bytes) + 1))[:len(ciphertext)]

# Perform the XOR operation
decrypted_bytes = bytes([c ^ k for c, k in zip(ciphertext, key_repeated)])

# Decode the result to a string
decrypted_text = decrypted_bytes.decode('utf-8')

print(f"The decrypted text is: {decrypted_text}")
```
The decrypted text is: 
>`CSC{onions_have_layers}`