from bbs import BBS
from PIL import Image

print("=== BBS PARAMETERS ===")

p = int(input("Enter prime p (p mod 4 = 3): "))
q = int(input("Enter prime q (q mod 4 = 3): "))
seed = int(input("Enter seed: "))

imgfile = input("Enter cover image: ")
msgfile = input("Enter message file: ")

# đọc ảnh
img = Image.open(imgfile).convert("L")

width, height = img.size
lc = width * height

print("\n=== IMAGE INFO ===")
print("Width:", width)
print("Height:", height)
print("Total pixel positions (lc):", lc)

# đọc message
with open(msgfile) as f:
    message = f.read()

bits = ''.join(format(ord(c),'08b') for c in message)

count = len(bits)

print("\nMessage bits:", count)

bbs = BBS(p,q,seed)

positions = []

print("\n=== GENERATING POSITIONS ===")

for i in range(count):

    x = bbs.next()
    r = x % lc

    print(f"x{i+1} = {x}  →  r{i} = {r}")

    positions.append(str(r))

with open("positions.txt","w") as f:
    f.write("\n".join(positions))

print("\nPositions saved to positions.txt")
