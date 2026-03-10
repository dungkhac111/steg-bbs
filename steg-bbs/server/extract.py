from PIL import Image

print("=== EXTRACT MESSAGE ===")

imgfile = input("Enter stego image: ")
posfile = input("Enter positions file: ")

img = Image.open(imgfile).convert("L")
pixels = list(img.getdata())

with open(posfile) as f:
    positions = [int(x.strip()) for x in f.readlines()]

bits = ""
message = ""

for pos in positions:

    pixel = pixels[pos]

    bits += str(pixel & 1)

    if len(bits) == 8:

        char = chr(int(bits,2))

        if char == '\0':
            break

        message += char

        bits = ""

print("Recovered message:", message)
