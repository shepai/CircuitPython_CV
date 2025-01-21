import storage
import os

# Ensure the storage is writable
storage.remount("/", readonly=False)

def save_image(filename, buf):

    # Write the raw byte array to a file
    try:
        with open(filename, "wb") as file:
            file.write(buf)
        print(f"Image saved as '{filename}' successfully.")
    except OSError as e:
        print(f"Failed to save image: {e}")
        
from test import AI_cam
from ov7670 import camera

cam=AI_cam(camera)
a,buf=cam.takePic()

save_image("/image.raw", buf)