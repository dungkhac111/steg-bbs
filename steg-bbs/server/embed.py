from PIL import Image

print("=== EMBEDDING MESSAGE ===")

imgfile = input("Enter cover image: ")

msgfile = input("Enter message file: ")

posfile = input("Enter positions file: ")

img = Image.open(imgfile).convert("L")

pixels = list(img.getdata())

lc = len(pixels)

print("Total pixels:",lc)


with open(msgfile) as f:
    message = f.read()

bits = ''.join(format(ord(c),'08b') for c in message)

print("Message bits:",len(bits))


with open(posfile) as f:
    positions = [int(x.strip()) for x in f.readlines()]


for i,bit in enumerate(bits):

    pos = positions[i]

    pixel = pixels[pos]

    newpixel = (pixel & 254) | int(bit)

    print(f"pixel[{pos}] : {pixel} -> {newpixel}")

    pixels[pos] = newpixel


img.putdata(pixels)

out = "stego.png"

img.save(out)

print("Stego image saved:",out)
