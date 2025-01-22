import numpy as np
import matplotlib.pyplot as plt

def raw_to_image(raw_file, output_image, width, height, endian="little"):
    # Read the raw data from the file
    with open(raw_file, "rb") as f:
        buffer = f.read()
    # Convert raw data to a NumPy array (RGB565 is 2 bytes per pixel)
    rgb_values = []
    for i in range(0, len(buffer), 2):
        # Extract the LSB and MSB
        pixel = buffer[i] << 8 | buffer[i + 1]

        # Extract RGB components
        r = (pixel >> 11) & 0x1F
        g = (pixel >> 5) & 0x3F
        b = pixel & 0x1F
        r = (r * 255) // 31
        g = (g * 255) // 63
        b = (b * 255) // 31

        # Append the RGB tuple to the list
        rgb_values.append((r, g, b))
    rgb_values=np.array(rgb_values).reshape((height,width,3))
    plt.imshow(rgb_values)
    plt.axis("off")
    plt.savefig(output_image)
    plt.show()
    print(f"Image saved as '{output_image}'.")


# Example Usage
raw_to_image("/its/home/drs25/image.raw",
             "/its/home/drs25/Pictures/output_image_cv2.png",
             width=160, height=120)

