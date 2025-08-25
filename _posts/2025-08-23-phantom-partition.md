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
>**Attachment:** [disk.img](/assets/file/disk.img)
>

---

## Solution
extract the disk image strings to see any interesting strings

`strings disk.img`

we find some interesting info

    This is a secret file inside the hidden partition!
    4353437b68696464656e5f696e5f7468655f706172746974696f6e5f7461626c655f323032357d

decoding the hex value with cyberchef we get the flag.

a bash script to the flag:
```
strings disk.img | cut -d \n -f 5 | xxd -r -p 
```
> `CSC{hidden_in_the_partition_table_2025}`


---
