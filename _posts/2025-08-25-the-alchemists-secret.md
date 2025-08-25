---
title: "The Alchemist's Secret"
date: 2025-08-23
categories: [CTF, SANReN, Cryptography]
tags: [srypto]
---

# Challenge
>***Points:** 30*
>
>An old parchment was discovered in a hidden compartment of an alchemist’s desk. The parchment contains an encrypted message, and a note reads: "Only those who understand the golden sequence can unveil the secret."
>
>Your task is to decrypt the message and retrieve the flag.
>
>Flag format: CSC{...}
>
>**Attachment:** [info.txt](/assets/file/info.txt)
>

---

## Solution
Lets check out the content of the file.

    cat info.txt | base64 -d

    CTD{wmm_b0oosm_e3be3sc3}

something close to, but not the flag.
According to the challenge description, there is an additional side note that says

    "Only those who understand the golden sequence can unveil the secret."

>golden Sequence = Golden Ratio = PHI = Fibunoci Sequence

A quick google search on Fibunocci cypher decryption and I go tons of them but I went with this one

[wordsmithingtools.com](https://wordsmithingtools.com/fibonacci-cipher)

and I got the flag

>`CSC{the_g0lden_s3qu3nc3}`