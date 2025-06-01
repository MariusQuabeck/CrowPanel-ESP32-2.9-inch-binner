from PIL import Image, ImageOps
import numpy as np
import sys
import os

# Constants for CrowPanel 2.9" display
WIDTH = 296
HEIGHT = 128

def convert_image_to_bin(input_path, output_path="txt.bin"):
    # Load and convert image to 1-bit
    image = Image.open(input_path).convert("1")  # Convert to 1-bit (black & white)

    # Resize and center on white canvas
    canvas = Image.new("1", (WIDTH, HEIGHT), 1)  # White background
    image = ImageOps.contain(image, (WIDTH, HEIGHT))
    x_offset = (WIDTH - image.width) // 2
    y_offset = (HEIGHT - image.height) // 2
    canvas.paste(image, (x_offset, y_offset))

    # Convert to numpy array
    pixels = np.array(canvas, dtype=np.uint8)

    # Convert to bit-packed binary (column-major, reversed bits)
    bin_data = bytearray()
    for x in range(WIDTH):
        for y in range(0, HEIGHT, 8):
            byte = 0
            for bit in range(8):
                if y + bit < HEIGHT and pixels[y + bit, x] == 0:  # 0 = black
                    byte |= (1 << bit)
            byte = int('{:08b}'.format(byte)[::-1], 2)  # Bit-reverse each byte
            bin_data.append(byte)

    # Write output file
    with open(output_path, "wb") as f:
        f.write(bin_data)
    print(f"Saved: {output_path} ({len(bin_data)} bytes)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_txtbin.py input_image.png [output_file]")
    else:
        in_file = sys.argv[1]
        out_file = sys.argv[2] if len(sys.argv) > 2 else "txt.bin"
        convert_image_to_bin(in_file, out_file)

