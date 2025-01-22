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
        
def save_numpy(filename, ar):

    # Write the raw byte array to a file
    try:
        with open(filename, "w") as file:
            s=""
            for i in range(len(ar)):
                for j in range(len(ar)):
                    s+=str(ar[i][j])+","
                s=s[:-1]+"\n"
                file.write(s)
                s=""
        print(f"Image saved as '{filename}' successfully.")
    except OSError as e:
        print(f"Failed to save image: {e}")
        
from CPCV import AI_cam
from ov7670 import camera

cam=AI_cam(camera)
a,buf=cam.takePic()
a=cam.convert_byte_array_to_image(buf)
save_image("/image.raw", buf)
del buf
save_numpy("/image.csv", a)
