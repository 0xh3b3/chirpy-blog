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
print("Hidden message:", message)
