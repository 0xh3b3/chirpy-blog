---
title: "Rabbit Hole"
date: 2025-05-20
categories: [CTF, Ctfroom, Stego]
tags: [stego]
---

# Gems
>
> Find the gems
>
> **File(1)** [stego_rabbit.zip](/assets/file/stego_rabbit.zip)
>

---

## Question #1

>What are the dimensions (width x height) of the stego_rabbit.png image? 
>(widthxheight)

![stego_rabbit](/assets/img/stego_rabbit.png)

I used exiftool tool to get the dimension, easy peasy
```exiftool stego_rabbit.png | grep -i "image size" | cut -d ":" -f 2```

> Solution: `1240x1240`

---

## Question #2

>A subtle, unencrypted message is hidden in the very first few pixels of the image's blue channel (LSB only). What is this message?

I made a script to extract the LSB from the blue channels
After extraction it returns binay bits which when converted to ASCII form a readable text, wait is that the flag??

```
from PIL import Image

def extract_lsb_message(image_path, max_bytes=100):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    bits = []
    for pixel in pixels:
        blue = pixel[2]  # Blue channel
        lsb = blue & 1   # Extract LSB
        bits.append(lsb)

        if len(bits) % 8 == 0:
            byte = int(''.join(str(b) for b in bits[-8:]), 2)
            if byte == 0 or len(bits) // 8 >= max_bytes:
                break

    # Convert bits to bytes
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        chars.append(chr(int(''.join(str(b) for b in byte), 2)))

    return ''.join(chars)

# Example usage
message = extract_lsb_message("stego_rabbit.png")
print("Hidden message:", messagThe flag is in uppercase i.e. THIS_IS_MY_FLAG e)
```
> Hidden Message: `FLAG_SIMPLE_LSB_HELLO`

## Question #3
> Using the critical information found in the image's metadata, a specific secret key, and careful analysis of the image's LSB data (which is encrypted and pseudo-randomly distributed), what is the main hidden alphanumeric flag?
>(The flag is in uppercase i.e. THIS_IS_MY_FLAG)